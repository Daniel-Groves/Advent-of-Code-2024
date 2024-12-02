with open('input.txt') as f:
    lines = [line.strip().split() for line in f]

def safe_with_removal(line):
    for i in range(1, len(line)):
        if not(0 < int(line[i]) - int(line[i-1]) < 4):
            return(safe(line[:i-1] + line[i:]) or safe(line[:i] + line[i+1:]))
    return True

def safe(line):
    for i in range(1, len(line)):
        if not(0 < int(line[i]) - int(line[i-1]) < 4):
            return False
    return True

safe_count = 0

for line in lines:
    reversed_line = line[::-1]
    if safe_with_removal(line) or safe_with_removal(reversed_line):
        safe_count += 1

print(safe_count)