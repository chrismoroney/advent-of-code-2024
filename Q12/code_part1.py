from collections import deque

def find_prices(areas, perimeters):
    return [area * perimeter for area, perimeter in zip(areas, perimeters)]

def find_areas(sections):
    return [len(section) for section in sections]


def find_perimeter(sections):
    perimeters = []
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    for section in sections:
        perimeter = 0
        for (i, j) in section:
            perimeter += 4
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                
                if (new_i, new_j) in section:
                    perimeter -= 1
        perimeters.append(perimeter)
    
    return perimeters


def find_sections(grid):
    visited = set()
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    sections = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) not in visited:
                visited.add((i, j))
                section = {(i, j)}
                queue = deque([(i, j)])
                plant = grid[i][j]
                while queue:
                    q_i, q_j = queue.popleft()
                    for direction in directions:
                        new_i = q_i + direction[0]
                        new_j = q_j + direction[1]
                        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[i]) and grid[new_i][new_j] == plant:
                            if (new_i, new_j) not in section:
                                section.add((new_i, new_j))
                                visited.add((new_i, new_j))
                                queue.append((new_i, new_j))
                sections.append(section)
    return sections

def parse_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            line = [c for c in line.replace('\n', '')]
            grid.append(line)

    return grid

if __name__ == "__main__":
    grid = parse_file('./input.txt')
    sections = find_sections(grid)
    areas = find_areas(sections)
    perimeters = find_perimeter(sections)
    prices = find_prices(areas, perimeters)
    print(sum(prices))