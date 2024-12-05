from collections import defaultdict

def get_middle_vals(updates):
    return_list = []
    
    for update in updates:
        n = len(update)
        return_list.append(int(update[n//2]))

    return return_list

def get_correct_order_updates(updates, after_rules):
    return_list = []
    
    for update in updates:
        nums = update.split(',')
        add_to_list = True
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if nums[j] not in after_rules[nums[i]]:
                    add_to_list = False
                    break

        if add_to_list:
            return_list.append(nums)
                    
    return return_list

def organize_rules(ordering_rules):
    after = defaultdict(set)

    for rule in ordering_rules:
        first_rule, second_rule = rule.split('|')
        after[first_rule].add(second_rule)

    return after

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
    order_after = organize_rules(ordering_rules)
    updates_in_right_order = get_correct_order_updates(updates, order_after)
    middle_vals = get_middle_vals(updates_in_right_order)
    print(sum(middle_vals))