from collections import deque

def find_prices(areas, sides):
    return [area * side for area, side in zip(areas, sides)]

def find_areas(sections):
    return [len(section) for section in sections]


def find_sides(sections):
    '''
    function inspired from hyperneutrino
    '''
    sides = []
    for section in sections:
        corners = set()
        for i, j in section:
            for c_i, c_j in [(i - 0.5, j - 0.5), (i + 0.5, j - 0.5), (i + 0.5, j + 0.5), (i - 0.5, j + 0.5)]:
                corners.add((c_i, c_j))
        num_corners = 0
        for c_i, c_j in corners:
            config = [(sr, sc) in section for sr, sc in [(c_i - 0.5, c_j - 0.5), (c_i + 0.5, c_j - 0.5), (c_i + 0.5, c_j + 0.5), (c_i - 0.5, c_j + 0.5)]]
            num = sum(config)

            if num == 1 or num == 3:
                num_corners += 1
            elif num == 2:
                if config == [True, False, True, False] or config == [False, True, False, True]:
                    num_corners += 2

        sides.append(num_corners)
    
    return sides

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
    sides = find_sides(sections)
    prices = find_prices(areas, sides)
    print(sum(prices))