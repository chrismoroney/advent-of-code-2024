def get_checksum(shifted_blocks):
    checksum = 0

    for i in range(len(shifted_blocks)):
        checksum += i * int(shifted_blocks[i])

    return checksum

def shift_blocks(translation):
    
    leftmost_idx = 0
    while translation[leftmost_idx] != '.':
        leftmost_idx += 1

    n = len(translation)-1
    while translation[n] == '.':
        n -= 1
    
    while n > leftmost_idx:
        translation[leftmost_idx] = translation[n]
        translation[n] = '.'

        while translation[n] == '.':
            n -= 1
        while translation[leftmost_idx] != '.':
            leftmost_idx += 1
        
    translation = [val for val in translation if val != '.']

    return translation


def translate_line(line):
    translation = []
    id = 0
    for i in range(len(line)):
        if i % 2 == 0:
            for i in range(int(line[i])):
                translation.append(id)
            id += 1
        else:
            for i in range(int(line[i])):
                translation.append('.')
    
    return translation

def parse_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            return line

if __name__ == "__main__":
    line = parse_file('./input.txt')
    translation = translate_line(line)
    shifted_blocks = shift_blocks(translation)
    checksum = get_checksum(shifted_blocks)
    print(checksum)
