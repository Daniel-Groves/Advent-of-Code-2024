secrets = [int(line) for line in open("input.txt").read().split("\n")]

def new_secret(secret, num):
    for _ in range(1, num + 1):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216

    return secret

print(sum(new_secret(secret, 2000) for secret in secrets))