import re

input = [lines for lines in open("input.txt").read().splitlines()]

program = [int(i) for i in input[4][9:].split(",")]

b = int((re.findall(r"\d+", input[1]))[0])
c = int((re.findall(r"\d+", input[2]))[0])

def combo_operand_value(operand):
    global a, b, c
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        print("Something went wrong with returning the combo operand")

def adv(operand, a):
    return int(a / 2**(combo_operand_value(operand)))

def bxl(operand, b):
    return b ^ operand

def bst(operand, b):
    return combo_operand_value(operand) % 8

def jnz(operand):
    if a != 0:
        return operand - 2
    else:
        return instruction_pointer
    
def bxc(operand, b, c):
    return b ^ c

def out(operand):
    return combo_operand_value(operand) % 8

def bdv(operand, a):
    return int(a / 2**(combo_operand_value(operand)))

def cdv(operand, a):
    return int(a / 2**(combo_operand_value(operand)))

def reverse_engineer(program_outputs):
    # Start with A = 0 as the only valid value for the last output
    valid_vals_for_a = {0}

    for required_output in reversed(program_outputs):
        next_vals_for_a = set()

        for a_val in valid_vals_for_a:
            a_shifted = a_val * 8

            # Test all possible 3-bit combinations (0 through 7)
            for candidate_a in range(a_shifted, a_shifted + 8):
                out = run(candidate_a)

                # Check if the first output matches the required output
                if out and out[0] == required_output:
                    next_vals_for_a.add(candidate_a)

        valid_vals_for_a = next_vals_for_a

    return min(valid_vals_for_a)


def run(a_in):
    global a, b, c, instruction_pointer
    a = a_in

    instruction_pointer = 0

    output = []

    halt = False

    while not halt:
        if instruction_pointer + 1 >= len(program):
            halt = True
            break

        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:
            a = adv(operand, a)
        elif opcode == 1:
            b = bxl(operand, b)
        elif opcode == 2:
            b = bst(operand, b)
        elif opcode == 3:
            instruction_pointer = jnz(operand)
        elif opcode == 4:
            b = bxc(operand, b, c)
        elif opcode == 5:
            output.append(str(out(operand)))
        elif opcode == 6:
            b = bdv(operand, a)
        elif opcode == 7:
            c = cdv(operand, a)
        else:
            print("Something went wrong with getting the opcode")

        instruction_pointer += 2

    output = [int(i) for i in output]

    return output

print(reverse_engineer(program))