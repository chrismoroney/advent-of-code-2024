import re

def sum_nums(nums):
    return sum(nums)

def get_products_from_matches(matches):
    regex_mul = r"mul\((\d+),(\d+)\)"

    add_to_return_nums = True
    return_nums = []

    for match in matches:

        if match == "don't()":
            add_to_return_nums = False
            continue

        if match == "do()":
            add_to_return_nums = True
            continue

        if add_to_return_nums:
            nums = re.search(regex_mul, match)
            num1, num2 = map(int, nums.groups())
            return_nums.append(num1 * num2)

    return return_nums


def parse_input_string(input_str):
    regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    matches = re.findall(regex, input_str)
    return matches


def parse_file(file_path):
    input_str = ""
    with open(file_path, 'r') as file:
        for line in file:
            input_str += line
    return input_str

if __name__ == "__main__":
    input_str = parse_file('./input.txt')
    matches = parse_input_string(input_str)
    nums = get_products_from_matches(matches)
    ans = sum_nums(nums)
    print(ans)