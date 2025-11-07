MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

def get_input():
    data = []

    with open("input.txt", "r") as f:
        for line in f.readlines():
            data.append(line.strip())

    for i, d in enumerate(data):
        new_d = d.split(": ")
        data[i] = new_d[1].split("; ")
    
    return data

class Draw():

    def __init__(self, r=0, g=0, b=0) :
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)
    
    def is_valid(self):
        return self.r <= MAX_RED and self.g <= MAX_GREEN and self.b <= MAX_BLUE
    
    def __str__(self):
        return f"Draw: r = {self.r}; g = {self.g}; b = {self.b}; valid = {self.is_valid()}"

class Game():
    
    def __init__(self, game=[]):
        self.draws = []
        
        for g in game:
            self.draws.append(g)
    
    def __str__(self):
        s = "Game: "
        for d in self.draws:
            s += f"\n {str(d)}"
        
        s += f"\nvalid game: {self.valid_game()}"
        return s

    def add(self, draw):
        self.draws.append(draw)
    
    def valid_game(self):
        return min([d.is_valid() for d in self.draws])
    
def parse(t):
    res = Game()
    
    for s in t:
        inp = s.split(", ")
        r = 0
        g= 0
        b = 0
        
        for i in inp:
            amt, col = i.split(" ")
            
            match col:
                case "red":
                    r = amt
                    
                case "blue":
                    b = amt
                
                case "green":
                    g= amt
        res.add(Draw(r, g ,b))
    return res

def part1(data):
    res = 0
    games = [parse(x) for x in data]
    for i, g in enumerate(games):
        if g.valid_game():
            res += i + 1

    return res

def part2(data):
    games = [parse(x) for x in data]
    res = sum([g.get_power() for g in games])
    return res

if __name__ == "__main__":
    data = get_input()
    print(part1(data))
    print(part2(data))