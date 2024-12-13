from collections import defaultdict

def check_num_tickets(machines_and_methods):
    tickets = []
    
    for _, combos in machines_and_methods.items():
        max_tickets = 400
        for combo in combos:
            if combo[0] * 3 + combo[1] <= max_tickets:
                tickets.append(combo[0] * 3 + combo[1])
                max_tickets = combo[0] * 3 + combo[1]

    return tickets


def check_valid_machines(a_button, b_button, prize):
    map_idx_to_win_prize = defaultdict(set)

    for i in range(len(a_button)):
        for x in range(1, 101):
            for y in range(1, 101):
                if a_button[i][0] * x + b_button[i][0] * y == prize[i][0]:
                    if a_button[i][1] * x + b_button[i][1] * y == prize[i][1]:
                        map_idx_to_win_prize[i].add((x, y))
    return map_idx_to_win_prize

def parse_file(file_path):
    counter = 0
    a_button = []
    b_button = []
    prize = []

    with open(file_path, 'r') as file:
        for line in file:
            if counter % 4 == 0:
                line = line.replace('Button A: X+', '')
                line = line.replace(', Y+', ' ')
                line = list(int(vals) for vals in line.split())
                a_button.append(line)
            elif counter % 4 == 1:
                line = line.replace('Button B: X+', '')
                line = line.replace(', Y+', ' ')
                line = list(int(vals) for vals in line.split())
                b_button.append(line)
            elif counter % 4 == 2:
                line = line.replace('Prize: X=', '')
                line = line.replace(', Y=', ' ')
                line = list(int(vals) for vals in line.split())
                prize.append(line)
            
            if counter % 4 == 3:
                counter = 0
            else:
                counter += 1

    return a_button, b_button, prize

if __name__ == "__main__":
    a_button, b_button, prize = parse_file('./input.txt')
    machines_and_methods = check_valid_machines(a_button, b_button, prize)
    num_tickets = check_num_tickets(machines_and_methods)
    print(sum(num_tickets))
    