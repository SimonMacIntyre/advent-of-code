import re
import copy

# Format the input data into nice rows and columns of characters
file = open('input.txt', 'r')
data = enumerate(file.readlines())
formatted_data = {}
for row_index, string in data:
    # \S = non-whitespace-character. So basically, split the input line into each individual character
    # While we are at it, remove the trailing \n and any empty whitespace
    formatted_data[row_index] = [x for x in re.split(r"(\S)", string.strip()) if x != '']


def process_seat(char, row_index, col_index, seat_map):
    # Seat is floor, seat doesn't change
    if char == '.':
        return ['.', False]

    # Seat is empty
    if char == 'L':
        count = get_adjacent_occupied_seat_count(row_index, col_index, seat_map)
        if count == 0:
            return ['#', True]
        else:
            return ['L', False]

    # Seat is occupied
    if char == '#':
        count = get_adjacent_occupied_seat_count(row_index, col_index, seat_map)
        if count >= 4:
            return ['L', True]
        else:
            return ['#', False]


def get_adjacent_occupied_seat_count(row_index, col_index, seat_map):
    count = 0
    for x in range(row_index - 1, row_index + 2):  # if checking row 3 col 3: makes row range of 2,3,4
        for y in range(col_index - 1, col_index + 2):  # if checking row 3 col 3: makes col range of 2,3,4
            if x == row_index and y == col_index:  # ignore current seat being processed
                continue
            if (x < 0 or y < 0) or (x >= len(seat_map) or y >= len(seat_map[x])):  # ignore values outside the ranges
                continue
            if seat_map[x][y] == '#':  # if the seat is occupied, add it to the count of adjacent occupied seats
                count += 1
    return count


# deep copy is necessary, otherwise python assigns by reference instead of value (that is D U M B)
# initialize seat maps before while loop
current_seat_map = copy.deepcopy(formatted_data)
next_seat_map = copy.deepcopy(formatted_data)

while True:
    # One loop = every seat was checked for changes, according to the current seat map
    # state changes keeps records of all the changes, so if there is ever a loop with no changes at all
    # we stop because we have reached equilibrium
    state_changes = []
    current_seat_map = copy.deepcopy(next_seat_map)

    # loop through seat by seat
    for row_index in current_seat_map:
        for col_index, char in enumerate(current_seat_map[row_index]):
            # new_char is the updated seat value, even if it remains the same we capture it and store it as if its new
            # it is the 'next iterations' state of that seat
            # single_state_change is just a boolean capturing if the seat actually changed states, so we can check for
            # equilibrium later
            new_char, single_state_change = process_seat(char, row_index, col_index, current_seat_map)
            next_seat_map[row_index][col_index] = new_char  # assign the new seat state for next iteration
            state_changes.append(single_state_change)  # capture whether or not state changed

    # At the end of the iteration, if there is not a single True in state_changes, we have reached equilibrium
    if True not in state_changes:
        break

# Now that we have reached equilibrium, how many seats are occupied?
occupied_seats = 0
for row in next_seat_map:
    for char in next_seat_map[row]:
        if char == '#':
            occupied_seats += 1

print(occupied_seats)


# part 2
# All of the functionality is the exact same as part 1, except for the function to count seats
# now counts seats in line of sight instead of just adjacent, and the threshold for leaving a seat is 5 instead of 4

def process_seat_part2(char, row_index, col_index, seat_map):
    if char == '.':
        return ['.', False]
    if char == 'L':
        count = get_occupied_seats_in_view_count(row_index, col_index, seat_map)
        if count == 0:
            return ['#', True]
        else:
            return ['L', False]
    if char == '#':
        count = get_occupied_seats_in_view_count(row_index, col_index, seat_map)
        if count >= 5:
            return ['L', True]
        else:
            return ['#', False]


# These are the 8 lines of sight.
# The idea is each time a seat is checked, we check each line of sight (algo), seat by seat
# outwards from the seat being processed.
# For example x-1 y-1 is the top-left diagonal line of sight. So if we were checking seat [5][5], it would check:
# [4][4] (this is x-1, y-1, so 5-1, 5-1). If it finds a seat (L or #) it either counts it or breaks (doesn't count it)
# Then goes to the next line of sight.
# After each algo is checked, we have the combined count of occupied seats across each line of sight
algos = [
    {'x': -1, 'y': -1},
    {'x': -1, 'y': 0},
    {'x': -1, 'y': 1},
    {'x': 0, 'y': -1},
    {'x': 0, 'y': 1},
    {'x': 1, 'y': -1},
    {'x': 1, 'y': 0},
    {'x': 1, 'y': 1},
]


def get_occupied_seats_in_view_count(row_index, col_index, seat_map):
    count = 0
    for algo in algos:

        # At the start of each algo(line of sight), get the next seat in line of sight to process
        x = row_index + algo['x']
        y = col_index + algo['y']

        while True:
            # ignore seats that do not exist at all (e.g., [-1][-1]), go to next line of sight
            if x not in seat_map:
                break

            # ignore seats that do not exist at all (e.g., [-1][-1]), go to next line of sight
            if y < 0 or y >= len(seat_map[x]):
                break

            # A seat is found. Process it, and break(move to next line of sight)
            if seat_map[x][y] == '#':
                count += 1
                break

            # A seat is found. Process it, and break(move to next line of sight)
            if seat_map[x][y] == 'L':
                break

            # We did not break, so a seat was not found yet. Go to next seat in line of sight.
            x += algo['x']
            y += algo['y']

    # All algos were checked and we have the finished count.
    return count


current_seat_map = formatted_data
next_seat_map = formatted_data
while True:
    state_changes = []
    current_seat_map = copy.deepcopy(next_seat_map)
    for row_index in current_seat_map:
        for col_index, char in enumerate(current_seat_map[row_index]):
            new_char, single_state_change = process_seat_part2(char, row_index, col_index, current_seat_map)
            next_seat_map[row_index][col_index] = new_char
            state_changes.append(single_state_change)
    if True not in state_changes:
        break

occupied_seats = 0
for row in next_seat_map:
    for char in next_seat_map[row]:
        if char == '#':
            occupied_seats += 1

print(occupied_seats)
