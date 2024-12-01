sum = 0

left = []
right = []

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()
        left.append(int(line[0]))
        right.append(int(line[1]))

dict = {}

for num in set(left):
    dict[num] = left.count(num)

for key in dict:
    sum += dict[key] * key * right.count(key)

print(sum)


