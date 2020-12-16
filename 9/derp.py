file = open('input', 'r')
numbers = file.readlines()

preamble = 25


def number_is_valid(index: int, num: int, preamble: int) -> bool:
    if (index + 1) <= preamble:
        return True
    valid = False
    for outer_index, outer_num in enumerate(numbers[index - preamble:index]):
        for inner_index, inner_num in enumerate(numbers[index - preamble:index]):
            if outer_num != inner_num and int(outer_num) + int(inner_num) == int(num):
                valid = True
    return valid


# part 1
for index, num in enumerate(numbers):
    if not number_is_valid(index, num, preamble):
        print(num)
        invalid_num = num

# part 2
search_size = 2
while True:
    for index, num in enumerate(numbers):
        doctored_list = [x.strip() for x in numbers[index:index + search_size]]
        doctored_list = [int(x) for x in doctored_list]
        if sum(doctored_list) == int(invalid_num):
            print(f"{min(doctored_list) + max(doctored_list)}")
            exit()
    search_size += 1
