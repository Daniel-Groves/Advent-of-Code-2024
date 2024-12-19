input = open("input.txt").read().splitlines()

towels = input[0].split(", ")

designs = input[2:]

def can_make(design, towels, memo={}):
    if design in memo:
        return memo[design]
    
    # base case
    if design in towels:
        return True
    
    # recursive case
    for towel in towels:
        if design.startswith(towel):
            if can_make(design[len(towel):], towels, memo):
                memo[design] = True
                return True
            
    memo[design] = False
    return False
            
count = 0

for design in designs:
    if can_make(design, towels):
        count += 1

print(count)
