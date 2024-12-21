from itertools import permutations, product

codes = ['A' + code for code in open("input.txt").read().split("\n")]

def get_sequences(start, end, arrows):
    coords = {
        '7': (0, 0), '8': (1, 0), '9': (2, 0),
        '4': (0, 1), '5': (1, 1), '6': (2, 1),
        '1': (0, 2), '2': (1, 2), '3': (2, 2),
        '0': (1, 3), 'A': (2, 3), '^': (1, 0), 
        '<': (0, 1), 'v': (1, 1), '>': (2, 1)
    }

    if arrows:
        coords['A'] == (2, 0)

    x1, y1 = coords[start]
    x2, y2 = coords[end]

    x_diff = x2 - x1
    y_diff = y2 - y1

    moves = []

    if x_diff < 0:
        moves.extend(["<"] * abs(x_diff))

    if y_diff > 0:
        moves.extend(["v"] * y_diff)
    elif y_diff < 0:
        moves.extend(["^"] * abs(y_diff))

    if x_diff > 0:
        moves.extend([">"] * x_diff)

    if arrows:
        if end == '<' or start == '<':
            moves.reverse()
    elif not valid_path(moves, coords, start, (0, 3)):
        moves.reverse()

    moves.append("A")

    return "".join(moves)

def valid_path(path, coords, start, blank):
    # checks if the path crosses over the blank spot
    x1, y1 = coords[start]

    for char in path:
        if char == '>':
            x1 += 1
        elif char == '<':
            x1 -= 1
        elif char == 'v':
            y1 += 1
        elif char == '^':
            y1 -= 1

        if (x1, y1) == blank:
            return False
        
    return True


def get_arrow_sequences(start, end):
    coords = {
    '^': (1, 0), 'A': (2, 0),
    '<': (0, 1), 'v': (1, 1), '>': (2, 1)
    }

    x1, y1 = coords[start]
    x2, y2 = coords[end]

    x_diff = x2 - x1
    y_diff = y2 - y1

    moves = []

    if x_diff < 0:
        moves.extend(["<"] * abs(x_diff))

    if y_diff > 0:
        moves.extend(["v"] * y_diff)
    elif y_diff < 0:
        moves.extend(["^"] * abs(y_diff))

    if x_diff > 0:
        moves.extend([">"] * x_diff)

    if end == '<' or start == '<':
        moves.reverse()

    

    moves.append("A")

    return "".join(moves)

total = 0

for code in codes:
    shortest_robot_1 = "A"

    for i in range(len(code)-1):
        shortest_robot_1 += get_sequences(code[i], code[i+1], False)

    shortest_robot_2 = "A"

    for i in range(len(shortest_robot_1)-1):
        shortest_robot_2 += get_arrow_sequences(shortest_robot_1[i], shortest_robot_1[i+1])

    shortest_human = ""

    for i in range(len(shortest_robot_2)-1):
        shortest_human += get_arrow_sequences(shortest_robot_2[i], shortest_robot_2[i+1])

    total += int(code[1:-1]) * len(shortest_human)

print(total)



