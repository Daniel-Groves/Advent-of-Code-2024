import time

input = open("input.txt").read() 

directions_input = input.split("\n\n")[1]
grid = [list(i) for i in input.split("\n\n")[0].split("\n")]

# reddit helped
def move_and_push(grid, pos_x, pos_y, dir_x, dir_y):
    stack = []
    path = [(pos_x, pos_y)]
    visited = set()
    while path:
        x, y = path.pop()
        if (x, y) in visited or grid[x][y] == ".":
            continue
        visited.add((x, y))
        if grid[x][y] == "#":
            return (pos_x, pos_y)
        stack.append(((grid[x][y], x, y)))
        path.append((x + dir_x, y + dir_y))
        if grid[x][y] == "[":
            path.append((x, y + 1))
        if grid[x][y] == "]":
            path.append((x, y - 1))

    if dir_x > 0:
        stack.sort(key=lambda path: path[1])
    if dir_x < 0:
        stack.sort(key=lambda path: -path[1])
    if dir_y > 0:
        stack.sort(key=lambda path: path[2])
    if dir_y < 0:
        stack.sort(key=lambda path: -path[2])

    while stack:
        char, old_x, old_y = stack.pop()
        grid[old_x + dir_x][old_y + dir_y] = char
        grid[old_x][old_y] = "."

    return (pos_x + dir_x, pos_y + dir_y)

def calculate_coord_sum(grid):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                sum += 100 * i + j
    return sum

for row in range(len(grid)):
    for column in range(len(grid[row])):
        if grid[row][column] == ".":
            grid[row][column] = ".."
        elif grid[row][column] == "O":
            grid[row][column] = "[]"
        elif grid[row][column] == "#":
            grid[row][column] = "##"
        elif grid[row][column] == "@":
            grid[row][column] = "@."

    grid[row] = list("".join(grid[row]))

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            pos = [i,j]
            break

directions = {">": [0,1], "<": [0,-1], "^": [-1,0], "v": [1,0]}

for direction in list(directions_input)[:]:
    if direction in directions:
        pos[0], pos[1] = move_and_push(grid, pos[0], pos[1], directions[direction][0], directions[direction][1])
    
print(calculate_coord_sum(grid))