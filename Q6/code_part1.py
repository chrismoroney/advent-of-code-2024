from collections import deque

def find_distinct_positions(position, list_of_objects, direction_idx, grid):
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    queue = deque([position])
    
    while queue:
        x, y = queue.popleft()

        new_x = x + directions[direction_idx][0]
        new_y = y + directions[direction_idx][1]

        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if (new_x, new_y) in list_of_objects:
                direction_idx = (direction_idx + 1) % 4
                queue.append((x, y))
            else:
                visited.add((x, y))
                queue.append((new_x, new_y))

        visited.add((x, y))
        

    return len(visited)

def find_obstacle_position(grid):
    list_of_obstacles = set()
    n = len(grid)

    for x in range(n):
        for y in range(len(grid[x])):
            if grid[x][y] == '#':
                coords = (x, y)
                list_of_obstacles.add(coords)

    return list_of_obstacles  


def find_starting_position(grid):
    n = len(grid)

    for x in range(n):
        for y in range(len(grid[x])):
            if grid[x][y] == '^':
                return x, y
            
    return None, None

def parse_file(file_path):
    grid = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.replace('\n', ''))
            grid.append(row)
    
    return grid


if __name__ == "__main__":
    grid = parse_file('./input.txt')
    start_x, start_y = find_starting_position(grid)
    starting_position = (start_x, start_y)
    list_of_obstacles = find_obstacle_position(grid)
    distinct_positions = find_distinct_positions(starting_position, list_of_obstacles, 0, grid)
    print(distinct_positions)