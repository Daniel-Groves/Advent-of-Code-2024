diff = 0

left = []
right = []

with open('input.txt') as f:
    for line in f:
        line = line.strip().split()
        left.append(line[0])
        right.append(line[1])

left.sort()
right.sort()

for i in range(len(left)):
    diff += abs(int(left[i]) - int(right[i]))

print(diff)

