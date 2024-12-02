reports = []

with open('input1', 'r') as file:
    for line in file:
        reports.append(list(map(int, line.split())))

print("reports =", reports)

# check each report if it is increasing or decreasing
validReports = 0

for report in reports:
    validReport = False

    if report == list(sorted(report)):
        print("report is increasing", report)
        validReport = True
        # check if difference between each number is at most 3 and at least 1
        for i in range(1, len(report)):
            if report[i] - report[i - 1] > 3 or report[i] - report[i - 1] < 1:
                validReport = False
                break

    elif report == list(sorted(report, reverse=True)):
        print("report is decreasing", report)
        validReport = True
        # check if difference between each number is at most 3
        for i in range(1, len(report)):
            if report[i - 1] - report[i] > 3 or report[i - 1] - report[i] < 1:
                validReport = False
                break

    if validReport:
        print(report)
        validReports += 1

print(validReports)
