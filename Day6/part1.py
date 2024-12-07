with open("input.txt") as f:
    lines = [list(line.strip()) for line in f]

initial_pos = (0, 0)

def move(pos, direction, grid):
    xpos = pos[0]
    ypos = pos[1]

    xdir = direction[0]
    ydir = direction[1]

    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    while True:
        if xpos + xdir < 0 or xpos + xdir >= len(lines[0]):
            grid[ypos][xpos] = "X"
            return grid
        elif ypos + ydir < 0 or ypos + ydir >= len(lines):
            grid[ypos][xpos] = "X"
            return grid
        
        if grid[ypos + ydir][xpos + xdir] == "#":
            current_dir = directions.index([xdir, ydir])
            next_dir = directions[(current_dir + 1) % 4]
            xdir = next_dir[0]
            ydir = next_dir[1]
        
        grid[ypos][xpos] = "X"
        ypos += ydir
        xpos += xdir

for line in lines:
    if "^" in line:
        initial_pos = (line.index("^"), lines.index(line))
        break

grid = move(initial_pos, [0, -1], lines)

count = 0
for line in grid:
    count += line.count("X")


print(count)


