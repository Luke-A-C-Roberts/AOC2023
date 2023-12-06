import re
from itertools import product, starmap

lines = []
with open("Day3.txt", "r") as f:
    lines = f.read().splitlines()

# Part 1
def part_numbers(ls: list[str]) -> list:
    numbers = []
    lens = set()
    for i, l in enumerate(ls):
        for re_match in re.finditer(r"[0-9]+", l):
            check_xs = [*filter(
                lambda x: 0<=x<len(l),
                range(re_match.start()-1, re_match.end()+1)
            )]
            check_ys = [*filter(
                lambda x: 0<=x<len(ls),
                range(i-1,i+2)
            )]
            check_chars = [*starmap(
                lambda x, y: ls[y][x],
                product(check_xs, check_ys)
            )]
            if [c for c in check_chars if c in [*"$%&*-+=#@/"]]:
                numbers.append(int(re_match.group()))

    return numbers

print(sum(part_numbers(lines)))

# Part 2
def gear_ratios(ls: list[str]) -> list:
    coords = []
    for y, row in enumerate(ls):
        for x, c in enumerate(row):
            if c == "*":
                coords.append(tuple([x, y]))
    gears = []
    for x, y in coords:
        xr = [*filter(lambda a: -1 < a < len(ls[0]), range(x-4, x+1))]
        yr = [*filter(lambda a: -1 < a < len(ls),    range(y-1, y+2))]

        re_matches = sum(
            [[*re.finditer(r"[^0-9][0-9]{1,3}", ls[i])] for i in yr],
            []
        )

        nums = [*map(
            lambda m: int(m.group()[1:]),
            filter(lambda m: m.start() in xr, re_matches))
        ]
        if len(nums) == 2:
            gears.append(nums[0] * nums[1])


    return gears

# gear_ratios(lines)
print(87287096)
print(sum(gear_ratios(lines)))