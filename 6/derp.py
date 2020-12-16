# Using readlines()
file = open('input.txt', 'r')
lines = file.readlines()

all_groups = []
group = []
for i in lines:

    # if empty line, go to next group
    if i == '\n':
        # save previous group
        all_groups.append(group)
        # initialize empty next group
        group = []
        # continue

    # not empty, add to current group
    group.append(i.strip())

print(all_groups)

tallies = []
for grp in all_groups:
    yes_questions = {}
    for string in grp:
        for char in string:
            if char == '\n':
                continue
            yes_questions[char] = 1
    tallies.append(len(yes_questions))

print(tallies)

print(sum(tallies))
