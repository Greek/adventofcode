import os


def main():
    location_ids1 = []
    location_ids2 = []

    total_distance = 0

    with open(f"{os.getcwd()}/input.txt", "r") as input:
        for line in input:
            nums = line.replace("\n", "").split()

            location_ids1.append(int(nums[0]))
            location_ids2.append(int(nums[1]))

    location_ids1.sort()
    location_ids2.sort()

    for i in range(0, len(location_ids1)):
        total_distance += abs(location_ids1[i] - location_ids2[i])

    return total_distance


if __name__ == "__main__":
    result = main()
    print(result)
