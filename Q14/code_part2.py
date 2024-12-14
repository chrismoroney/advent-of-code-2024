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


def simulate_x_seconds(robots_pos, robots_vel, time):
    results = []

    for pos, vel in zip(robots_pos, robots_vel):
        dx = vel[0] * time + pos[0]
        dy = vel[1] * time + pos[1]

        new_x = dx % 101
        new_y = dy % 103

        results.append((new_x, new_y))
    
    return results

def simulate_over_time(robots_pos, robots_vel):
    min_sf = float("inf")
    best_iteration = None

    for time in range(101 * 103):
        result = []
        result.append(simulate_x_seconds(robots_pos, robots_vel, time))

        for res in result:
            quad = get_vals_in_quadrants(res)
            sf = get_safety_factor(quad)

            if sf < min_sf:
                min_sf = sf
                best_iteration = time
    return best_iteration


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
    best_itr = simulate_over_time(robots_pos, robots_vel)
    print(best_itr)