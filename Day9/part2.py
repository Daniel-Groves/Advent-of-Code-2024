from copy import deepcopy

input = list(open("input.txt").read())

def move(storage):
    # find gaps and files
    gaps = [i for i in storage if i[0] == "."]
    files = [i for i in storage[::-1] if i[0] != "."]

    for index, file in enumerate(files[:]):
        # find the leftmost gap that can fit the file and the leftover space
        gap_index, leftover= get_leftmost_gap(file, gaps, storage)

        # if there is a suitable gap
        if gap_index is not None:

            # some jank splitting so we can recraft the storage
            storage_start = storage[:storage.index(gaps[gap_index])]
            storage_end = storage[storage.index(gaps[gap_index])+1:]

            # one could call this a bad smell...
            middle_part = deepcopy([file])

            # add leftover gap
            if leftover > 0:
                middle_part += [[".", leftover]]

            # replace the moved file with a gap
            try:
                storage_start[storage_start.index(file)][0] = "."
            except:
                pass

            try:
                storage_end[storage_end.index(file)][0] = "."
            except:
                pass

            storage = storage_start + middle_part + storage_end

            storage = deepcopy(storage)

            gaps = [i for i in storage if i[0] == "."]
            files = [i for i in storage[::-1] if i[0] != "."]

    return storage

def get_leftmost_gap(file, gaps, storage):
    # look through gaps to find the first one that can fit the file
    for index, gap in enumerate(gaps):
        # we only want to move it if we are moving it left
        if storage.index(gap) > storage.index(file):
            break
        if file[1] <= gap[1]:
            return index, int(gap[1]) - int(file[1])

    return None, None

def calculate_checksum(translation):
    checksum = 0
    iterator = 0

    for i in range(len(translation)):
        for j in range(translation[i][1]):
            if str(translation[i][0]) not in  ".n":
                checksum += int(translation[i][0]) * iterator
            iterator += 1

    return checksum

translation = []

# turn input into a list of lists where each list is of the form [id, length] or in the case of a gap [".", length]
for i in range(len(input)):
    if i % 2 == 0:
        translation.append([(i // 2), int(input[i])])    
    else:
        if int(input[i]) > 0:
            translation.append([".", int(input[i])])


translation = move(translation)

checksum = calculate_checksum(translation)

print(checksum)




