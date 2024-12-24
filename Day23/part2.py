from collections import defaultdict

pairs = [(line.split("-")) for line in open("input.txt").read().split("\n")]

def next_group(groups):
    bigger_groups = []
    i = 0
    for group in groups:
        print(i)
        i += 1
        for group2 in groups:
            # if they only have one differing element
            differing_elements = list((set(group) | set(group2)) - (set(group) & set(group2)))
            if group == ['co', 'de', 'ka'] and group2 == ['co', 'de', 'ta']:
                print(differing_elements)
                print(connections['ta'])
                print(connections['ka'])
            if len(differing_elements) == 2:
                if group == ['co', 'de', 'ka'] and group2 == ['co', 'de', 'ta']:
                    print("hi")
                # print(differing_elements)
                if differing_elements[0] in connections[differing_elements[1]]:
                    # if group == ['co', 'de', 'ka'] and group2 == ['co', 'de', 'ta']:
                    #     print("hi2")
                    bigger_group = set(tuple(sorted(list(set(group) | set(group2)))))
                    # print(bigger_group)
                    if bigger_group not in bigger_groups:
                        # print("adding")
                        bigger_groups.append(bigger_group)

    return bigger_groups

individuals = []

connections = defaultdict(list)

threes = []
for pair in pairs:
    individuals.append(pair[0])
    individuals.append(pair[1])
    connections[pair[0]].append(pair[1])
    connections[pair[1]].append(pair[0])

pairs = [(sorted(pair)) for pair in pairs]

print(len(individuals))

i = 0

for lan in individuals:
    print(i)
    i += 1
    for pair in pairs:
        if lan in pair: continue
        if pair[0] not in connections[lan] or pair[1] not in connections[lan]: continue
        three = sorted([lan, pair[0], pair[1]])
        if three in threes: continue
        threes.append(three)

count = 0
threes = [list(three) for three in threes]

print(threes)

# for three in threes:
#     if "t" in three[0][0] + three[1][0] + three[2][0]:
#         count += 1

biggest_group = threes

i = 0

while biggest_group:
    print(i)
    i += 1
    old_groups = biggest_group
    biggest_group = next_group(biggest_group)
    if biggest_group:
        print(f"len biggest_group: {len(biggest_group)}")

print(old_groups)