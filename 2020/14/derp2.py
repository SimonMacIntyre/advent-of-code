from itertools import product
import re

file = open('input', 'r')
data = file.readlines()


# 36 bit
def int_to_binary(value):
    return f"{int(value):036b}"


# 36 bit
def binary_to_int(value):
    return int(str(value), 2)


def process_floating_bits_from_binary(binary):
    new_binaries = []
    floating_bits = binary.count('X')
    all_possible_sequences = [x for x in product([0, 1], repeat=floating_bits)]
    for seq in all_possible_sequences:
        new_binary = binary
        q = 0
        for i, char in enumerate(new_binary):
            if char == 'X':
                new_binary = new_binary[:i] + str(seq[q]) + new_binary[i + 1:]
                q += 1
        new_binaries.append(new_binary)
    return new_binaries


def apply_mask_to_binary(mask, binary):
    new_binary = ''
    for i, bin in enumerate(binary):
        if mask[i] == 'X':
            new_binary += 'X'
            continue
        if mask[i] == '0':
            new_binary += bin
        if mask[i] == '1':
            new_binary += '1'
    return new_binary


results = {}

for line in data:
    if re.match(r'mask =', line):
        mask = line[7:]
    else:
        pattern = re.match(r"mem\[(\d*)\] = (\d*)", line)  # mem[8] = 11
        memories = process_floating_bits_from_binary(apply_mask_to_binary(mask, int_to_binary(pattern.group(1))))
        value = pattern.group(2)
        for memory in memories:
            results[memory] = value

print(sum([int(x) for x in results.values()]))
