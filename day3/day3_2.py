import re

DONT = "don't"
DO = "do"


def split_do_dont(text, do="do"):
    # split at first occurrence
    if do == "do":
        return re.split(r"do\(\)", text, 1)
    else:
        return re.split(r"don\'t\(\)", text, 1)


def find_multiplications(text):
    return re.findall(r"mul\(\d+,\d+\)", text)


def extract_numbers(mul):
    return [int(num) for num in re.findall(r"\d+", mul)]


split_memory = []
searched_instruction = DONT
with open('input', 'r') as corrupted_memory:
    for line in corrupted_memory:
        while True:
            print(line)
            if searched_instruction == DONT:
                spliiit = split_do_dont(line, DONT)

                if len(spliiit) == 1:
                    split_memory.append(find_multiplications(spliiit[0]))
                    break

                (text, line) = spliiit
                split_memory.append(find_multiplications(text))
                searched_instruction = DO

            elif searched_instruction == DO:
                spliiit = split_do_dont(line, DO)

                if len(spliiit) == 1:
                    break

                (_, line) = spliiit
                text = ""
                searched_instruction = DONT
            else:
                raise ValueError("Invalid instruction")

            # split_memory.append(find_multiplications(text))
            print(split_memory)

# print(line)
print(split_memory)

result = 0
for line in split_memory:
    for mul in line:
        (num1, num2) = extract_numbers(mul)
        print(num1, num2)
        result += num1 * num2

print(result)
