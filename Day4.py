import re
from itertools import starmap, repeat
from more_itertools import unzip

lines = []
with open("Day4.txt", "r") as f:
    lines = f.read().splitlines()

#part 1
lines = [*map(
    lambda s: s[re.match(r"Card\s+\d+:\s", s).end():].split("|"),
    lines
)]

winning_nums, nums = [*map(list, unzip(lines))]

def get_nums(n: list[str]) -> list[int]:
    return [*map(lambda s: set(map(lambda s: int(s.group()), list(re.finditer(r"\d+", s)))), n)]

winning_nums = get_nums(winning_nums)
nums = get_nums(nums)

scores = [*starmap(lambda a, b: len(a & b), zip(winning_nums, nums))]
calculated_scores = [*map(lambda x: 0 if not x else 2 ** (x - 1), scores)]

print(sum(calculated_scores))

#part 2
card_counts = [*repeat(1, len(lines))]
for i, score in enumerate(scores):
    card_count = card_counts[i]
    for j in range(i + 1, i + score + 1):
        card_counts[j] += card_count

print(sum(card_counts))