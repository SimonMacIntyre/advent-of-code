import re

file = open('input', 'r')
data = file.readlines()


# 36 bit
def int_to_binary(value):
    return f"{int(value):036b}"


# 36 bit
def binary_to_int(value):
    # print(value)
    return int(str(value), 2)


def apply_mask_to_binary(mask, binary):
    new_binary = ''
    for i, bin in enumerate(binary):
        # print(i, bin)
        if mask[i] == 'X':
            new_binary += bin
            continue
        new_binary += mask[i]
    return new_binary


results = {}

for line in data:
    if re.match(r'mask =', line):
        mask = line[7:]
    else:
        pattern = re.match(r"mem\[(\d*)\] = (\d*)", line)  # mem[8] = 11
        memory = pattern.group(1)
        value = apply_mask_to_binary(mask, int_to_binary(pattern.group(2)))
        results[memory] = value

# print(results)
print(sum([binary_to_int(x) for x in results.values()]))