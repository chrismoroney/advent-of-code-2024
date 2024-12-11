def apply_rules_to_stones(stones):
    new_stones = []
    for stone in stones:
        if int(stone) == 0:
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = stone[:mid]
            right = stone[mid:]
            left_num = str(int(left)) if left else 0
            right_num = str(int(right)) if right else 0
            new_stones.append(left_num)
            new_stones.append(right_num)
        else:
            new_stones.append(str(int(stone) * 2024))
    
    return new_stones

def apply_rules_25_times(stones):
    for _ in range(25):
        stones = apply_rules_to_stones(stones)
    return stones

def parse_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            return line.split()

if __name__ == "__main__":
    stones = parse_file('./input.txt')
    new_stones = apply_rules_25_times(stones)
    print(len(new_stones))