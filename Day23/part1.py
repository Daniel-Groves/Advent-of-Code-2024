pairs = [(line.split("-")) for line in open("input.txt").read().split("\n")]
individuals = []

threes = []

for pair in pairs:
    individuals.append(pair[0])
    individuals.append(pair[1])

pairs = [(sorted(pair)) for pair in pairs]

print(len(individuals))

i = 0

for lan in individuals:
    print(i)
    i += 1
    for pair in pairs:
        if lan in pair: continue
        if sorted([lan, pair[0]]) in pairs and sorted([lan, pair[1]]) in pairs:
            three = sorted([lan, pair[0], pair[1]])
            if three in threes: continue
            threes.append(three)

count = 0
threes = [list(three) for three in threes]
for three in threes:
    if "t" in three[0][0] + three[1][0] + three[2][0]:
        count += 1

print(count)