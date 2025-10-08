from typing import List


def input():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            nums = [int(x) for x in line.strip().split(" ") if x != '']
            data.append(nums)
    return data

def check_safe(report: List):
    all_decreasing = True
    all_increasing = True
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if diff > 0:
            all_decreasing = False
        else:
            all_increasing = False
        absdiff = abs(diff)
        if absdiff > 3 or absdiff == 0:
            return False
    return all_increasing or all_decreasing

def part1(data: List):
    return sum([check_safe(report) for report in data])

def check_safe_with_removal(report: List):
    if check_safe(report): 
        return True

    for i in range(len(report)):
        removed = report.pop(i)
        if check_safe(report):
            return True
        report.insert(i, removed)
    return False

def part2(data: List):
    return sum([check_safe_with_removal(report) for report in data])

def main():
    data = input()
    # check input parsed correctly
    #print(data[:5])
   
    #get solutions
    print("part 1 answer:", part1(data))
    print("part 2 answer:", part2(data))

if __name__ == "__main__":
    main()

