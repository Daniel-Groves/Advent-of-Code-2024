from collections import deque

corrupted_coords = []

coords = [line for line in open("input.txt").read().split("\n")][:1024]
for coord in coords:
    coords = [int(i) for i in coord.split(",")][:1024]
    corrupted_coords.append(coords)

grid_size = 70

grid = []

def print_grid():
    for row in grid:
        print("".join(row))

for i in range(grid_size + 1):
    grid.append(["."] * (grid_size + 1))

for coord in corrupted_coords:
    grid[coord[1]][coord[0]] = "#"

queue = deque() 
queue.append((0, 0, 0))

visited = set()

while queue:
    x, y, steps = queue.popleft()

    if (x, y) == (grid_size, grid_size):
        print(steps)
        break

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= grid_size and 0 <= ny <= grid_size and grid[ny][nx] == "." and (nx, ny) not in visited:
            queue.append((nx, ny, steps + 1))
            visited.add((nx, ny)) 

print_grid()