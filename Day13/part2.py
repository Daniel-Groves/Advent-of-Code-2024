lines = [line.strip() for line in open("input.txt","r")]

lines = [line for line in lines if line != ""]

machines = []

def cost_presses(a_presses, b_presses):
    return 3 * a_presses + b_presses

def solve_equation(ax, ay, bx, by, px, py):
    a = round((py - ((by * px) / bx)) / (ay - ((by * ax) / bx)))
    b = round((px - ax * a) / bx)
    
    if ax * a + bx * b == px and ay * a + by * b == py:
        return cost_presses(a,b)
    return 0


def cost_machine(machine):
    a_moves = machine[0]
    b_moves = machine[1]
    prize = machine[2]

    return solve_equation(a_moves[0], a_moves[1], b_moves[0], b_moves[1], prize[0], prize[1])



for i in range(0,len(lines),3):
    machine = []
    button_a = [int(lines[i][12:14])] + [int(lines[i][18:20])]
    button_b = [int(lines[i+1][12:14])] + [int(lines[i+1][18:20])]
    prize = lines[i+2].split(", ")
    prize = [10000000000000+int(prize[0][9:])] + [10000000000000+int(prize[1][2:])]

    machine.append(button_a)
    machine.append(button_b)
    machine.append(prize)
    machines.append(machine)

cost = 0

for machine in machines:
    cost += cost_machine(machine)

print(cost)