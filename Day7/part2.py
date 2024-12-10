from itertools import product

with open("input.txt") as f:
    lines = [line.strip() for line in f]

lines = [line.split(": ") for line in lines]

sums = []
nums = []

def can_reach_target(target, nums, index=0, current_result=0):
    # Base case
    if index == len(nums):
        return current_result == target
    
    # Recursive case
    next_num = nums[index]

    # Try adding
    if can_reach_target(target, nums, index + 1, current_result + next_num):
        return True
    
    # Try multiplying
    if can_reach_target(target, nums, index + 1, current_result * next_num):
        return True
    
    # Try concatenating
    if can_reach_target(target, nums, index + 1, int(str(current_result) + str(next_num))):
        return True
    
    return False


for line in lines:
    sums.append(int(line[0]))
    nums.append([int(i) for i in line[1].split(" ")])

total = 0

for i in range(len(nums)):
    if can_reach_target(sums[i], nums[i]):
        total += sums[i]

print(total)