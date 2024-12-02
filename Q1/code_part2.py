def sum_scores(scores):
    return sum(scores)

def count_similarity_score(first_group, second_group):
    second_group_map = {}
    scores = []

    for i in range(len(second_group)):
        if second_group[i] not in second_group_map:
            second_group_map[second_group[i]] = 1
        else:
            second_group_map[second_group[i]] += 1
    
    for j in range(len(first_group)):
        if first_group[j] in second_group_map:
            score = first_group[j] * second_group_map[first_group[j]]
            scores.append(score)

    return scores


def parse_file(file_path):
    first_group, second_group = [], []
    with open(file_path, 'r') as file:
        for line in file:
            vals = tuple(line.split('   '))
            first_group.append(int(vals[0]))
            second_group.append(int(vals[1].replace('\n', '')))
    
    return sorted(first_group), sorted(second_group)
            


if __name__ == "__main__":
    first_group, second_group = parse_file('./input.txt')
    scores = count_similarity_score(first_group, second_group)
    print(sum_scores(scores))