import re

lines = [line.strip() for line in open("input.txt","r")]

width = 101
height = 103

top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0

for line in lines:
    x, y, vx, vy = re.findall(r"[-\d]+", line)

    x_final = (int(x) + int(vx) * 100) % width
    y_final = (int(y) + int(vy) * 100) % height

    if x_final < width // 2 and y_final < height // 2:
        top_left += 1
    elif x_final > width // 2 and y_final < height // 2:
        top_right += 1
    elif x_final < width // 2 and y_final > height // 2:
        bottom_left += 1
    elif x_final > width // 2 and y_final > height // 2:
        bottom_right += 1

print(top_left * top_right * bottom_left * bottom_right)