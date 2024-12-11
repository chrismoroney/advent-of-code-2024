from functools import cache

@cache
def apply_rules_to_stones(stone, steps_remaining):
    if steps_remaining == 0:
        return 1
    
    if stone == 0:
        return apply_rules_to_stones(1, steps_remaining - 1)
    
    s = str(stone)
    if len(s) % 2 == 0:
        mid = len(s) // 2
        return apply_rules_to_stones(int(s[:mid]), steps_remaining - 1) + apply_rules_to_stones(int(s[mid:]), steps_remaining - 1)
    
    return apply_rules_to_stones(stone * 2024, steps_remaining - 1)


def apply_rules_75_times(stones):
    total = 0
    for stone in stones:
        total += apply_rules_to_stones(stone, 75)
    return total

def parse_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            return [int(val) for val in line.split()]

if __name__ == "__main__":
    stones = parse_file('./input.txt')
    total = apply_rules_75_times(stones)
    print(total)