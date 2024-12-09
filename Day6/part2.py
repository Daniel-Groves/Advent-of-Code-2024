import copy 

with open("input.txt") as f:
    lines = [list(line.strip()) for line in f]

initial_pos = (0, 0)

direction_position_pairs = []

def move(init_pos, init_direction, grid):
    visited = set()

    x = init_pos[0]
    y = init_pos[1]

    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    dir_index = directions.index(init_direction)


    while 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        state = (y, x, dir_index)
        if state in visited:
            return True
        visited.add(state)

        dx, dy = directions[dir_index]
        ny, nx = y + dy, x + dx

        if ny >= len(grid) or ny < 0 or nx >= len(grid[0]) or nx < 0:
            return False

        if not (0 <= ny < len(grid) and 0 <= nx < len(grid[0])) or grid[ny][nx] in "#O":
            dir_index = (dir_index + 1) % 4
        else:
            y, x = ny, nx

    return False  

def print_grid(grid):
    for line in grid:
        print("".join(line))

for line in lines:
    if "^" in line:
        initial_pos = (line.index("^"), lines.index(line))
        break

old_grid = copy.deepcopy(lines)


count = 0

for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        direction_position_pairs = []
        if cell == "." and not([x, y] == initial_pos):
            lines[y][x] = "O"
            if move(initial_pos, [0, -1], lines):
                count += 1
            lines[y][x]= "."




print(count)


