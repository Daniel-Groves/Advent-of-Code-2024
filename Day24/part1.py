from collections import defaultdict
from copy import deepcopy

input = open("input.txt").read().split("\n\n")
wires_in = ([wire.split(": ") for wire in input[0].split("\n")])

instructions = [instruction.replace(" ->", "").split(" ") for instruction in input[1].split("\n")]

wires = defaultdict(int)

for wire in wires_in:
    wires[wire[0]] = int(wire[1])

while True: 
    old_wires = deepcopy(wires)

    for instruction in instructions:
        if instruction[1] == "AND":
            wires[instruction[3]] = wires[instruction[0]] & wires[instruction[2]]
        elif instruction[1] == "OR":
            wires[instruction[3]] = wires[instruction[0]] | wires[instruction[2]]
        elif instruction[1] == "XOR":
            wires[instruction[3]] = wires[instruction[0]] ^ wires[instruction[2]]

    if old_wires == wires:
        break

z_wires = {key: value for key, value in wires.items() if key.startswith('z')}

result = 0

for i in range(0, len(z_wires)):
    result += z_wires['z' + str(i).zfill(2)] * (2 ** (i))

print(result)