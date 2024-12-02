with open('input.txt') as f:
    lines = [line.strip().split() for line in f]

def safe(line):
    for i in range(1, len(line)):
        if not(0 < int(line[i]) - int(line[i-1]) < 4):
            return False
    return True

safe_count = 0

for line in lines:
    if safe(line) or safe (line[::-1]):
        safe_count += 1

print(safe_count)