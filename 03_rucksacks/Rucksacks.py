def main():

    # setup priorities
    lower_case = ord('a')
    upper_case = ord('A')

    char_priorities = {}

    for val in range(1, 27):
        char_priorities[lower_case] = val
        lower_case += 1

    for val in range(27, 53):
        char_priorities[upper_case] = val
        upper_case += 1

    priority_sum = 0

    with open("input.txt") as input:
        lines = input.readlines()

    # part 1
    for line in lines:
        stripped_line = line.strip()
        length = len(stripped_line)
        compartment1 = stripped_line[slice(0, length//2)]
        compartment2 = stripped_line[slice(length//2, length)]

        wrongly_packed_item = set(compartment1).intersection(set(compartment2)).pop()

        priority_sum += char_priorities[ord(wrongly_packed_item)]

    print("Priority Sum:")
    print(priority_sum)

    # part 2
    priority_sum = 0
    start_pos = 0

    def chunk3(lst):
        for i in range(0, len(lst), 3):
            yield lst[i:i+3]

    for line_group in chunk3(lines):
        start_pos += 3
        badge_item = set(line_group[0].strip()).intersection(set(line_group[1].strip())).intersection(set(line_group[2].strip())).pop()

        priority_sum += char_priorities[ord(badge_item)]

    print("Priority Sum:")
    print(priority_sum)

if __name__ == "__main__":
    main()