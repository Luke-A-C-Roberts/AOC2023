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
    return re.search('|'.join(char_numbers) + '|' + '|'.join(spelled), l)


def convert_to_int(m: re.Match, r: bool) -> int:
    spelled = spelled_numbers_r if r else spelled_numbers
    if m.group(0) in spelled:
        return spelled.index(m.group(0)) + 1
    return int(m.group(0))


def solve(l: str) -> int:
    [m1, m2] = [*map(lambda b: find_first_number(l, b), [False, True])]

    if [*m1.span()] == [len(l) - m2.end(), len(l) - m2.start()]:
        return 11 * convert_to_int(m1, False)

    return 10 * convert_to_int(m1, False) + convert_to_int(m2, True)


print(sum(map(solve, lines)))