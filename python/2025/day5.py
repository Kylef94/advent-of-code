test = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def get_input():
    with open("input.txt") as f:
        return parse_input([line.strip("\n") for line in f.readlines()])
    
def parse_input(data):
    ind = data.index("")
    ranges = data[:ind]
    ids = [int(x) for x in data[ind + 1:]]
    ranges = [x.split("-") for x in ranges]
    ranges = [(int(y[0]), int(y[1])) for y in ranges]
    return ranges, ids

def part1(intervals, ids):
    total = 0
    for id in ids:
        for low, high in intervals:
            if low <= id <= high:
                #print(f"{id} is fresh")
                total += 1
                break
    return total

def part2(intervals):
    total = 0
    seen = set()
    for low, high in intervals:
            for i in range(low, high + 1):
                if i not in seen:
                    total += 1 
                    seen.add(i)
    return total

if __name__ == "__main__":
    t_intervals, t_ids = parse_input(test.split("\n"))
    intervals, ids = get_input()
    print(t_intervals, t_ids)
    print("part 1 test:", part1(t_intervals, t_ids))
    print("part 2 test:", part2(t_intervals))
    print("part 1 solution:", part1(intervals, ids))
    print("part 2 solution:", part2(intervals))