test = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

class Rotation:
    is_left: bool
    distance: int
    
    def __init__(self, rotation: str):
        self.is_left = True if rotation[0] == "L" else False
        self.distance = int(rotation[1:])

    def __repr__(self):
        return f"{"L" if self.is_left else "R"}{self.distance}"
    
class Safe:
    dial: int
    end_clicks: int
    clicks: int

    def __init__(self):
        self.dial = 50
        self.end_clicks = 0
        self.clicks = 0

    def turn(self, rotation: Rotation):
        for i in range(rotation.distance):
            if rotation.is_left:
                self.dial -= 1
            else:
                self.dial += 1
            
            self.dial = self.dial % 100

            if self.dial == 0:
                self.clicks += 1

        if self.dial == 0: 
            self.end_clicks += 1
            



def get_input():
    with open("input.txt") as f:
        return [Rotation(x) for x in f.readlines()]
    
def solution(rotations):
    safe = Safe()
    for rot in rotations:
        safe.turn(rot)
    print("part 1 solution:", safe.end_clicks)
    print("part 2 solution:", safe.clicks)

if __name__ == "__main__":
    test_rots = [Rotation(x) for x in test.split("\n")]
    print("test:")
    solution(test_rots)
    print("using input:")
    solution(get_input())
    
