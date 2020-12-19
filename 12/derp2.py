import re
import math

file = open('input', 'r')
data = file.readlines()

formatted_data = [re.findall(r"\D|\d*", x.strip()) for x in data]

# Delete trailing whitespace.... annoying
for x in formatted_data:
    del x[2]

pos_x = 0
pos_y = 0
facing = 180
waypoint_relative = [10, 1]


def l(val):
    while val:
        waypoint_relative[0], waypoint_relative[1] = -waypoint_relative[1], waypoint_relative[0]
        val -= 90


def r(val):
    while val:
        waypoint_relative[0], waypoint_relative[1] = waypoint_relative[1], -waypoint_relative[0]
        val -= 90


def f(val):
    global pos_x, pos_y
    pos_x += waypoint_relative[0] * val
    pos_y += waypoint_relative[1] * val


def n(val):
    global waypoint_relative
    waypoint_relative[1] += val


def s(val):
    global waypoint_relative
    waypoint_relative[1] -= val


def e(val):
    global waypoint_relative
    waypoint_relative[0] += val


def w(val):
    global waypoint_relative
    waypoint_relative[0] -= val


for i in formatted_data:
    func_name = str(i[0]).lower()
    eval(func_name + "(" + i[1] + ")")

print(pos_x, pos_y, abs(pos_x) + abs(pos_y))
