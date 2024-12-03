import re


def find_multiplications(text):
    return re.findall(r"mul\(\d+,\d+\)", text)


def extract_numbers(mul):
    return [int(num) for num in re.findall(r"\d+", mul)]


split_memory = []
with open('input', 'r') as corrupted_memory:
    for line in corrupted_memory:
        split_memory.append(find_multiplications(line))

# print(line)
print(split_memory)

result = 0
for line in split_memory:
    for mul in line:
        (num1, num2) = extract_numbers(mul)
        print(num1, num2)
        result += num1 * num2

print(result)