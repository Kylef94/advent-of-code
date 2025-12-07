test = """987654321111111
811111111111119
234234234234278
818181911112111"""

def get_input():
    with open("input.txt") as f:
        return [line for line in f.readlines()]
def part1(battery_banks):
    total = 0
    for bank in battery_banks:
        print(bank)
        seen = set()
        joltage = 0
        for i in range(len(bank) - 1):
            battery = bank[i]
            if battery in seen: 
                continue
            battery2 = max(bank[i+1:])
            joltage = max(joltage, int(battery + battery2))
            seen.add(battery)
        total += joltage
    return total


if __name__ == "__main__":
    t = test.split("\n")
    print("part 1 test:", part1(t))
    # print("part 2 test:", part2(t))
    print("part 1 solution:", part1(get_input()))
    # print("part 2 solution:", part2(get_input()))
    # t2 = ["1001001-1010101"]
    # print("part2 t2:", part2(t2))
