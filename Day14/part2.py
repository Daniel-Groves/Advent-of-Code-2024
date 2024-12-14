import re
import numpy as np

lines = [line.strip() for line in open("input.txt","r")]

width = 101
height = 103

time = 1

var_x = []
var_y = []

for i in range(150):
    x_finals = []
    y_finals = []
    time += 1
    for line in lines:
        x, y, vx, vy = re.findall(r"[-\d]+", line)

        x_final = (int(x) + int(vx) * time) % width
        y_final = (int(y) + int(vy) * time) % height

        x_finals.append(x_final)
        y_finals.append(y_final)

    # compute variance of time
    var_x.append([np.var(x_finals), time])
    var_y.append([np.var(y_finals), time])

#christmas tree will have much lower variance so we can just find x and y with the lowest variance
var_x.sort()
var_y.sort()

bx = var_x[0][1]
by = var_y[0][1]

k = 1

# chinese remainder theorem
while (k*width + bx) % height != by % height:
    k += 1

time = k*width + bx

print(time)