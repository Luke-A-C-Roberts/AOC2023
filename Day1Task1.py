import re

lines = []
with open("Day1Task1.txt", "r") as f:
    lines = f.readlines()
lines = [*map(lambda s: s.strip(), lines)]

char_numbers = [chr(i) for i in range(49, 58)]
spelled_numbers = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
spelled_numbers_r = [*map(lambda x: x[::-1], spelled_numbers)]

def find_first_number(l: str, r: bool):
    l = l[::-1] if r else l
    spelled = spelled_numbers_r if r else spelled_numbers
    s = re.search(
        '|'.join(char_numbers)
        + '|'
        + '|'.join(spelled),
        l
    )
    return s

def solve(l: str) -> int:
    print(l)
    r1 = find_first_number(l, False)
    r2 = find_first_number(l, True)

    if r1.span() == tuple([len(l) - r2.end(), len(l) - r2.start()]):
        if r1.group(0) in spelled_numbers:
            return 11 * (spelled_numbers.index(r1.group(0)) + 1)
        return 11 * int(r1.group(0))

    if r1.group(0) in spelled_numbers:
        r1 = spelled_numbers.index(r1.group(0)) + 1
    else:
        r1 = int(r1.group(0))
    if r2.group(0) in spelled_numbers_r:
        r2 = spelled_numbers_r.index(r2.group(0)) + 1
    else:
        r2 = int(r2.group(0))

    return 10 * r1 + r2

# print(solve("bfqpb9"))
print(sum(map(solve, lines)))

