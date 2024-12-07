def check_list(target, list_of_nums, current_total):
    if len(list_of_nums) == 0 and current_total != target:
        return False

    if len(list_of_nums) == 0 and current_total == target:
        return True
    
    added_val = current_total + int(list_of_nums[0])
    mult_val = current_total * int(list_of_nums[0])
    concat_val = int(str(current_total) + str(list_of_nums[0]))
    
    return check_list(target, list_of_nums[1:], added_val) or check_list(target, list_of_nums[1:], mult_val) or check_list(target, list_of_nums[1:], concat_val)

def check_nums(nums):
    results = []

    for list_of_nums in nums:
        if check_list(int(list_of_nums[0]), list_of_nums[2:], int(list_of_nums[1])):
            results.append(int(list_of_nums[0]))

    return results

def parse_file(file_path):
    nums = []

    with open(file_path, 'r') as file:
        for line in file:
            vals = line.replace(':', '').replace('\n', '').split(' ')
            nums.append(vals)
    
    return nums

if __name__ == "__main__":
    nums = parse_file('./input.txt')
    results = check_nums(nums)
    print(sum(results))