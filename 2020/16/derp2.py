import re
from collections import defaultdict

file = open('test2.txt', 'r')
data = file.readlines()

# format input data
rules = defaultdict(lambda: [])
rule_pattern = re.compile(r'(^.*): (\d*)-(\d*) or (\d*)-(\d*)$')
your_ticket_reached = False
nearby_tickets_reached = False
nearby_tickets = {}

for index, line in enumerate([d for d in data if d.rstrip()]):
    if line.rstrip() == 'your ticket:':
        your_ticket_reached = True
        continue
    if line.rstrip() == 'nearby tickets:':
        nearby_tickets_reached = True
        continue
    match = re.match(rule_pattern, line)
    if match:
        rules[match.group(1)].append((match.group(2), match.group(3)))
        rules[match.group(1)].append((match.group(4), match.group(5)))
        continue
    ticket = line.rstrip().replace(' ', '').split(',')
    if not nearby_tickets_reached:
        my_ticket = ticket
        continue
    nearby_tickets[index] = ticket


def is_ticket_valid(ticket) -> bool:
    for target in [int(t) for t in ticket]:
        target_valid = False
        for r in [rules[y] for y in rules]:
            if target_valid:
                break
            for r_set in r:
                min, max = r_set
                if int(min) <= target <= int(max):
                    target_valid = True
                    break
        if not target_valid:
            return False
    return True


# remove invalids
for i, t in [x for x in nearby_tickets.items()]:
    if not is_ticket_valid(t):
        print(f"deleting index {i} which is {nearby_tickets[i]}")
        del nearby_tickets[i]

# End format data section


# print(rules, my_ticket, nearby_tickets)

rule_positions = {}

values_by_position = [*zip(*nearby_tickets.values())]
possible_rules = {}
for rule in rules:
    possible_rules[rule] = defaultdict(lambda: 0)
num_of_tickets = len(nearby_tickets)

for i, x in enumerate(values_by_position):
    print(f"processing...")
    for v in x:
        for rule in rules:
            valid = False
            for rule_set in rules[rule]:
                min, max = rule_set
                if min <= v <= max:
                    valid = True
                    # break
            if valid:
                possible_rules[rule][i] += 1

print(possible_rules)
