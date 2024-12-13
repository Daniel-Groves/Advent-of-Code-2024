lines = [line.strip() for line in open("input.txt","r")]

lines = [line for line in lines if line != ""]

machines = []

def cost_presses(machine, a_presses, b_presses):
    return 3 * a_presses + b_presses

def cost_machine(machine):
    costs = []
    button_presses = []

    a_moves = machine[0]
    b_moves = machine[1]
    prize = machine[2]

    for i in range(0,100):
        position_x = 0
        position_y = 0
        position_x += int(a_moves[0]) * i
        position_y += int(a_moves[1]) * i

        if position_x > prize[0] or position_y > prize[1]:
            break

        for j in range(100,0,-1):
            if (position_x + int(b_moves[0]) * j) == prize[0] and (position_y + int(b_moves[1]) * j) == prize[1]:
                button_presses.append((i,j))
                costs.append(cost_presses(machine,i,j))
                break

    return min(costs) if costs else 0



for i in range(0,len(lines),3):
    machine = []
    button_a = [int(lines[i][12:14])] + [int(lines[i][18:20])]
    button_b = [int(lines[i+1][12:14])] + [int(lines[i+1][18:20])]
    prize = lines[i+2].split(", ")
    prize = [int(prize[0][9:])] + [int(prize[1][2:])]

    machine.append(button_a)
    machine.append(button_b)
    machine.append(prize)
    machines.append(machine)

cost = 0

for machine in machines:
    cost += cost_machine(machine)

print(cost)