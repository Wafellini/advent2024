import re


def count_xmas(text):
    return len(re.findall("XMAS", text))


def find_diagonals(row, col, diagonal_list, increment_row=1, increment_col=1):
    diagonal = ""
    while True:
        try:
            print(row, col, "coo")
            if row < 0 or col < 0:
                diagonal_list.append(diagonal)
                break
            diagonal += all_lines[row][col]
            row += increment_row
            col += increment_col
        except IndexError:
            print(row, col, "XDD")
            diagonal_list.append(diagonal)
            return


total_xmas = 0

all_lines = []
with open("input1", "r") as file:
    for line in file:
        all_lines.append(line)

# print(len(all_lines), len(all_lines[0]))
vertical_lines = ["".join(line[col] for line in all_lines) for col in range(len(all_lines[0]) - 1)]

diagonal_back = []
diagonal_forward = []
for column in range(len(all_lines[0])):
    row = 0
    col = column
    find_diagonals(row, col, diagonal_forward)
    # row_back = len(all_lines[0])
    print(row, col)
    find_diagonals(row, col, diagonal_back, 1, -1)

for roww in range(1, len(all_lines)):
    row = roww
    col = 0
    find_diagonals(row, col, diagonal_forward)
    col_back = len(all_lines)
    find_diagonals(row, col_back, diagonal_back, 1, -1)

print(diagonal_forward)
print(diagonal_back)

all_lines += vertical_lines
all_lines += diagonal_back
all_lines += diagonal_forward

reversed_all_lines = []
for line in all_lines:
    reversed_all_lines.append(line[::-1])

all_lines += reversed_all_lines
for line in all_lines:
    total_xmas += count_xmas(line)

print(total_xmas)
