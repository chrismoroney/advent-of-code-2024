def sum_diffs(diffs):
    return sum(diffs)

def find_differences(first_group, second_group):
    diffs = []
    for i in range(len(first_group)):
        diff = abs(int(first_group[i]) - int(second_group[i]))
        diffs.append(diff)
    
    return diffs

def parse_file(file_path):
    first_group, second_group = [], []
    with open(file_path, 'r') as file:
        for line in file:
            vals = tuple(line.split('   '))
            first_group.append(vals[0])
            second_group.append(vals[1].replace('\n', ''))
    
    return sorted(first_group), sorted(second_group)
            


if __name__ == "__main__":
    first_group, second_group = parse_file('./input.txt')
    diffs = find_differences(first_group, second_group)
    print(sum_diffs(diffs))