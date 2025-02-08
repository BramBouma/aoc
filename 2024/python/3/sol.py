import re


def read_input():
    with open("input.txt") as f:
        inp = f.read()

    return inp


def search(input_string):
    regex_pattern = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"
    search_result = re.findall(regex_pattern, input_string)

    return search_result


# mul string must be some form of "mul\([0-9]{0,3},[0-9]{0,3}\)"
def mul(mul_string):
    regex_pattern = "[0-9]{0,3},[0-9]{0,3}"
    x, y = re.findall(regex_pattern, mul_string)[0].split(",")

    return int(x) * int(y)


def filter_cond(input_string):
    regex_pattern = r"(?:^|do\(\))(.*?)(?=don't\(\)|$)"
    matches = re.findall(regex_pattern, input_string, re.DOTALL)

    filtered = "".join(matches)
    return filtered


if __name__ == "__main__":
    inst = read_input()
    res = search(inst)

    print("Part 1: ", sum([mul(i) for i in res]))

    cond = filter_cond(inst)
    filres = search(cond)

    print("Part 2: ", sum([mul(i) for i in filres]))
