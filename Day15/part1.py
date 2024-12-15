input = open("input.txt").read() 

directions = input.split("\n\n")[1]
grid = [list(i) for i in input.split("\n\n")[0].split("\n")]

def push_block(pos, grid, direction):
    if direction[0] == 0:
        line = grid[pos[0]]
        axis = 1
    elif direction[1] == 0:
        line = [grid[i][pos[1]] for i in range(len(grid))]
        axis = 0

    if direction[axis] == 1:
        line_start = line[:pos[axis]]
        line = line[pos[axis]:]
    elif direction[axis] == -1:
        line_end = line[pos[axis] + 1:]
        line = line[:pos[axis] + 1]
        line.reverse()

    if no_move(line):
        return grid, pos
    else:
        first_clear = line.index(".")
        for i in range(1, first_clear + 1):
            line[i] = "O"
        line[0] = "."
        line[1] = "@"

    if direction[axis] == 1:
        line = line_start + line
    elif direction[axis] == -1:
        line.reverse()
        line = line + line_end

    # put line back in grid
    for i in range(len(line)):
        if axis == 0:
            grid[i][pos[1]] = line[i]
        elif axis == 1:
            grid[pos[0]][i] = line[i]

    return grid, [pos[0] + direction[0], pos[1] + direction[1]]


def no_move(line):
    for i in range(len(line)):
        if line[i] == "#":
            return True
        if line[i] == ".":
            return False

def move(pos, grid, direction):
    if grid[pos[0] + direction[0]][pos[1] + direction[1]] == ".":
        grid[pos[0] + direction[0]][pos[1] + direction[1]] = "@"
        grid[pos[0]][pos[1]] = "."
        pos = [pos[0] + direction[0], pos[1] + direction[1]]
    elif grid[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
        return grid, pos
    elif grid[pos[0] + direction[0]][pos[1] + direction[1]] == "O":
        grid, pos = push_block(pos, grid, direction)

    return grid, pos

def calculate_coord_sum(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                sum += 100 * i + j
    return sum

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            pos = [i,j]
            break

for direction in list(directions)[:]:
    directions = {">": [0,1], "<": [0,-1], "^": [-1,0], "v": [1,0]}

    if direction in directions:
        grid, pos = move(pos, grid, directions[direction])
    
print(calculate_coord_sum(grid))