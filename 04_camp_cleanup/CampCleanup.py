from typing import List


def main():
    
    with open("input.txt") as input:
        lines = input.readlines()
    
    fully_contained_ranges = 0
    overlapping_ranges = 0

    for line in lines:
        ranges = line.strip().split(",")
        set1 = range_to_set(ranges[0])
        set2 = range_to_set(ranges[1])

        if set1.issubset(set2) or set2.issubset(set1):
            fully_contained_ranges += 1

        if len(set1.intersection(set2)) > 0:
            overlapping_ranges += 1

    print("Fully-contained ranges")
    print(fully_contained_ranges)

    print("Overlapping ranges")
    print(overlapping_ranges)


def range_to_set(num_range:str) -> set:
    nums = num_range.split("-")
    return set(list(range(int(nums[0]), int(nums[1]) +1)))

if __name__ == "__main__":
    main()