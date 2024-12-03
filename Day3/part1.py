import re

txt = open('input.txt').read()

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", txt)

real_matches = []

do = True

for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif do:
        real_matches.append(match)

real_matches = [match[4:-1].split(',') for match in real_matches]

total = sum([int(match[0]) * int(match[1]) for match in real_matches])

print(total)