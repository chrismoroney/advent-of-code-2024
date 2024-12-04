def count_xmas_words(lines):
    counter = 0

    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            if lines[i][j] == 'A':
                diags = 0
                current_str = ""
                for dir in range(-1, 2):
                    new_i = i + dir
                    new_j = j + dir
                    current_str += lines[new_i][new_j]

                if current_str == "MAS" or current_str == "SAM":
                    diags += 1

                current_str = ""
                for dir in range(-1, 2):
                    new_i = i + dir
                    new_j = j - dir
                    current_str += lines[new_i][new_j]
                
                if current_str == "MAS" or current_str == "SAM":
                    diags += 1
                
                if diags == 2:
                    counter += 1

    return counter
    

def parse_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(list(line.strip()))
    
    return lines

if __name__ == "__main__":
    lines = parse_file('./input.txt')
    count = count_xmas_words(lines)
    print(count)