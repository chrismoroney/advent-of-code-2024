from collections import defaultdict
from functools import cmp_to_key

def get_middle_vals(updates):
    return_list = []
    
    for update in updates:
        n = len(update)
        return_list.append(int(update[n//2]))

    return return_list


def reorganize_updates(updates, before):
    
    def compare(a, b):
        if a in before[b]:
            return -1
        if b in before[a]:
            return 1
        return 0

    for update in updates:
        update.sort(key=cmp_to_key(compare))

    return updates

def get_incorrect_order_updates(updates, before_rules):
    return_list = []
    
    for update in updates:
        nums = update.split(',')
        add_to_list = False
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] in before_rules[nums[i]]:
                    add_to_list = True
                    break

        if add_to_list:
            return_list.append(nums)
                    
    return return_list

def organize_rules(ordering_rules):
    before = defaultdict(set)

    for rule in ordering_rules:
        first_rule, second_rule = rule.split('|')
        before[second_rule].add(first_rule)

    return before

def parse_file(file_path):
    ordering_rules = []
    updates = []

    switch = False

    with open(file_path, 'r') as file:
        for line in file:
            if line == '\n':
                switch = True
                continue
            
            if switch:
                updates.append(line.replace('\n', ''))
            else:
                ordering_rules.append(line.replace('\n', ''))
    
    return ordering_rules, updates

if __name__ == "__main__":
    ordering_rules, updates = parse_file('./input.txt')
    order_before = organize_rules(ordering_rules)
    updates_in_wrong_order = get_incorrect_order_updates(updates, order_before)
    reorganized_updates = reorganize_updates(updates_in_wrong_order, order_before)
    middle_vals = get_middle_vals(reorganized_updates)
    print(sum(middle_vals))