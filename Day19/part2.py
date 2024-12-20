input = open("input.txt").read().splitlines()

towels = input[0].split(", ")

designs = input[2:]

def can_make_num(design, towels, memo={}):
    if design in memo:
        return memo[design]
    
    num_ways = 0
    
    for towel in towels:
        if design == towel:
            num_ways += 1
        elif design.startswith(towel):
            num_ways += can_make_num(design[len(towel):], towels, memo)
            
    memo[design] = num_ways
    return num_ways
            
count = 0

for design in designs:
    count += can_make_num(design, towels)

print(count)
