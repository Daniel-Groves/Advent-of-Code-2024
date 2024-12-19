from collections import deque

def print_grid():
    for row in grid:
        print("".join(row))

def search():
    queue = deque() 
    queue.append((0, 0, 0))

    visited = set()

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == (grid_size, grid_size):
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= grid_size and 0 <= ny <= grid_size and grid[ny][nx] == "." and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny)) 

    return False

corrupted_coords = []

coords = [line for line in open("input.txt").read().split("\n")]

for coord in coords:
    coords = [int(i) for i in coord.split(",")]
    corrupted_coords.append(coords)

grid_size = 70

grid = []

for i in range(grid_size + 1):
    grid.append(["."] * (grid_size + 1))

for coord in corrupted_coords[:1024]:
    grid[coord[1]][coord[0]] = "#"

traversable = True

i = 1024

while traversable and i < len(corrupted_coords):
    traversable = search()
    if not traversable:
        print(corrupted_coords[i])
        break
    else:
        i += 1
        grid[corrupted_coords[i][1]][corrupted_coords[i][0]] = "#"
