from tqdm import tqdm

def get_checksum(shifted_blocks):
    checksum = 0

    for i in range(len(shifted_blocks)):
        if shifted_blocks[i] != '.':
            checksum += i * int(shifted_blocks[i])

    return checksum

def shift_blocks(translation, largest_id, size, loc):
    '''
    inspired from William Y Feng
    '''
    for id in tqdm(range(largest_id, -1, -1)):
        free_spaces_from_idx = 0
        free_idx = 0

        while free_idx < loc[id] and free_spaces_from_idx < size[id]:
            free_idx = free_idx + free_spaces_from_idx
            free_spaces_from_idx = 0

            while translation[free_idx] != '.':
                free_idx += 1
            while free_idx + free_spaces_from_idx < len(translation) and translation[free_idx + free_spaces_from_idx] == '.':
                free_spaces_from_idx += 1

        if free_idx >= loc[id]:
            continue
    
        for i in range(free_idx, free_idx + size[id]):
            translation[i] = id
        for i in range(loc[id], loc[id] + size[id]):
            translation[i] = '.'
    
    return translation


def translate_line(line):
    translation = []
    size = []
    loc = []
    id = 0
    
    for i, val in enumerate(line):
        val = int(val)
        if i % 2 == 0:
            loc.append(len(translation))
            size.append(val)
            translation += [id] * val
            id += 1
        else:
            translation += '.' * val
    
    return translation, id-1, size, loc

def parse_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            return line

if __name__ == "__main__":
    line = parse_file('./input.txt')
    translation, largest_id, size, loc = translate_line(line)
    shifted_blocks = shift_blocks(translation, largest_id, size, loc)
    #print(shifted_blocks)
    checksum = get_checksum(shifted_blocks)
    print(checksum)
