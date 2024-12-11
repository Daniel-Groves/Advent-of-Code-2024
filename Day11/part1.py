def blink(stones):
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            num = str(stone)
            new_stones.append(int(num[:len(num)//2]))
            new_stones.append(int(num[len(num)//2:]))
        else:
            new_stones.append(stone * 2024)

    return new_stones

def blink_rep(n, input):
    for i in range(n):
        print(i)
        input = blink(input)
    return input


input = (open("input.txt").read())

input = [int(i) for i in input.split(" ")]

print(len(blink_rep(25, input)))