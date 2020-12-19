import re
import math

file = open('input', 'r')
data = file.readlines()

# formatted_data = list(filter('', [re.split(r"(\D)(\d*)", x.strip()) for x in data]))

formatted_data = [re.findall(r"\D|\d*", x.strip()) for x in data]

# Delete trailing whitespace.... annoying
for x in formatted_data:
    del x[2]

pos_x = 0
pos_y = 0
facing = 180


def get_facing_from_decimal(dec):
    if dec == .25 or dec == -.75:
        return 90
    if dec == .5 or dec == -.5:
        return 180
    if dec == .75 or dec == -.25:
        return 270
    if dec == 0:
        return 0


def get_direction_from_facing(degree):
    if degree == 0:
        return 'w'
    if degree == 90:
        return 'n'
    if degree == 180:
        return 'e'
    if degree == 270:
        return 's'


def l(val):
    global facing
    x = math.modf((facing - val) / 360)[0]
    facing = get_facing_from_decimal(x)


def r(val):
    global facing
    x = math.modf((facing + val) / 360)[0]
    facing = get_facing_from_decimal(x)


def f(val):
    dir = get_direction_from_facing(facing)
    eval(dir + "(" + str(val) + ")")


def n(val):
    global pos_y
    pos_y += val


def s(val):
    global pos_y
    pos_y -= val


def e(val):
    global pos_x
    pos_x += val


def w(val):
    global pos_x
    pos_x -= val


for i in formatted_data:
    func_name = str(i[0]).lower()
    eval(func_name + "(" + i[1] + ")")

print(pos_x, pos_y, abs(pos_x) + abs(pos_y))
