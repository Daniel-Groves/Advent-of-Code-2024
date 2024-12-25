input = open("input.txt").read().split("\n\n")

locks = []
keys = []

def get_nums(lock_or_key):
    return [sum(1 for row in lock_or_key if row[i] == "#") - 1 for i in range(5)]

for item in input:
    if item.startswith("#####"):
        locks.append([list(item) for item in item.split("\n")])
    else:
        keys.append([list(item) for item in item.split("\n")])

locks = [get_nums(lock) for lock in locks]
keys = [get_nums(key) for key in keys]

fit_count = 0

for key in keys:
    for lock in locks:
        sums = [key[i] + lock[i] for i in range(0, 5)]
        if all([sums[i] < 6 for i in range(0, 5)]):
            fit_count += 1

print(fit_count)