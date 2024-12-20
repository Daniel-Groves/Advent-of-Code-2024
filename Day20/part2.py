from collections import deque, defaultdict

grid = [list(line) for line in open("input.txt").read().split("\n")]

MAX_CHEAT = 1

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

def length_with_cheat(grid, start, end, cheat_wall, path):
    saves = [0]

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = wall[0] + dx, wall[1] + dy
        ox, oy = wall[0] - dx, wall[1] - dy
        if (nx, ny) in path and (ox, oy) in path:
            saves.append(abs(path.index((nx, ny)) - path.index((ox, oy))) - 2)

    return max(saves)

walls = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "S":
            start = (x, y)
        elif cell == "E":
            end = (x, y)
        elif cell == "#":
            walls.append((x, y))

steps, path = length_to_end(grid, start, end)

saved_count = 0
counts = defaultdict(int)
print(path)
print(len(walls))

# for wall in walls:
#     saved = length_with_cheat(grid, start, end, wall, path)
#     print(saved)
#     if saved:
#         counts[saved] += 1
#     if saved >= 100:
#         saved_count += 1

for path_point in path:


print(saved_count)
print(counts)