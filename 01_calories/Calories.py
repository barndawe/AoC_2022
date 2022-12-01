def main():
    elf_calories = [0]
    elf_idx = 0

    with open("input.txt") as input:
        lines = input.readlines()

    for line in lines:
        if line.strip() == "":
            elf_idx +=1
            elf_calories.append(0)
        else:
            elf_calories[elf_idx] += int(line)

    elf_calories.sort(reverse=True)

    print("Max elf calories:")
    print(elf_calories[0])

    print("Combined top 3 elf calories")
    print(elf_calories[0] + elf_calories[1] + elf_calories[2])

if __name__ == "__main__":
    main()