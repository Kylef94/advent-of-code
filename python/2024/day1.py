from collections import Counter

def input():
    left = []
    right = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data = line.strip().split(" ")
            l, r = data[0], data[-1]
            left.append(int(l))
            right.append(int(r))
    
    return sorted(left),sorted(right)

def part1(left, right):
    sum = 0
    for i in range(len(left)):
        diff = left[i] - right[i]
        if diff < 0: diff *= -1
        sum += diff
    return sum

def part2(left, right):
    counts = Counter(right)
    sum = 0
    for num in left:
        sum += num * counts[num]
    return sum

def main():
    left, right = input()
    # check input parsed correctly
    print(left[:5])
    print(right[:5])    
    #get solutions
    print("part 1 answer:", part1(left, right))
    print("part 2 answer:", part2(left, right))

if __name__ == "__main__":
    main()

