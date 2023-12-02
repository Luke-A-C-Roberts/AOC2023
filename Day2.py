from functools import reduce
from operator import mul
import re

lines = []
with open("Day2.txt", "r") as f:
    lines = f.read().splitlines()

# Part 1
def remove_game_lable(s: str) -> str:
    return s[re.search("Game [0-9]+: ", s).end():]

def split(s: str) -> list[str]:
    return [*map(lambda sub_s: sub_s.strip(), s.split(";"))]

def cubes(l: list[str]) -> list[tuple[int, str]]:
    cube_l = []
    for s in l:
        for m in re.findall("[0-9]+ [red|green|blue]", s):
            substrings = m.split()
            cube_l.append((int(substrings[0]), substrings[1]))
    return cube_l

def cube_numbers(l: list[tuple[int, str]]) -> dict[int, str]:
    d = {"r": 0, "g": 0, "b": 0}
    for (num, color) in l:
        d[color] = max(d[color], num)
    return d

def possible_game(d: dict[int, str]):
    return d["r"] <= 12 and d["g"] <= 13 and d["b"] <= 14

game_sum = 0
game_power = 0
for game_id, line in enumerate(lines):
    line = remove_game_lable(line)
    line = split(line)
    line = cubes(line)
    line = cube_numbers(line)
    if possible_game(line):
        game_sum += game_id + 1
    game_power += reduce(mul, line.values())

print(game_sum)
print(game_power)