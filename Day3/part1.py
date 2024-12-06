import re

txt = open('input.txt').read()

matches = re.findall(r"mul\(\d+,\d+\)", txt)

total = 0

for match in matches:
    num1, num2 = match[4:-1].split(',')
    total += int(num1) * int(num2)

print(total)