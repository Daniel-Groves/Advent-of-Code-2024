def trailhead_score(lines, i, j, num, visited):
    # Base case of reaching 9
    if num == 9 and [i, j] not in visited:
        visited.append([i, j])
        return 1
    
    # Recursive case
    score = 0
    up_score = 0
    down_score = 0
    left_score = 0
    right_score = 0

    #check in bounds
    if i - 1 >= 0:
        if lines[i - 1][j] == str(num + 1):
            up_score = trailhead_score(lines, i - 1, j, num + 1, visited)

    if i + 1 < len(lines):
        if lines[i + 1][j] == str(num + 1):
            down_score = trailhead_score(lines, i + 1, j, num + 1, visited)

    if j - 1 >= 0:
        if lines[i][j - 1] == str(num + 1):
            left_score = trailhead_score(lines, i, j - 1, num + 1, visited)

    if j + 1 < len(lines[i]):
        if lines[i][j + 1] == str(num + 1):
            right_score = trailhead_score(lines, i, j + 1, num + 1, visited)

    score = up_score + down_score + left_score + right_score

    return score


with open("input.txt") as f:
    lines = [list(line.strip()) for line in f]

total = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "0":
            total += trailhead_score(lines, i , j, 0, [])

print(total)