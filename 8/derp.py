file = open('input', 'r')
lines = file.readlines()

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


current_index = 0
while current_index <= len(lines) - 1:
    if index_was_already_called(current_index):
        print(f"infinite loop detected. Accumulator value: {accumulator}")
        exit()
    operation, arg = lines[current_index].split()
    next_index_mod = eval(operation + "(int(" + arg + "))")  # e.g., acc(arg), jmp(arg)
    current_index += next_index_mod
