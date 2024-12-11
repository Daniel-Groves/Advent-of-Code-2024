input = list(open("input.txt").read())

def move(string):
    gap_index = string.index(".")

    for i in range(len(string)-1,0,-1):
        if string[i] != ".":
            last_file_index = i
            break

    string[gap_index] = string[last_file_index]

    return string[:last_file_index]

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



