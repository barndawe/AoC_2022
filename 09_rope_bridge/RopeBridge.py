from enum import Enum
from typing import List, Set, Tuple
from Point import Point

def main():

    with open("input.txt") as input:
        lines = input.readlines()

    #NUM_KNOTS = 2
    NUM_KNOTS = 10

    knots: List[Point] = []
    unique_knot_positions: List[Set[Point]] = []

    for _ in range(0, NUM_KNOTS):
        # all knots start at 0,0
        knots.append(Point(0,0))
        unique_knot_positions.append(set())

    for line in lines:
        direction, distance = parse_line(line)
        # loop through number of moves
        for _ in range(0, distance):
            # move the first knot
            move_head(knots[0], direction)
            unique_knot_positions[0].add(Point(knots[0].x, knots[0].y))

            # move all subsequent knots one at a time
            for knot_num in range(1, NUM_KNOTS):
                move_tail(knots[knot_num-1], knots[knot_num])

                # add the latter knot's position to its set
                unique_knot_positions[knot_num].add(Point(knots[knot_num].x, knots[knot_num].y))

    print(len(unique_knot_positions.pop()))

def move_head(head: Point, direction: str):
    match direction:
        case "U":
            head.move(0, 1)
        case "D":
            head.move(0, -1)
        case "L":
            head.move(-1, 0)
        case "R":
            head.move(1,0)

def move_tail(head: Point, tail: Point):
    difx = head.x - tail.x
    dify = head.y - tail.y

    tail_h = 0
    tail_v = 0

    if difx == 2:
        tail_h = 1
        if dify > 0:
            tail_v = 1
        if dify < 0:
            tail_v = -1
    if difx == -2:
        tail_h = -1
        if dify > 0:
            tail_v = 1
        if dify < 0:
            tail_v = -1
    if dify == 2:
        tail_v = 1
        if difx > 0:
            tail_h = 1
        if difx < 0:
            tail_h = -1
    if dify == -2:
        tail_v = -1
        if difx > 0:
            tail_h = 1
        if difx < 0:
            tail_h = -1

    tail.move(tail_h, tail_v)

def parse_line(line: str)-> Tuple[str, int]:
    direction = line[0:1]
    distance = int(line.strip()[2:])

    return (direction, distance)

if __name__ == "__main__":
    main()
