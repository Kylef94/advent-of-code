test = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
def get_input():
    with open("input.txt") as f:
        data = f.read()
        return data.split(",")
    
def id_generator(ids):
    id, end = ids.split("-")
    digits = len(id)
    id, end = int(id), int(end)
    while id <= end:
        yield id, digits
        if id == 10 ** digits - 1:
            digits += 1
        id += 1

def part1(id_ranges):
    total = 0
    for ids in id_ranges:
        for id, digits in id_generator(ids):
            n = 10 ** (digits // 2)
            if id // n == id % n:
                total += id
    return total

# def split_num(n, digits):
#      k = 10 ** digits
#      while n > 0:
#          yield n % k
#          n = n // k

def split_num(n, digits):
      n = str(n)
      start = 0
      end = digits
      while end <= len(n):
          yield n[start:end]
          start = end
          end += digits
      if start < len(n):
          yield n[start:]

def part2(id_ranges):
    total = 0
    for ids in id_ranges:
        for id, length in id_generator(ids):
            for d in range(1, (length // 2) + 1):
                digits = [x for x in split_num(id, d)]
                invalid = all([digits[i] == digits[i-1] for i in range(1, len(digits))])
                if invalid:
                    #print("invalid id found:", id)
                    total += id
                    break
    return total

if __name__ == "__main__":
    t = test.split(",")
    print("part 1 test:", part1(t))
    print("part 2 test:", part2(t))
    print("part 1 solution:", part1(get_input()))
    print("part 2 solution:", part2(get_input()))
    # t2 = ["1001001-1010101"]
    # print("part2 t2:", part2(t2))

    