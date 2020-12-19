import re
import math
from datetime import datetime
import numpy

file = open('test', 'r')
data = file.readlines()

minimum = int(data[0].rstrip())

bus_ids = re.findall(r"(\d*)", data[1])
bus_ids = filter(lambda x: x != '', bus_ids)

bus_closest_times = {}
for i in bus_ids:
    bus_closest_times[i] = (math.ceil(minimum / int(i)) * int(i)) - minimum

sorted_closest_times = sorted(bus_closest_times.items(), key=lambda item: item[1])

print(int(sorted_closest_times[0][0]) * int(sorted_closest_times[0][1]))

# part 2
file = open('input', 'r')
data = file.readlines()

bus_ids = re.findall(r"(\d*|x)", data[1])
bus_ids = filter(lambda x: x != '', bus_ids)

bus_ids = [x for x in bus_ids]

# startTime = datetime.now()

t = 0

t = 99999999999984  # only start at this value for the real `input` file

jump = int(bus_ids[:1][0])  # Start by jumping by the first bus id every loop
start_at_index = 1  # this is the current index we are looking for a match on
matched_ids = [int(bus_ids[:1][0])]  # these are the ids we multiply together to figure out how far to jump
while True:
    for index, bus_id in enumerate(bus_ids):  # for each time, search each bus for the required match
        if bus_id == 'x' or index < start_at_index:  # ignore x, and indexes less than start_at_index have been matched
            continue
        if (t + index) % int(bus_id) == 0:  # A match is found
            escape = True
            # jump forward to the next time that these matches occur in sequence, to start searching for the next match
            jump = (int(bus_id) * numpy.prod(matched_ids))
            matched_ids.append(int(bus_id))  # add this found index to the matched list
            start_at_index = index + 1  # don't search through this bus_id anymore

        else:
            escape = False
            break
    if escape:
        print(t)
        break
    t += jump

# print(datetime.now() - startTime)

# TOO SLOW

# startTime = datetime.now()
#
# @lru_cache(None)
# def get_time_from_bus_id_and_loop(bus_id, loop):
#     return int(bus_id) * int(loop)
#
# time_loop = 1
# while True:
#     # print(f"Iteration {time_loop} ... ")
#     magic_number = True
#     target = get_time_from_bus_id_and_loop(bus_ids[0], time_loop)
#     bus_loop = 1
#     for bus_id in bus_ids[1:]:
#         if bus_id == 'x':
#             bus_loop += 1
#             continue
#         bus_target = target + bus_loop
#         i = 1
#         while get_time_from_bus_id_and_loop(bus_id, i) <= bus_target:
#             i += 1
#         if get_time_from_bus_id_and_loop(bus_id, i - 1) == bus_target:
#             # this bus is a match, just continue to next bus
#             bus_loop += 1
#             continue
#         else:
#             # this bus didn't meet the target
#             # print(f"{target} not a match")
#             magic_number = False
#             break
#     if magic_number:
#         print(target)
#         break
#     time_loop += 1
#
#
# print(datetime.now() - startTime)
