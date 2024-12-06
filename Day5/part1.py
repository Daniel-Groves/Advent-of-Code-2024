txt = open('input.txt').read()

txt = txt.split('\n\n')

rules = [rule.split('|') for rule in txt[0].split('\n')]
updates = [update.split(',') for update in txt[1].split('\n')[1:-1]]

total = 0

def check_rules(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True

for update in updates:
    add = True
    if check_rules(rules, update):
        total += int(update[int((len(update)-1)/2)])

print(total)