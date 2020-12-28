import copy
from collections import defaultdict

data = [6, 19, 0, 5, 7, 13, 1]
# test_data = [0, 3, 6]

spoken = copy.deepcopy(data)

# spoken = copy.deepcopy(test_data)

# format will look like spoken[number-spoken] = [2, 4, 6]. Elements being the index of the last time it was spoken.
spoken = defaultdict(lambda: [])

# initialize
for i, num in enumerate(data):
    spoken[num].append(i)
    last = num
loop = len(spoken)
# while loop <= 20:
# while loop < 2020:
while loop <= 30000000:
    if len(spoken[last]) > 1:
        next = spoken[last][-1] - spoken[last][-2]
        spoken[next].append(loop)
        last = next
    else:
        spoken[0].append(loop)
        last = 0
    loop += 1
    if loop % 1000000 == 0:
        print(last)

print(last)
# TOO SLOW
# def find_index_of_nth_most_recent_occurrence(n, value):
#     # for example n = 1, is the first most recent occurence, recent meaning, from end of array searching towards start
#     return int([index for index, number in enumerate(spoken) if number == value][-n:][0])
# loop = len(spoken)
# while loop < 2020:
# while loop < 10000:
# while loop < 30000000:
#     last_spoken = spoken[-1:][0]
#     occurs_count = spoken.count(last_spoken)
#     if occurs_count > 1:
#         most_recent_index = find_index_of_nth_most_recent_occurrence(1, last_spoken)
#         next_most_recent_index = find_index_of_nth_most_recent_occurrence(2, last_spoken)
#         next_number = most_recent_index - next_most_recent_index
#         spoken.append(next_number)
#     else:
#         spoken.append(0)
#     if loop % 100000 == 0:
#         print(loop, next_number)
#     loop += 1
# print(spoken[-1:][0])
