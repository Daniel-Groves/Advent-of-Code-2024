from itertools import permutations, product
from functools import cache
import time

codes = [code for code in open("input.txt").read().split("\n")]

@cache
def get_sequences(start, end, arrows):
    coords = {
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '1': (0, 2), '2': (1, 2), '3': (2, 2),
    '0': (1, 3), 'A': (2, 3), '^': (1, 0), 
    '<': (0, 1), 'v': (1, 1), '>': (2, 1)
    }

    if arrows:
        coords['A'] = (2, 0)

    x1, y1 = coords[start]
    x2, y2 = coords[end]

    x_diff, y_diff = x2 - x1, y2 - y1
    moves = []

    if x_diff < 0:
        moves.extend(["<"] * abs(x_diff))

    if y_diff > 0:
        moves.extend(["v"] * y_diff)
    elif y_diff < 0:
        moves.extend(["^"] * abs(y_diff))

    if x_diff > 0:
        moves.extend([">"] * x_diff)

    if arrows and (end == '<' or start == '<'):
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

@cache
def compute_path_length(sequence, depth):
    if depth == 1:
        return len(sequence)

    if any(char in sequence for char in "0123456789"):
        arrows = False
    else:
        arrows = True
    
    res = 0

    sequence = "A" + sequence

    for i in range(len(sequence) - 1):
        res += compute_path_length(get_sequences(sequence[i], sequence[i + 1], arrows), depth - 1)

    return res

total = 0

start = time.time()

for code in codes:
    total += int(code[:-1]) * compute_path_length(code, 27)

print(total)

print(time.time() - start)



