def search_xmas(lines, x, y, direction, idx):
    if idx == 3:
        return True
    
    chars = ['M', 'A', 'S']
    width = len(lines)
    height = len(lines[0])

    new_x = x + direction[0]
    new_y = y + direction[1]

    if 0 <= new_x < width and 0 <= new_y < height and lines[new_x][new_y] == chars[idx]:
        return search_xmas(lines, new_x, new_y, direction, idx+1)
        
    return False


def count_xmas_words(lines):
    counter = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'X':
                for direction in directions:
                    if search_xmas(lines, i, j, direction, 0):
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