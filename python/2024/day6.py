from ast import List


test = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''

class Map:
    grid: List
    rows: int
    cols: int
    start_pos: tuple[int]

    def __init__(self, map: str):
        self.grid = []
        for i, row in enumerate(map.split("\n")):
            if "^" in row:
                self.start_pos = (i, row.find("^"))
            self.grid.append(list(row))

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        print("map created with start pos", self.start_pos)
        print("rows:", self.rows, "cols:", self.cols)
    
    def get(self, row: int, col: int):
        return self.grid[row][col]
    
    def put(self, char: str, row: int, col: int):
        self.grid[row][col] = char

class Guard:
    position_row: int
    position_col: int
    visited: set
    direction: int
    moves: List
    map: Map

    def __init__(self, map: Map):
        self.map = map
        self.position_row, self.position_col = map.start_pos
        self.direction = 0
        self.moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.visited = {map.start_pos}

    def move(self):
        rows, cols = self.map.rows, self.map.cols
        row_inc, col_inc = self.moves[self.direction]
        row, col = self.position_row + row_inc, self.position_col + col_inc
        if 0 > row or row >= rows or 0 > col or col >= cols:
            self.position_row, self.position_col = row, col
            return
        if self.map.get(row, col) == "#":
            self.turn()
        else:
            self.visited.add((row, col))
            self.position_row, self.position_col = row, col
    
    def turn(self):
        self.direction += 1
        if self.direction >= len(self.moves):
            self.direction = 0

    def find_exit(self):
        rows, cols = self.map.rows, self.map.cols
        while 0 <= self.position_row < rows and 0 <= self.position_col < cols:
            self.move()
        return len(self.visited) 

def parse_input():
    with open("input.txt") as f:
        map = f.read()
    return Map(map)

def main():
    map = parse_input()
    guard = Guard(map)
    print("part 1:", guard.find_exit())
    #print("part 2:", part2(data))

if __name__ == "__main__":
    main()