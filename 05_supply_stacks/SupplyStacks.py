from typing import Dict, List
import re
from parse import *


def main():
    
    with open("input.txt") as input:
        lines = input.readlines()

    # i'm assuming that if there's ever more than 9 stacks they keep to the same width
    # (i.e 4 chars per stack item, except for the last where there's 3)
    stacks: Dict[int, List[str]] = {}
    num_stacks = (len(lines[0].strip())//4) + 1 # add 1 for the final 3 char line

    for stack_num in range(1,num_stacks+1):
        stacks[stack_num] = []

    for index, line in enumerate(lines):
        # the first line that has no square brackets is the stack number line
        if  "[" not in line:
            stack_nums_line_index = index
            break

    #build the crate stacks from the bottom up
    for stack_line in lines[stack_nums_line_index - 1:: -1]:
        for stack_num in range(1, num_stacks + 1):
            crate = re.sub("[^A-Za-z]", "", stack_line[(stack_num - 1) * 4: stack_num * 4])
            if not crate == "":
                stacks[stack_num].append(crate)

    first_move_index = stack_nums_line_index + 2

    for move_line in lines[first_move_index:]:
        count, from_stack, to_stack = parse("move {} from {} to {}", move_line)
        mover9001(stacks, int(count), int(from_stack), int(to_stack))

    stack_top = ""

    for stack in stacks.values():
        stack_top += stack.pop()

    print(stack_top)

def mover9000(stacks: Dict[int, List[str]], count: int, from_stack: int, to_stack: int):
    for _ in range(count):
        stacks[to_stack].append(stacks[from_stack].pop())

def mover9001(stacks: Dict[int, List[str]], count: int, from_stack: int, to_stack: int):
    transfer = stacks[from_stack][len(stacks[from_stack]) - count:]
    stacks[to_stack].extend(transfer)
    stacks[from_stack] = stacks[from_stack][:len(stacks[from_stack]) - count]
    print(stacks[from_stack])

if __name__ == "__main__":
    main()