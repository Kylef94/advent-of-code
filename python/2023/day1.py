def get_input():
    data = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def get_digits(line):
    num = ""
    chars = list(line)
    
    for c in chars:
        if c.isdigit():
            num += c
            break
    
    for c in chars[::-1]:
        if c.isdigit():
            num += c
            break
            
    return int(num)

def part1(data):
    return sum([get_digits(line) for line in data])

def to_digits(num):
    if len(num) == 2:
        return int(num)
    else:
        digits = num[0] + num[-1]
        return int(digits)
    
def convert(line):
    res = ""
    for i, c in enumerate(line):
        
        if c.isdigit():
            res += c
            continue
            
        match c:
            case "o":
                if (i + 3 <= len(line)) and line[i:i+3] == "one":
                    res += "1" 
            
            case "e":
                if (i + 5 <= len(line)) and line[i:i+5] == "eight":
                    res += "8" 
            
            case "n":
                if (i + 4 <= len(line)) and line[i:i+4] == "nine":
                    res += "9"
                
            case "t":
                if (i + 5 <= len(line)) and line[i:i+5] == "three":
                    res += "3"
                
                elif (i + 3 <= len(line)) and line[i:i+3] == "two":
                    res += "2" 
                    
            case "f":
                if (i + 4 <= len(line)) and line[i:i+4] == "four":
                    res += "4"
                
                if (i + 4 <= len(line)) and line[i:i+4] == "five":
                    res += "5"
            
            case "s":
                if (i + 3 <= len(line)) and line[i:i+3] == "six":
                    res += "6"
                
                if (i + 5 <= len(line)) and line[i:i+5] == "seven":
                    res += "7"
    return res

def part2(data):
    return sum([to_digits(convert(x)) for x in data])

if __name__ == "__main__":
    data = get_input()
    print(part1(data))
    print(part2(data))