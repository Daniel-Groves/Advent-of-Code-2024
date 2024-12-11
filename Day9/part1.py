input = list(open("input.txt").read())

def move(storage):
    gap_index = storage.index(".")

    for i in range(len(storage)-1,0,-1):
        if storage[i] != ".":
            last_file_index = i
            break

    storage[gap_index] = storage[last_file_index]

    return storage[:last_file_index]

translation = []

for i in range(len(input)):
    if i % 2 == 0:
        for j in range(int(input[i])):
            translation.append(i // 2)
    else:
        for j in range(int(input[i])):
            translation.append(".")

count = 0

while "." in translation:
    translation = move(translation)

checksum = 0

for i in range(len(translation)):
    if translation[i] != ".":
        checksum += int(translation[i]) * i

print(checksum)



