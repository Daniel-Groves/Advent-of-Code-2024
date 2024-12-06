import numpy as np
import re

def count_horizontal(array, string):
    count = 0
    for i in range(len(array)):
        line = "".join(array[i])
        count += len(re.findall(string, line))
    return count

def count_vertical(array, string):
    return count_horizontal(np.array(array).T, string)

def count_diagonal(array, string):
    array = np.array(array)

    diags = [array.diagonal(i).tolist() for i in range(-len(array), len(array))] + [np.fliplr(array).diagonal(i).tolist() for i in range(-len(array), len(array))]
    
    return count_horizontal(diags, string)

array = []

with open("input.txt") as f:
    lines = [line.strip() for line in f]
    for line in lines:
        array.append(list(line))


count = count_horizontal(array, "XMAS") + count_vertical(array, "XMAS") + count_horizontal(array, "SAMX") + count_vertical(array, "SAMX") + count_diagonal(array, "XMAS") + count_diagonal(array, "SAMX")

print(count)


