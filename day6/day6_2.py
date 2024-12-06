all_lines = []
start_position = [0, 0]
direction = "up"

with open("input1", "r") as file:
    for indx, line in enumerate(file):
        if "^" in line:
            start_position[0] = indx
            start_position[1] = line.index("^")
        all_lines.append(list(line.strip()))
print(start_position)


def take_a_step(current_position, direction, rotate_right=False):
    # print(current_position, direction)
    if rotate_right:
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        elif direction == "left":
            direction = "up"

    if direction == "up":
        potential_position = [current_position[0] - 1, current_position[1]]
    elif direction == "down":
        potential_position = [current_position[0] + 1, current_position[1]]
    elif direction == "left":
        potential_position = [current_position[0], current_position[1] - 1]
    elif direction == "right":
        potential_position = [current_position[0], current_position[1] + 1]

    if potential_position[0] < 0 or potential_position[1] < 0 or potential_position[0] >= len(all_lines) or \
            potential_position[1] >= len(all_lines[0]):
        print(len(all_lines), len(all_lines[0]))
        return current_position, direction, "end"

    if all_lines[potential_position[0]][potential_position[1]] == "#":
        return take_a_step(current_position, direction, rotate_right=True)
    else:
        all_lines[current_position[0]][current_position[1]] = "X"
        visited[current_position[0]][current_position[1]] += 1
        if visited[current_position[0]][current_position[1]] > 10:
            return potential_position, direction, "loop"
        return potential_position, direction, "continue"


status = "continue"
current_position = start_position
visited = [[0 for _ in range(len(all_lines[0]))] for _ in range(len(all_lines))]
while status == "continue":
    current_position, direction, status = take_a_step(current_position, direction)

obstacle_positions = []
for indx, line in enumerate(all_lines):
    for indx2, char in enumerate(line):
        if char == "X":
            obstacle_positions.append([indx, indx2])

print(obstacle_positions)

loops = 0
for new_obstacle_position in obstacle_positions:
    visited = [[0 for _ in range(len(all_lines[0]))] for _ in range(len(all_lines))]
    all_lines[new_obstacle_position[0]][new_obstacle_position[1]] = "#"
    current_position = start_position
    direction = "up"
    status = "continue"
    while True:
        current_position, direction, status = take_a_step(current_position, direction, False)
        if status == "loop":
            loops += 1
            # print("loop")
            # print(new_obstacle_position)
            # for line in all_lines:
            #     print(line)
            break
        elif status == "end":
            break
    all_lines[new_obstacle_position[0]][new_obstacle_position[1]] = "X"

for line in all_lines:
    print(line)
print(loops)
