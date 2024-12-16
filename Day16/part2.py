import heapq

maze = [list(line) for line in open("input.txt").read().splitlines()]

directions = ["N", "E", "S", "W"]

for y, line in enumerate(maze):
    for x, cell in enumerate(line):
        if cell == "S":
            start = (x, y)
            break

for y, line in enumerate(maze):
    for x, cell in enumerate(line):
        if cell == "E":
            end = (x, y)
            break

start_dir = "E"

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def search(start, end, start_dir):
    priority_queue = []

    heapq.heappush(priority_queue, (0, start[0], start[1], start_dir, []))

    visited = {}
    cheapest_paths = []

    while priority_queue:
        cost, x, y, direction, path = heapq.heappop(priority_queue)

        if (x, y) == end:
            if not cheapest_paths or cost == cheapest_paths[0][0]:
                cheapest_paths.append((cost, path + [(x, y)]))
            elif cost < cheapest_paths[0][0]:
                cheapest_paths = [(cost, path + [(x, y)])]
            continue

        state = (x, y, direction)

        if state in visited and visited[state] < cost:
            continue

        visited[state] = cost

        current_dir_index = directions.index(direction)

        # Move forward
        new_x, new_y = x + dx[current_dir_index], y + dy[current_dir_index]
        if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != "#":
            heapq.heappush(priority_queue, (cost + 1, new_x, new_y, direction, path + [(x, y)]))

        # Turn clockwise
        new_dir_index = (current_dir_index + 1) % 4
        new_dir = directions[new_dir_index]
        heapq.heappush(priority_queue, (cost + 1000, x, y, new_dir, path + [(x, y)]))

        # Turn anti-clockwise
        new_dir_index = (current_dir_index - 1) % 4
        new_dir = directions[new_dir_index]
        heapq.heappush(priority_queue, (cost + 1000, x, y, new_dir, path + [(x, y)]))

    if cheapest_paths:
        return [path for _, path in cheapest_paths]
    else:
        return []

paths = search(start, end, start_dir)

seats = set()

for path in paths:
    for x, y in path:
        seats.add((x, y))

print(len(seats))
