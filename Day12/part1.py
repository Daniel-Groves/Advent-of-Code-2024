import time

with open("input.txt") as f:
    lines = [list(line.strip()) for line in f]

def print_grid(grid):
    for row in grid:
        print("".join(row))

def done(grid):
    for row in grid:
        for cell in row:
            if cell not in [".", "-"]:
                return False
    return True

def calc_region(grid, i, j):
    plant = grid[i][j]
    perimeter = 0
    area = 0

    region = [(i, j)]
    stack = [(i, j)]

    grid[i][j] = "."

    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while stack:
        i, j = stack.pop()
        area += 1
        for vector in vectors:
            if 0 <= i + vector[0] < len(grid) and 0 <= j + vector[1] < len(grid[i]):
                if grid[i + vector[0]][j + vector[1]] == plant:
                    stack.append((i + vector[0], j + vector[1]))
                    grid[i + vector[0]][j + vector[1]] = "."
                    region.append((i + vector[0], j + vector[1]))
                elif grid[i + vector[0]][j + vector[1]] == ".":
                    continue
                else:
                    perimeter += 1
            else:
                perimeter += 1

    return perimeter, area, region

def find_region(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] not in [".", "-"]:
                return calc_region(grid, i, j)

cost = 0

while not done(lines):
    perimeter, area, region = find_region(lines)
    for i, j in region:
        lines[i][j] = "-"
    cost += perimeter * area

print(cost)