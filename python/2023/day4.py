def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            l = l.split(':')
            data.append(l[1].strip())
    return data

def part1(data):
    res = 0
    for card in data:
        card = card.split("|")

        lnums = set([x for x in card[0].split(" ") if x != ''])
        rnums = set([x for x in card[1].split(" ") if x != ''])
        wins = lnums & rnums
        
        if wins:
            if len(wins) == 1:
                res += 1
            else: 
                res += pow(2, len(wins) - 1)
    return res

def part2(data):
    copies = [1] * len(data)
    
    for c, card in enumerate(data):
        card = card.split("|")
        lnums = set([x for x in card[0].split(" ") if x != ''])
        rnums = set([x for x in card[1].split(" ") if x != ''])
        wins = lnums & rnums
        
        if wins:
            for i in range(c + 1, c + len(wins) + 1):
                copies[i] += 1 * copies[c]
                
    return sum(copies)

if __name__ == "__main__":
    data = get_input()
    print(part1(data))
    print(part2(data))