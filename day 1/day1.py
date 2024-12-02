# Initialize empty lists
list1 = []
list2 = []

# Open the file and process each line
with open('input1', 'r') as file:
    for line in file:
        # Split the line into two numbers and append to respective lists
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

print("list1 =", list1)
print("list2 =", list2)

totalDist = 0
for (a, b) in zip(sorted(list1), sorted(list2)):
    totalDist += abs(b - a)

print(totalDist)

