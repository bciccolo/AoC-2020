import copy

infinite_loop = False

def main():
    instructions = parse_instructions()
    # print(instructions)
    print("Part 1: " + str(run_instructions(instructions)))
    print("Part 2: " + str(modify_instructions(instructions)))


def modify_instructions(instructions):
    global infinite_loop

    result = 0

    # Strategy: modify the first instruction in the program and see if it runs, if it does then
    # we're done, if doeesn't then go back to the original program and modify the next instruction
    for attempt in range(len(instructions)):
        modified = copy.deepcopy(instructions)

        instruction = modified[attempt]
        operation = instruction[0]
        argument = instruction[1]

        if operation == "nop":
            modified[attempt] = ("jmp", argument)
            result = run_instructions(modified)
        elif operation == "jmp":
            modified[attempt] = ("nop", argument)
            result = run_instructions(modified)

        if infinite_loop == False:
            break;

    return result


def parse_instructions():
    instructions = []

    file = open('day8.dat', 'r')
    lines = file.readlines()
    for line in lines:
        parts = line.strip().split()
        # nop +402
        # jmp +570
        # acc -12

        operation = parts[0]
        argument = int(parts[1]) # will properly handle the +/- sign

        instructions.append((operation, argument))

    return instructions


def run_instructions(instructions):
    global infinite_loop

    next_instruction = 0
    accumulator = 0

    # Run until we get to a line number we've already executed
    infinite_loop = False
    line_numbers = set()
    while True:
        if next_instruction in line_numbers:
            infinite_loop = True
            break

        line_numbers.add(next_instruction)

        instruction = instructions[next_instruction]
        operation = instruction[0]
        argument = instruction[1]

        if operation == "acc":
            accumulator = accumulator + argument
            next_instruction = next_instruction + 1
        elif operation == "jmp":
            next_instruction = next_instruction + argument
        else: # operation == "nop"
            next_instruction = next_instruction + 1

        # We made it to the end of the program without hitting an infinite loop
        if next_instruction == len(instructions):
            break;

    return accumulator


main()