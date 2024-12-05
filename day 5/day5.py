rules = {}
updates = []
with open("input", "r") as file:
    for line in file:
        if "|" in line:
            (page_bofore, page_after) = line.split("|")

            # add page_before to rules
            page_before = int(page_bofore.strip())
            page_after = int(page_after.strip())
            if page_before not in rules:
                rules[page_before] = [page_after]
            else:
                rules[page_before].append(page_after)

        elif "," in line:
            updates.append([int(l) for l in line.strip().split(",")])

print(rules)
print(updates)

correct_updates = []
for update in updates:
    not_correct = False
    for entry_idx in range(len(update) - 1, -1, -1):
        # print(update[entry_idx])
        if update[entry_idx] in rules:
            entries_to_check = update[0:entry_idx]
            for entry in rules[update[entry_idx]]:
                if entry in entries_to_check:
                    not_correct = True
                    break

    if not not_correct:
        correct_updates.append(update)

print(correct_updates)

summm = 0
for update in correct_updates:
    summm += update[len(update)//2]

print(summm)
