all_lines = []
with open("input1", "r") as file:
    for line in file:
        all_lines.append(list(line.strip()))

grids = []
# 3x3 grids
for row in range(0, len(all_lines) - 2):
    for col in range(0, len(all_lines[0]) - 2):
        grids.append([[all_lines[row][col], all_lines[row][col + 1], all_lines[row][col + 2]],
                      [all_lines[row + 1][col], all_lines[row + 1][col + 1], all_lines[row + 1][col + 2]],
                      [all_lines[row + 2][col], all_lines[row + 2][col + 1], all_lines[row + 2][col + 2]]])

# check
# M.S
# .A.
# M.S
mmass_count = 0
for grid in grids:
    if grid[1][1] == "A":

        top_left, top_right = grid[0][0], grid[0][2]
        bottom_left, bottom_right = grid[2][0], grid[2][2]

        if (top_left == top_right == "M" and bottom_left == bottom_right == "S") or \
                (top_left == bottom_left == "M" and top_right == bottom_right == "S") or \
                (top_left == top_right == "S" and bottom_left == bottom_right == "M") or \
                (top_left == bottom_left == "S" and top_right == bottom_right == "M"):
            mmass_count += 1

print(mmass_count)
