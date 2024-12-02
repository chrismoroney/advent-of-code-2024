def is_safe(line):
    first_val, second_val = line[0], line[1]
    is_increasing, is_decreasing = False, False
    remove_bad_level = False

    if first_val == second_val:
        return False
    elif first_val < second_val:
        is_increasing = True
    else:
        is_decreasing = True

    for i in range(1, len(line)):
        if is_decreasing:
            if line[i-1] - line[i] != 1 and line[i-1] - line[i] != 2 and line[i-1] - line[i] != 3:
                return False
            
        elif is_increasing:
            if line[i] - line[i-1] != 1 and line[i] - line[i-1] != 2 and line[i] - line[i-1] != 3:
                return False

    return True

def count_safe(lines):
    counter = 0
    for line in lines:
        if is_safe(line):
            counter += 1
    
    return counter
    

def parse_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            vals = line.split(' ')
            new_vals = []
            for val in vals:
                val = int(val.replace('\n', ''))
                new_vals.append(val)
            lines.append(new_vals)
    return lines

if __name__ == "__main__":
    lines = parse_file('./input.txt')
    num_safe = count_safe(lines)
    print(num_safe)