from itertools import product

with open("input.txt") as f:
    lines = [line.strip() for line in f]

lines = [line.split(": ") for line in lines]

sums = []
nums = []

def check_sum(sum, nums, operations):
    if len(nums) == 1:
        if sum == nums[0]:
            return True
        else:
            return False
        
    total = nums[0]

    for i in range(len(nums[1:])):
        if total > sum:
            return False
        if operations[i] == "+":
            total += nums[i+1]
        elif operations[i] == "*":
            total *= nums[i+1]
        elif operations[i] == "||":
            total = int(str(total) + str(nums[i+1]))

    if total == sum:
        return True
    else:
        return False


for line in lines:
    sums.append(int(line[0]))
    nums.append([int(i) for i in line[1].split(" ")])

total = 0

for i in range(len(nums)):
    poss_operations = list(product(["+", "*", "||"], repeat=len(nums[i])-1))
    poss_operations = [list(poss_operation) for poss_operation in poss_operations]

    for poss_operation in poss_operations:
        if check_sum(sums[i], nums[i], poss_operation):
            total += sums[i]
            break


print(total)