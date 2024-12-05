from collections import defaultdict

rules = defaultdict(list)
updates = []
with open("input", "r") as file:
    for line in file:
        if "|" in line:
            (page_before, page_after) = map(int, line.split("|"))
            rules[page_before].append(page_after)

        elif "," in line:
            updates.append(list(map(int, line.strip().split(","))))

print(rules)
print(updates)

correct_updates = []
for update in updates:
    not_valid = False
    for entry_idx in range(len(update) - 1, -1, -1):
        if update[entry_idx] in rules:
            entries_to_check = set(update[0:entry_idx])
            if any(entry in entries_to_check for entry in rules[update[entry_idx]]):
                not_valid = True
                break

    if not not_valid:
        correct_updates.append(update)

print(correct_updates)

total_sum = 0
for update in correct_updates:
    total_sum += update[len(update) // 2]

print(total_sum)
