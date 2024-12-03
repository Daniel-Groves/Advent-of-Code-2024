import re

txt = open('input.txt').read()

matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", txt)

real_matches = []

do = True

total = 0

for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    elif do:
        num1, num2 = match[4:-1].split(',')
        total += int(num1) * int(num2)

print(total)