from collections import defaultdict

def split(stone):
    num = str(stone)
    left = int(num[:len(num)//2])
    right = int(num[len(num)//2:])

    return left, right

def blink(stone_counts):
    new_counts = defaultdict(int)

    for stone, count in stone_counts.items():
        if stone == 0:
            new_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            left, right = split(stone)
            new_counts[left] += count
            new_counts[right] += count
        else:
            new_counts[stone * 2024] += count

    return new_counts

def blink_rep(n, stones):
    stone_counts = defaultdict(int)

    for stone in stones:
        stone_counts[stone] += 1

    for i in range(n):
        stone_counts = blink(stone_counts)
    
    return sum(stone_counts.values())


input = (open("input.txt").read())

input = [int(i) for i in input.split(" ")]

print(blink_rep(75, input))