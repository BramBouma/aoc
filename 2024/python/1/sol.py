def read():
    with open("input.txt", "r") as f:
        filel = f.readlines()

    return filel


def clean(input: list):
    mid = [x.split("   ") for x in input]

    for line in mid:
        line[1] = line[1].replace("\n", "")

    return mid


def get_counts(list_a, list_b):
    count_list = []
    for i in list_a:
        count = 0
        for j in list_b:
            if i == j:
                count += 1

        count_list.append(count)

    return count_list


if __name__ == "__main__":
    bl = read()
    t = clean(bl)

    left = [int(line[0]) for line in t]
    left.sort()
    right = [int(line[1]) for line in t]
    right.sort()

    dl = [abs(left[i] - right[i]) for i in range(len(left))]

    print("Part 1: ", sum(dl))

    lc = get_counts(left, right)
    sim_score = sum(x * y for x, y in zip(left, lc))

    print("Part 2: ", sim_score)
