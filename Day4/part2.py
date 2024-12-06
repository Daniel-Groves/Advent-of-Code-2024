import numpy as np
import re

array = []

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    for line in lines:
        array.append(list(line))

count = 0

for i in range(1, len(array)-1):
    for j in range(1, len(array[i])-1):
        if array[i][j] == "A" and (array[i+1][j+1] + array[i-1][j-1] in "SMS") and (array[i-1][j+1] + array[i+1][j-1] in "SMS"):
            count += 1

print(count)



