test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def get_input():
    with open("input.txt") as f:
        return [line for line in f.readlines()]
    
def can_access(grid, r: int, c: int):
    neighbours = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    rolls = 0
    for r_inc, c_inc in neighbours:
        row = r + r_inc
        col = c + c_inc
        if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
            try:
                if grid[row][col] == "@":
                    rolls += 1
            except IndexError:
                print("index error at row, col:", row, col)
                print("r, c:", r, c)
                print("incs:", r_inc, c_inc)
    return rolls < 4

def part1(grid):
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "@" and can_access(grid, r, c):
                total += 1
    return total

def clean_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "@" and can_access(grid, r, c):
                grid[r][c] = "x"
                total += 1
    return grid, total

def part2(grid):
    total = 0
    changed = True
    while changed:
        removed = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "@" and can_access(grid, r, c):
                    grid[r] = grid[r][:c] + "x" + grid[r][c+1:]
                    removed += 1
        total += removed
        if removed == 0:
            changed = False
    return total

if __name__ == "__main__":
    t = test.split("\n")
    print("part 1 test:", part1(t))
    print("part 2 test:", part2(t))
    print("part 1 solution:", part1(get_input()))
    print("part 2 solution:", part2(get_input()))