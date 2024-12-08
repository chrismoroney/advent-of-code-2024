from collections import defaultdict

def count_inbound_antinodes(grid, antinodes):
    antinodes = set(antinodes)
    not_inbound = 0

    for antinode in antinodes:
        x = antinode[0]
        y = antinode[1]

        if not (0 <= x < len(grid) and 0 <= y < len(grid)):
            not_inbound += 1
    
    return len(antinodes) - not_inbound

def get_antinode_locations(freqs, map_of_freqs):
    antinodes = []
    for freq in freqs:
        list_of_locations = map_of_freqs[freq]
        for i in range(len(list_of_locations)-1):
            for j in range(i+1, len(list_of_locations)):
                dx = list_of_locations[j][0] - list_of_locations[i][0]
                dy = list_of_locations[j][1] - list_of_locations[i][1]

                antinode_x = list_of_locations[i][0] - dx
                antinode_y = list_of_locations[i][1] - dy

                antinodes.append((antinode_x, antinode_y))

                antinode_x = list_of_locations[j][0] + dx
                antinode_y = list_of_locations[j][1] + dy

                antinodes.append((antinode_x, antinode_y))
    return antinodes


def get_map_of_freqs(grid, freqs):
    map_of_freqs = defaultdict(list)

    for freq in freqs:
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == freq:
                    if grid[i][j] not in map_of_freqs:
                        map_of_freqs[grid[i][j]] = [(i, j)]
                    else:
                        map_of_freqs[grid[i][j]].append((i, j))

    return map_of_freqs

def get_set_of_freqs(grid):
    freqs = set()

    for line in grid:
        for c in line:
            if c != '.' and c not in freqs:
                freqs.add(c)
    
    return freqs

def parse_file(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file:
            grid.append([char for char in line.replace('\n', '')])

    return grid

if __name__ == "__main__":
    grid = parse_file('./input.txt')
    freqs = get_set_of_freqs(grid)
    map_of_freqs = get_map_of_freqs(grid, freqs)
    antinodes = get_antinode_locations(freqs, map_of_freqs)
    answer = count_inbound_antinodes(grid, antinodes)
    print(answer)
