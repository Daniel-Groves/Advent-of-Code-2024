input = list(open("input.txt").read())

def move(string):
    gap_index = string.index(".")


    for i in range(len(string)):
        if string[len(string) - 1 - i] != ".":
            last_file_index = len(string) - 1 - i
            break

    string[gap_index] = string[last_file_index]
    string[last_file_index] = "."

    return string

translation = []

for i in range(len(input)):
    if i % 2 == 0:
        for j in range(int(input[i])):
            translation.append(i // 2)
    else:
        for j in range(int(input[i])):
            translation.append(".")

count = 0


initial_free_space_count = translation.count(".")
while translation.count(".") > 0 and "." in translation[:-initial_free_space_count]:
    translation = move(translation)


checksum = 0

for i in range(len(translation)):
    if translation[i] != ".":
        checksum += int(translation[i]) * i

print(checksum)



