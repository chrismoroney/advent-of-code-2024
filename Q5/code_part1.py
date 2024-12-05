from collections import defaultdict

def get_middle_vals(updates):
    return_list = []
    
    for update in updates:
        n = len(update)
        return_list.append(int(update[n//2]))

    return return_list

def get_correct_order_updates(updates, rules_map):
    return_list = []
    
    for update in updates:
        nums = update.split(',')
        i = 0
        add_to_list = True
        while i < len(nums) - 1:
            if nums[i+1] not in rules_map[nums[i]]:
                add_to_list = False
            i += 1

        if add_to_list:
            return_list.append(nums)
                    
    return return_list

def organize_rules(ordering_rules):
    rules_map = defaultdict(set)

    for rule in ordering_rules:
        first_rule, second_rule = rule.split('|')
        if first_rule not in rules_map:
            set_to_add = set()
            set_to_add.add(second_rule)
            rules_map[first_rule] = set_to_add
        else:
            rules_map[first_rule].add(second_rule)

    return rules_map

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
    rules_map = organize_rules(ordering_rules)
    updates_in_right_order = get_correct_order_updates(updates, rules_map)
    middle_vals = get_middle_vals(updates_in_right_order)
    print(sum(middle_vals))