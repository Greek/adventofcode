import os
from collections import Counter


def main():
    # Part 1
    location_ids1 = []
    location_ids2 = []

    total_distance = 0

    with open(f"{os.getcwd()}/input.txt", "r") as file:
        for line in file:
            nums = line.replace("\n", "").split()

            location_ids1.append(int(nums[0]))
            location_ids2.append(int(nums[1]))

    location_ids1.sort()
    location_ids2.sort()

    for i in range(len(location_ids1)):
        total_distance += abs(location_ids1[i] - location_ids2[i])

    # Part 2
    counts = Counter(location_ids2)
    similarity_score = sum(num * counts[num] for num in location_ids1)

    return total_distance, similarity_score


if __name__ == "__main__":
    result = main()
    print(result)
