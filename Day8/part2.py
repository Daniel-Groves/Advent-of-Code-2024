import itertools

with open("input.txt") as f:
    lines = [line.strip() for line in f]

antenna_locs = []

# find the locations of antennas
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] not in  ".#":
            antenna_locs.append([i, j])

# find all pairs of antennas
antenna_loc_pairs = list(itertools.combinations(antenna_locs, 2))

antinode_locs = []

for pair in antenna_loc_pairs:
    antenna_loc = pair[0]
    antenna_loc2 = pair[1]

    # antinodes only created when antennas have same frequency
    if lines[antenna_loc[0]][antenna_loc[1]] != lines[antenna_loc2[0]][antenna_loc2[1]]:
        continue

    # calulcate initial antinode positions (i.e. original antennas)
    antinode_1 = [antenna_loc[0], antenna_loc[1]]
    antinode_2 = [antenna_loc2[0], antenna_loc2[1]]

    # check antinode in bounds and add if so
    if antinode_1 not in antinode_locs:
        if antinode_1[0] >= 0 and antinode_1[1] >= 0 and antinode_1[0] < len(lines) and antinode_1[1] < len(lines[0]):
            antinode_locs.append(antinode_1)

    if antinode_2 not in antinode_locs:
        if antinode_2[0] >= 0 and antinode_2[1] >= 0 and antinode_2[0] < len(lines) and antinode_2[1] < len(lines[0]):
            antinode_locs.append(antinode_2)

    # find as many antinodes in one direction till out of bounds
    while antinode_1[0] >= 0 and antinode_1[1] >= 0 and antinode_1[0] < len(lines) and antinode_1[1] < len(lines[0]):
        antinode_1 = [antinode_1[0] - (antenna_loc2[0] - antenna_loc[0]), antinode_1[1] - (antenna_loc2[1] - antenna_loc[1])]

        # check antinode in bounds and add if so
        if antinode_1 not in antinode_locs:
            if antinode_1[0] >= 0 and antinode_1[1] >= 0 and antinode_1[0] < len(lines) and antinode_1[1] < len(lines[0]):
                antinode_locs.append(antinode_1)

    # find as many antinodes in other direction till out of bounds
    while antinode_2[0] >= 0 and antinode_2[1] >= 0 and antinode_2[0] < len(lines) and antinode_2[1] < len(lines[0]):
        antinode_2 = [antinode_2[0] - (antenna_loc[0] - antenna_loc2[0]), antinode_2[1] - (antenna_loc[1] - antenna_loc2[1])]

        # check antinode in bounds and add if so
        if antinode_2 not in antinode_locs:
            if antinode_2[0] >= 0 and antinode_2[1] >= 0 and antinode_2[0] < len(lines) and antinode_2[1] < len(lines[0]):
                antinode_locs.append(antinode_2)

print(len(antinode_locs))

