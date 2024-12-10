from collections import deque

def find_score(grid, head):
    score = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    x, y = head[0], head[1]
    visited = {(x, y)}
    
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for direction in directions:
            new_x = x + direction[0]
            new_y = y + direction[1]

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                if grid[new_x][new_y] == grid[x][y] + 1:
                    if not (new_x, new_y) in visited:
                        if grid[new_x][new_y] == 9:
                            score += 1
                        else:
                            queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

    return score

def get_scores(grid, trailheads):
    scores = []

    for head in trailheads:
        score = find_score(grid, head)
        scores.append(score)

    return scores


def find_trailheads(grid):
    trailheads = set()

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                trailheads.add((x, y))
    
    return trailheads

def parse_file(file_path):
    grid = []

    with open(file_path, 'r') as file:
        for line in file:
            line = list(line.replace('\n', ''))
            line = [int(val) for val in line]
            grid.append(line)

    return grid

if __name__ == "__main__":
    grid = parse_file('./input.txt')
    trailheads = find_trailheads(grid)
    scores = get_scores(grid, trailheads)
    print(sum(scores))