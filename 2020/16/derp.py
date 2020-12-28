import re
from collections import defaultdict

file = open('input.txt', 'r')
data = file.readlines()

# format input data
rules = defaultdict(lambda: [])
rule_pattern = re.compile(r'(^.*): (\d*)-(\d*) or (\d*)-(\d*)$')
your_ticket_reached = False
nearby_tickets_reached = False
nearby_tickets = []

for line in [d for d in data if d.rstrip()]:
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
    nearby_tickets.append(ticket)


# End format data section

def get_ticket_scanning_error_rate(ticket_batch):
    invalid_values = []
    for t in ticket_batch:
        invalid_values.append(get_invalid_values_from_ticket(t))

    #format invalid values
    invalid_values = [x for y in invalid_values for x in y]
    print(sum(invalid_values))


# returns list of invalid values
def get_invalid_values_from_ticket(ticket):
    invalid_values = []
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
            invalid_values.append(target)
    return invalid_values


get_ticket_scanning_error_rate(nearby_tickets)

# print(rules, my_ticket, nearby_tickets)
