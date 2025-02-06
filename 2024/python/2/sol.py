def read_input():
    report_list = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            int_line = []
            for i in line.split():
                int_line.append(int(i))

            report_list.append(int_line)

    return report_list


def check(report: list):
    if len(report) != len(set(report)):
        return False
    else:
        pass

    inc = [report[i] < report[i + 1] for i in range(len(report) - 1)]
    if any(inc) and not all(inc):
        return False
    else:
        pass

    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) > 3:
            return False
        else:
            continue

    return True


def dampened(report):
    if check(report):
        return True
    else:
        pass

    for i in range(len(report)):
        t_report = report[:i] + report[i+1:]

        if check(t_report):
            return True
        else:
            continue

    return False


if __name__ == "__main__":
    rl = read_input()

    sl = [check(r) for r in rl]
    n_safe = sum(sl)

    print("Part 1: ", n_safe)

    sld = [dampened(r) for r in rl]
    n_safed = sum(sld)

    print("Part 2: ", n_safed)
