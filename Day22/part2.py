from collections import deque, defaultdict
from itertools import product

secrets = [int(line) for line in open("input.txt").read().split("\n")]

def new_secret(secret, num):
    for _ in range(1, num + 1):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216

    return secret

sequences = defaultdict(int)

for secret in secrets:
    sequences_set = set()
    changes = deque()
    changes.append(new_secret(secret, 1) - secret)
    secret = new_secret(secret, 1)
    for _ in range(1, 2001):
        next_secret = new_secret(secret, 1)
        changes.append(int(str(next_secret)[-1]) - int(str(secret)[-1]))
        secret = next_secret

        if len(changes) > 4:
            changes.popleft()

        if tuple(changes) in sequences_set:
            continue

        sequences[tuple(changes)] += int(str(secret)[-1])
        sequences_set.add(tuple(changes))
    
max_sequence = max(sequences, key=sequences.get)
print(sequences[max_sequence])