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
    area = 0

    region = [(i, j)]
    stack = [(i, j)]

    grid[i][j] = "."
    plots = set()  # Keep track of all plots in the region

    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while stack:
        i, j = stack.pop()
        area += 1
        plots.add((i, j))  # Add the current plot to the region
        for vector in vectors:
            ni, nj = i + vector[0], j + vector[1]
            in_bounds = 0 <= ni < len(grid) and 0 <= nj < len(grid[ni])
            if in_bounds and grid[ni][nj] == plant:
                stack.append((ni, nj))
                grid[ni][nj] = "."

    # Calculate corners
    corners = 0
    for plot in plots:
        i, j = plot
        # Neighboring cells
        ul = (i - 1, j - 1)
        u = (i - 1, j)
        ur = (i - 1, j + 1)
        r = (i, j + 1)
        dr = (i + 1, j + 1)
        d = (i + 1, j)
        dl = (i + 1, j - 1)
        l = (i, j - 1)

        # Outward corners
        if all(neighbor not in plots for neighbor in [u, ur, r]):
            corners += 1
        if all(neighbor not in plots for neighbor in [u, ul, l]):
            corners += 1
        if all(neighbor not in plots for neighbor in [d, dl, l]):
            corners += 1
        if all(neighbor not in plots for neighbor in [d, dr, r]):
            corners += 1

        # Inward corners
        if u in plots and r in plots and ur not in plots:
            corners += 1
        if u in plots and l in plots and ul not in plots:
            corners += 1
        if d in plots and l in plots and dl not in plots:
            corners += 1
        if d in plots and r in plots and dr not in plots:
            corners += 1

        if u not in plots and l not in plots and ul in plots:
            corners += 1
        if u not in plots and r not in plots and ur in plots:
            corners += 1
        if d not in plots and l not in plots and dl in plots:
            corners += 1
        if d not in plots and r not in plots and dr in plots:
            corners += 1    

    print(corners)
    return corners, area, region


def find_region(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] not in [".", "-"]:
                return calc_region(grid, i, j)

cost = 0

while not done(lines):
    sides, area, region = find_region(lines)
    for i, j in region:
        lines[i][j] = "-"
    cost += sides * area

print(cost)