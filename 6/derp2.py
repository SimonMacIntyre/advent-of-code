# Using readlines()
# file = open('testinput.txt', 'r')
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
    print(i)
    group.append(i.strip())

print(all_groups)


def intersecting_chars(group):
    yes_questions = {}

    for string in group:
        for char in string:
            if char in yes_questions:
                continue
            char_in_all = True
            for string2 in group:
                if char not in string2:
                    char_in_all = False
                    break
            if char_in_all:
                yes_questions[char] = 1
    return len(yes_questions)


tallies = []
for grp in all_groups:
    if grp[0] == "":
        del grp[0]
    tallies.append(intersecting_chars(grp))

print(sum(tallies))
