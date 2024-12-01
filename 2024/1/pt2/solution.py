from collections import Counter

def main():
    location_ids1 = []
    location_ids2 = []


    total_distance = 0

    with open(
        f"{os.getcwd()}/input.txt", "r"
    ) as input:
        for line in input:
            nums = line.replace("\n", "").split()

            location_ids1.append(int(nums[0]))
            location_ids2.append(int(nums[1]))

    counts = Counter(location_ids2)
    similarity_score = sum(num * counts[num] for num in location_ids1)

    for i in range(0, len(location_ids1)):
        location_ids1.sort()
        location_ids2.sort()

        curr1 = location_ids1[i]
        curr2 = location_ids2[i]

        total_distance += abs(curr1 - curr2)

    return total_distance, similarity_score


if __name__ == "__main__":
    result = main()
    print(result)
