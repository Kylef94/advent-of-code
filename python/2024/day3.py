from typing import List
import re

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def input():
    with open("input.txt", "r") as f:
        data = f.read()
    return data

def search(text):
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    return re.findall(regex, text)

def part1(data: str):
    muls_list = search(data)
    res = 0
    for d in muls_list:
        cur = d.replace("mul(", "").replace(")", "").split(",")
        res += int(cur[0]) * int(cur[1])
    return res

assert part1(test) == 161

#part 2
def search2(text: str):
    regex = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    return re.findall(regex, text)

def part2(data: str):
    ops_list = search2(data)
    res = 0
    do = True
    for op in ops_list:
        match op:
            case "don't()": 
                do = False
            case "do()": 
                do = True
            case _:
                if do:
                    cur = op.replace("mul(", "").replace(")", "").split(",")
                    res += int(cur[0]) * int(cur[1])
    return res

assert part2(test2) == 48

def main():
    data = input()
    #tests
    print(part1(test))
    print(part2(test2))

    #get solutions
    print("part 1 answer:", part1(data))
    print("part 2 answer:", part2(data))

if __name__ == "__main__":
    main()

