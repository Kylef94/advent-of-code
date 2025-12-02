from itertools import permutations

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def generate_operator_sets(length: int, ops: list, res: list, part2: bool) -> list:
    if len(ops) == length:
        res.append(ops)
        return
    
    operators = [["+"], ["*"]]
    if part2: 
        operators.append(["||"])

    for op in operators:
        generate_operator_sets(length, ops.copy() + op, res, part2)

    return res

def concatenate(num1, num2):
    return int(str(num1) + str(num2))

def evaluate(nums: list, ops: list):
    total = nums[0]
    cur = 1
    for op in ops:
        match op:
            case "+":
                total += nums[cur]
            case "*":
                total *= nums[cur]
            case "||":
                total = concatenate(total, nums[cur])
        cur += 1
    return total

def parse_input(text: str):
    res = []
    lines = text.split("\n")
    for l in lines:
        expected, digits = l.split(":")
        digits = digits.strip()
        res.append((int(expected), [int(x) for x in digits.split(" ")]))
    return res

def get_input():
    with open("input.txt") as f:
        return parse_input(f.read())
    
def part1(data):
    res = 0
    for d in data:
        expected, digits = d
        combos = generate_operator_sets(len(digits) - 1, [], [], False)
        for combo in combos:
            if evaluate(digits, combo) == expected:
                res += expected
                break
    return res

def part2(data):
    res = 0
    for d in data:
        expected, digits = d
        combos = generate_operator_sets(len(digits) - 1, [], [], True)
        for combo in combos:
            if evaluate(digits, combo) == expected:
                res += expected
                break
    return res

if __name__ == "__main__":
    # t = parse_input(test)
    # print("test part1:", part1(t))
    # print("test part2:", part2(t))
    print("part1:", part1(get_input()))
    print("part2:", part2(get_input()))
    
    
    
        