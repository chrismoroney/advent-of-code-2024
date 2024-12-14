def get_safety_factor(quadrants):
    answer = 1
    for q in quadrants:
        answer *= q

    return answer

def get_vals_in_quadrants(results):
    quads = [0] * 4
    width = 101
    height = 103

    for r_x, r_y in results:
        if r_x < (width - 1) // 2 and r_y < (height - 1) // 2:
            quads[0] += 1
        elif r_x > (width - 1) // 2 and r_y < (height - 1) // 2:
            quads[1] += 1
        elif r_x < (width - 1) // 2 and r_y > (height - 1) // 2:
            quads[2] += 1
        elif r_x > (width - 1) // 2 and r_y > (height - 1) // 2:
            quads[3] += 1

    return quads
    


def simulate_100_seconds(robots_pos, robots_vel):
    results = []

    for pos, vel in zip(robots_pos, robots_vel):
        dx = vel[0] * 100 + pos[0]
        dy = vel[1] * 100 + pos[1]

        new_x = dx % 101
        new_y = dy % 103

        results.append((new_x, new_y))
    
    return results


def parse_file(file_path):
    pos = []
    vel = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.replace('p=', '').replace(' v=', ',')
            line = line.split(',')
            line = [int(val) for val in line]
            pos.append((line[0], line[1]))
            vel.append((line[2], line[3]))
    
    return pos, vel

if __name__ == "__main__":
    robots_pos, robots_vel = parse_file('./input.txt')
    results = simulate_100_seconds(robots_pos, robots_vel)
    quadrants = get_vals_in_quadrants(results)
    answer = get_safety_factor(quadrants)
    print(quadrants)
    print(answer)