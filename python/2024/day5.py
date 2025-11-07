test = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def parse_input():
    with open("input.txt") as f:
        text = f.read()
        return parse(text)
    
def parse(text):
    updates = []
    rulesdict = {}
    for line in text.split("\n"):
        if "|" in line:
            before, after = line.split("|")
            before, after = int(before), int(after)

            if before not in rulesdict:
                rulesdict[before] = {after}
            else:
                rulesdict[before].add(after)

        if "," in line:
            updates.append([int(x) for x in line.split(",")])

    return rulesdict, updates

def sort_pages(page_a, page_b, rules):
    if page_a == page_b:
        return 0
    
    elif page_a in rules and page_b in rules[page_a]:
        return 1
    
    elif page_b in rules and page_a in rules[page_b]:
        return -1

def check_update(update, rules):
    for i in range(len(update) - 1):
        if sort_pages(update[i], update[i+1], rules) == -1:
            return 0
    return update[len(update) // 2]
    
def part1(rules, updates):
    res = 0
    for update in updates:
        res += check_update(update, rules)
    return res
    
assert part1(*parse(test)) == 143

def correct_update(upd, rules):
    update = upd.copy()
    correct = False
    while not correct:
        correct = True
        for i in range(len(update) - 1):
            if sort_pages(update[i], update[i+1], rules) == -1:
                update[i], update[i+1] = update[i+1], update[i]
                correct = False
    return update[len(update) // 2]

def part2(rules, updates):
    res = 0
    for update in updates:
        if check_update(update, rules) == 0:
            res += correct_update(update, rules)
    return res

assert part2(*parse(test)) == 123

def main():
    rules, updates = parse_input()
    print("part 1:", part1(rules, updates))
    print("part 2:", part2(rules, updates))

if __name__ == "__main__":
    main()