file = open('input', 'r')
lines = file.readlines()

# format input
data = []
for line in lines:
    operation, arg = line.split()
    data.append({operation: arg})

accumulator = 0


def acc(arg: int) -> int:
    global accumulator
    accumulator += arg
    return 1


def jmp(arg: int) -> int:
    return arg


def nop(arg: int) -> int:
    return 1


called_indexes = []


def index_was_already_called(index: int) -> bool:
    global called_indexes
    if index in called_indexes:
        return True
    called_indexes.append(index)
    return False


# indexes who have had their original jmp or nop swapped to the other
swapped_indexes = []


def index_was_already_swapped(index: int) -> bool:
    global swapped_indexes
    if index in swapped_indexes:
        return True
    swapped_indexes.append(index)
    return False


current_index = 0
swapped_once = False


def reset():
    global accumulator, current_index, swapped_once, called_indexes
    accumulator = 0
    current_index = 0
    swapped_once = False
    called_indexes = []


while current_index != len(data):
    if index_was_already_called(current_index):
        reset()
        continue
    operation = list(data[current_index].keys())[0]
    arg = data[current_index][operation]
    if operation == 'jmp' and not swapped_once:
        if not index_was_already_swapped(current_index):
            operation = 'nop'
            swapped_once = True
    if operation == 'nop' and not swapped_once:
        if not index_was_already_swapped(current_index):
            operation = 'jmp'
            swapped_once = True
    next_index_mod = eval(operation + "(int(" + arg + "))")  # e.g., acc(arg), jmp(arg)
    current_index += next_index_mod

print(accumulator)
