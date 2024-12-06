all_lines = []
current_position = [0, 0]
direction = "up"

with open("input1", "r") as file:
    for indx, line in enumerate(file):
        if "^" in line:
            current_position[0] = indx
            current_position[1] = line.index("^")
        all_lines.append(list(line.strip()))
print(current_position)

def take_a_step(current_position, direction, rotate_right=False):
    print(current_position, direction)
    # direction = "right" if rotate_right else "up"
    # direction = "left" if rotate_right else "down"
    # direction = "up" if rotate_right else "left"
    # direction = "down" if rotate_right else "right"
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
        return potential_position, direction, "continue"


status = "continue"
while status == "continue":
    current_position, direction, status = take_a_step(current_position, direction)

print(all_lines)

total_steps = 0
for line in all_lines:
    total_steps += line.count("X")

print(total_steps+1)
for step in all_lines:
    print("".join(step))