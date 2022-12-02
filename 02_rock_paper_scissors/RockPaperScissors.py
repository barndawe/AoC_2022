def main():
    rps_outcomes_part_1 = {
        "A X": 1 + 3, # rock vs rock - draw
        "A Y": 2 + 6, # rock vs paper - win
        "A Z": 3 + 0, # rock vs scissors - lose
        "B X": 1 + 0, # paper vs rock - lose
        "B Y": 2 + 3, # paper vs paper - draw
        "B Z": 3 + 6, # paper vs scissors - win
        "C X": 1 + 6, # scissors vs rock - win
        "C Y": 2 + 0, # scissors vs paper - lose
        "C Z": 3 + 3  # scissors vs scissors - draw
    }

    rps_outcomes_part_2 = {
        "A X": 0 + 3, # rock lose - scissors
        "A Y": 3 + 1, # rock draw - rock
        "A Z": 6 + 2, # rock win - paper
        "B X": 0 + 1, # paper lose - rock
        "B Y": 3 + 2, # paper draw - paper
        "B Z": 6 + 3, # paper win - scissors
        "C X": 0 + 2, # scissors lose - paper
        "C Y": 3 + 3, # scissors draw - scissors
        "C Z": 6 + 1  # scissors win - rock
    }

    total_score_part_1 = 0
    total_score_part_2 = 0

    with open("input.txt") as input:
        lines = input.readlines()

    for line in lines:
       line = line.strip()
       total_score_part_1 += rps_outcomes_part_1[line]
       total_score_part_2 += rps_outcomes_part_2[line]

    print("Total score part 1:")
    print(total_score_part_1)

    print("Total score part 2:")
    print(total_score_part_2)

if __name__ == "__main__":
    main()