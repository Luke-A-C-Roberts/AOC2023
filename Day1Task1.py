import re

lines = []
with open("Day1Task1.txt", "r") as f:
    lines = f.read().splitlines()

cn = [chr(i) for i in range(49, 58)]
sn = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
sn_r = [*map(lambda x: x[::-1], sn)]


def find_first_number(l: str, r: bool):
    (l, s) = (l[::-1], sn_r) if r else (l, sn)
    return re.search('|'.join([*cn, *s]), l)


def convert_to_int(m: re.Match, r: bool) -> int:
    s = sn_r if r else sn
    g = m.group()
    return s.index(g) + 1 if g in s else int(g)


def solve(l: str) -> int:
    [m1, m2] = [*map(lambda b: find_first_number(l, b), [False, True])]

    if [*m1.span()] == [len(l) - m2.end(), len(l) - m2.start()]:
        return 11 * convert_to_int(m1, False)

    return 10 * convert_to_int(m1, False) + convert_to_int(m2, True)


print(sum(map(solve, lines)))