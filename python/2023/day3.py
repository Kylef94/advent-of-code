from collections import deque

def get_input():
    data = []
    with open("input.txt", "r") as f:
        for l in f.readlines():
            data.append(l.strip())
    return data

def get_num(row, c):
    if row[c].isdigit():
        tmp = deque()
        tmp.append(row[c])
        l = c - 1
        r = c + 1
        
        while l >= 0 and row[l].isdigit():
            tmp.appendleft(row[l])
            l -= 1
        
        while r <= len(row) - 1 and row[r].isdigit():
            tmp.append(row[r])
            r += 1
        res = "".join(tmp)
        return int(res)
    return None

def search(data, r, c):
    res = []
    
    #search left
    if c > 0:
        num = get_num(data[r], c-1)
        if num: res.append(num)
    
    #search right
    if c < len(data[0]):
        num = get_num(data[r], c+1)
        if num: res.append(num)
        
    #search above
    if r > 0:
        num = get_num(data[r-1], c)
        if num: 
            res.append(num)
        else:
            if c > 0:
                num = get_num(data[r-1], c-1)
                if num: res.append(num)
            
            if c < len(data[0]):
                num = get_num(data[r-1], c+1)
                if num: res.append(num)
    
    #search below
    if r < len(data):
        num = get_num(data[r+1], c)
        if num: 
            res.append(num)
        else:
            if c > 0:
                num = get_num(data[r+1], c-1)
                if num: res.append(num)
            
            if c < len(data[0]):
                num = get_num(data[r+1], c+1)
                if num: res.append(num)
    return res
    
    
def part1(data):
    res = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            cur = data[r][c]
            if cur == '.' or cur.isdigit():
                continue
            else:
                res.extend(search(data, r, c))
    return sum(res)

def part2(data):
    res = []
    for r in range(len(data)):
        for c in range(len(data[0])):
            cur = data[r][c]
            
            if cur == "*":
                nums = search(data, r , c)

                if len(nums) > 1:
                    total = 1
                    for n in nums:
                        total *= n
                
                    res.append(total)
    return sum(res)

if __name__ == "__main__":
    data = get_input()
    print(part1(data))
    print(part2(data))