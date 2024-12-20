from collections import deque, defaultdict

grid = [list(line) for line in open("input.txt").read().split("\n")]

MAX_CHEAT = 20

def length_to_end(grid, start, end):
    queue = deque()
    queue.append((start[0], start[1], 0))

    visited = [(start[0], start[1])]

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps, visited

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#" and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.append((nx, ny))

    return None, []

def length_with_cheat(start, end, path):
    saved = path.index(end) - path.index(start) - 2
    if saved <= 0:
        return 0
    return saved

def get_taxi_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1]) + 1

def get_coords_within_taxi_distance(x, y, distance):
    coords = []
    for dx in range(-distance, distance + 1):
        dy_max = distance - abs(dx)
        for dy in range(-dy_max, dy_max + 1):
            if y + dy >= 0 and y + dy < len(grid) and x + dx >= 0 and x + dx < len(grid[0]) and grid[y + dy][x + dx] != "#":
                coords.append((x + dx, y + dy))
    return coords

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "S":
            start = (x, y)
        elif cell == "E":
            end = (x, y)


steps, path = length_to_end(grid, start, end)

saved_count = 0

for start in path:
    for end in get_coords_within_taxi_distance(start[0], start[1], MAX_CHEAT):
        if end not in path: continue
        if get_taxi_distance(start, end) > MAX_CHEAT + 2: continue
        saved = length_with_cheat(start, end, path) - get_taxi_distance(start, end) + 3
        if saved >= 100:
            saved_count += 1

print(saved_count)
