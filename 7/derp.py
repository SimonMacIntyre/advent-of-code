import re as regex

file = open('input', 'r')
lines = file.readlines()

master_rules = {}


def get_parent_from_line(line: str):
    parent = regex.compile(r'(\S*\s\S*)\sbags contain').match(line)[1]
    return parent


def get_children_from_line(line: str):
    children = regex.findall(r'(\d*)\s(\S*\s\S*) bags?[,|.]', line)
    return children


def check_if_contains_no_bags(line: str) -> bool:
    return bool(regex.findall(r'no other bags', line))


def process_rule(line: str):
    global master_rules
    parent = get_parent_from_line(line)
    children = get_children_from_line(line)

    # Add new rules to master rules dictionary
    for count, bag in children:
        if parent not in master_rules:
            master_rules[parent] = {}
        master_rules[parent].update({bag: int(count)})


for rule_string in lines:
    if check_if_contains_no_bags(rule_string):
        continue
    process_rule(rule_string)


def bag_can_contain_bag(bag: str, can_contain_bag: str) -> bool:
    if bag not in master_rules:
        return False
    for inner_bag in master_rules[bag]:
        if bag_can_contain_bag(inner_bag, can_contain_bag):
            return True
    return can_contain_bag in master_rules[bag]


count = 0
for bag in master_rules:
    if bag_can_contain_bag(bag, 'shiny gold'):
        count += 1

# print(master_rules)
print(f"{count} bags can contain 'shiny gold' bag")


# Part 2
def bag_holds_this_many_bags(bag: str) -> int:
    count = 0
    if bag not in master_rules:
        return 0
    for inner_bag in master_rules[bag]:
        count += master_rules[bag][inner_bag]
        count += (bag_holds_this_many_bags(inner_bag)) * master_rules[bag][inner_bag]
    return count


print(f"'shiny gold' bag holds {bag_holds_this_many_bags('shiny gold')} bags")
