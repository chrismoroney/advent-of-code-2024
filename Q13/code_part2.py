from collections import defaultdict

def check_num_tickets(machines_and_methods):
    tickets = []
    
    for _, combos in machines_and_methods.items():
        for combo in combos:
            tickets.append(combo[0] * 3 + combo[1])

    return tickets


def check_valid_machines(a_button, b_button, prize):
    '''
    inspired from hyperneutrino - https://www.youtube.com/watch?v=-5J-DAsWuJc
    '''
    valid_combos = defaultdict(set)

    for i in range(len(a_button)):
        a_x = a_button[i][0]
        a_y = a_button[i][1]
        b_x = b_button[i][0]
        b_y = b_button[i][1]
        p_x = prize[i][0]
        p_y = prize[i][1]

        c_a = (p_x * b_y - p_y * b_x) / (a_x * b_y - a_y * b_x)
        c_b = (p_x - a_x * c_a) / b_x
        if c_a % 1 == 0 and c_b % 1 == 0:
            valid_combos[i].add((int(c_a), int(c_b)))

    return valid_combos


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
                line = list(int(vals) + 10000000000000 for vals in line.split())
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
    