from math import ceil, floor, sqrt


def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.strip()
            tmp = []
            for s in l.split(" "):
                if s.isdigit():
                    tmp.append(int(s))
            data.append(tmp)
    return list(zip(data[0], data[1]))


def get_wins(race):
    #solving using quadratic formula where quadratic is -x^2 + time*x - dist
    a = -1
    time = race[0] #b
    dist = race[1] * -1 #c
    
    negb = time * -1
    disc = sqrt(time*time - 4*a*dist)
    denom = 2 * a
    
    root1 = (negb + disc) / denom
    root2 = (negb - disc) / denom
    #return round(root1), round(root2)
    return ceil(root2) - floor(root1) - 1 
    

def part1(data):
    res = []
    total = 1
    for d in data:
        res.append(get_wins(d))
    
    for r in res:
        total *= r
    return total

def part2(data):
    res = []
    total = 1
    for d in data:
        res.append(get_wins(d))
    
    for r in res:
        total *= r
    return total

if __name__ == "__main__":
    data = get_input()
    print(data)
    print(part1(data))
    print(part2(data))