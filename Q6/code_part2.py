from collections import deque

def find_loop(position, list_of_objects, grid):
    visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0 
    queue = deque([(position[0], position[1], dir)])
    
    while queue:
        x, y, dir = queue.popleft()

        if (x, y, dir) in visited:
            return True

        visited.add((x, y, dir))

        new_x = x + directions[dir][0]
        new_y = y + directions[dir][1]

        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
            if (new_x, new_y) in list_of_objects:
                new_dir = (dir + 1) % 4
                queue.append((x, y, new_dir))
            else:
                queue.append((new_x, new_y, dir))

    return False

def find_num_loops(starting_position, set_of_path, list_of_obstacles, grid):
    num_loops = 0

    for space in set_of_path:
        x, y = space
        if grid[x][y] == '.':
            list_of_obstacles.add(space)
            if find_loop(starting_position, list_of_obstacles, grid):
                num_loops += 1
            list_of_obstacles.remove(space)
    
    return num_loops

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
                queue.append((new_x, new_y))

        visited.add((x, y))
        

    return visited

def find_existing_obstacle_position(grid):
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
    list_of_obstacles = find_existing_obstacle_position(grid)
    set_of_path = find_distinct_positions(starting_position, list_of_obstacles, 0, grid)
    num_loops = find_num_loops(starting_position, set_of_path, list_of_obstacles, grid)
    print(num_loops)