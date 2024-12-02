reports = []

with open('input1', 'r') as file:
    for line in file:
        reports.append(list(map(int, line.split())))

print("reports =", reports)


def is_increasing(report):
    if report == list(sorted(report)):
        for level in range(1, len(report)):
            if report[level] - report[level - 1] > 3 or report[level] - report[level - 1] < 1:
                return False
        return True
    return False


def is_decreasing(report):
    if report == list(sorted(report, reverse=True)):
        for level in range(1, len(report)):
            if report[level - 1] - report[level] > 3 or report[level - 1] - report[level] < 1:
                return False
        return True
    return False


# check each report if it is increasing or decreasing
validReports = 0

for report in reports:
    validReport = False

    if report == list(sorted(report)):
        validReport = is_increasing(report)

    elif report == list(sorted(report, reverse=True)):
        validReport = is_decreasing(report)

    if not validReport:
        # check if removing any element will make the report valid
        for i in range(len(report)):
            if is_increasing(report[:i] + report[i + 1:]) or is_decreasing(report[:i] + report[i + 1:]):
                validReport = True
                break

    if validReport:
        print(report)
        validReports += 1

print(validReports)
