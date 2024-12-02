def is_all_increasing(sub_line):
    for i in range(1, len(sub_line)):
        diff = sub_line[i] - sub_line[i - 1]
        if diff < 1 or diff > 3:
            return False
    return True

def is_all_decreasing(sub_line):
    for i in range(1, len(sub_line)):
        diff = sub_line[i - 1] - sub_line[i]
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe(line):
    if is_all_increasing(line) or is_all_decreasing(line):
        return True
    
    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]
        if is_all_increasing(modified_line) or is_all_decreasing(modified_line):
            return True
        
    return False


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
    lines = parse_file('./input_sample.txt')
    num_safe = count_safe(lines)
    print(num_safe)