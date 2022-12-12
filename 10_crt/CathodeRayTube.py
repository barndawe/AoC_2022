from typing import List, Tuple

def main():
    with open("input.txt") as input:
        lines = input.readlines()

    # register starts at 1
    x_register = 1
    signal_strength = 0
    cycle = 0
    addx_second_cycle = False

    output_buffer: List[str] = []
    output_line: str = ""

    for line in lines:
        instruction, instr_cycles, value = parse_instruction(line)

        for _ in range(0, instr_cycles):
            output_line_position = cycle % 40

            # clear the line into the buffer
            if output_line_position == 0:
                output_buffer.append(output_line[:])
                output_line = ""

            if output_line_position in range(x_register - 1, x_register + 2):
                output_line += "#"
            else:
                output_line += "."


            cycle +=1

            if (cycle - 20) % 40 == 0:
                signal_strength += x_register * cycle

            if instruction == "addx" and not addx_second_cycle:
                addx_second_cycle = True
            elif instruction == "addx" and addx_second_cycle:
                addx_second_cycle = False
                x_register += value

    output_buffer.append(output_line[:])

    print(signal_strength)
    for line in output_buffer:
        print(line)



def parse_instruction(line: str)-> Tuple[str, int, int]:
    instruction = line[0:4]

    if instruction == "addx":
        value = int(line.strip()[4:])
        instr_cycles = 2
    else:
        value = ""
        instr_cycles = 1

    return (instruction, instr_cycles, value)

if __name__ == "__main__":
    main()