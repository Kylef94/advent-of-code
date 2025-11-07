test = "MMMSXXMASM \
MSAMXMSMSA \
AMXSXMAAMM \
MSAMASMSMX \
XMASAMXAMM \
XXAMMXXAMA \
SMSMSASXSS \
SAXAMASAAA \
MAMMMXMMMM \
MXMXAXMASX"

# (row, col)
SEARCH_DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
SEARCH_STRING = "XMAS"

def parse_input():
    res = []
    with open("input.txt") as f:
        text = f.read()
        for line in text.split("\n"):
            res.append(line)
    return res

def search(data, row, col, letter_index, direction):
    row_inc, col_inc = direction
    r = row + row_inc
    c = col + col_inc
    if (0 <= r < len(data)) and (0 <= c < len(data[row])):
        if data[r][c] == SEARCH_STRING[letter_index]:
            if letter_index < len(SEARCH_STRING) - 1:
                return search(data, r, c, letter_index + 1, direction)
            else:
                return 1
    return 0
    
def part1(data):
    res = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == SEARCH_STRING[0]:
                for direction in SEARCH_DIRECTIONS:
                    res += search(data, row, col, 1, direction)
    return res

assert part1(test.split(" ")) == 18

def search2(data, row, col):
    left_diagonal = data[row - 1][col - 1] + data[row][col] + data[row + 1][col + 1]
    right_diagonal = data[row + 1][col - 1] + data[row][col] + data[row - 1][col + 1]
    left_mas = left_diagonal =="MAS" or left_diagonal =="SAM"
    right_mas = right_diagonal =="MAS" or right_diagonal =="SAM"
    return left_mas and right_mas

def part2(data):
    res = 0
    for row in range(1, len(data) - 1):
        for col in range(1, len(data[row]) - 1):
            if data[row][col] == "A":
                res += search2(data, row, col)
    return res

assert part2(test.split(" ")) == 9
def main():
    data = parse_input()
    print("part 1:", part1(data))
    print("part 2:", part2(data))

if __name__ == "__main__":
    main()