file = open('input', 'r')
data = file.readlines()

# format the data
data = sorted([int(x) for x in data])
data.insert(0, 0)
data.append(data[-1] + 3)

# part 1
difference_counts = {}

for index, jolt_rating in enumerate(data):
    if index == len(data) - 1:
        break
    difference = data[index + 1] - jolt_rating
    if difference not in difference_counts:
        difference_counts[difference] = 1
    else:
        difference_counts[difference] += 1

print(difference_counts[1] * difference_counts[3])

# part 2

# stolen solution using tribonacci random shit
tribonacciSequence = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149]


def fuck_you(num):
    if num > len(tribonacciSequence):
        print('poop')
        exit()
    return tribonacciSequence[num - 1]


multiplier = 1
currentRun = 1
for joltage in data:
    if joltage + 1 in data:
        currentRun += 1
    else:
        multiplier *= fuck_you(currentRun)
        currentRun = 1

print(multiplier)

# simons solution

# build a tree
tree = {}

# Builds a tree of nodes and their children nodes, looks like:
# [parent_node] = [children_nodes...]
# [A] = [B]
# [B] = [C, D, E]
# [C] = [D, E]

for index, jolt_rating in enumerate(data):
    if index == len(data) - 1:
        break
    tree[index] = []
    for i in range(1, 4):
        if index + i >= len(data):
            continue
        difference = data[index + i] - jolt_rating
        if 1 <= difference <= 3:
            tree[index].append(index + i)

memo = {}


def compute_paths(node_index):
    global memo
    count = 0
    if node_index not in tree:  # this is a leaf on the tree (the end of the path)
        memo[node_index] = 0
        return 0

    # if B has children C,D,E - then B has 3 paths. But only 2 of them are 'new', because node B already
    # is part of 1 path, from presumably its parent node A. A -> B -> (C,D,E) = 3 total paths.
    # if you just count A -> B, its 1 path. If you add B children C,D,E you would end with 4 paths but there are only 3.
    # have to account for the current path (e.g., A -> B).
    # So each nodes NEW paths count is actually = ((number of children) - 1) + childrens_counts
    count = len(tree[node_index]) - 1
    for child_node_index in tree[node_index]:
        count += memo[child_node_index]  # count this nodes children's nodes counts


    memo[node_index] = count

    return count


# loop backwards through the data from the bottom to the top
for index in range(len(data) - 1, -1, -1):
    # each iteration counts the number of paths from that parent node (index) to the last node
    compute_paths(index)

print(memo[0] + 1)
