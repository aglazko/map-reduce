import sys

total_cost = 0
prev_item = None

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    if len(mapped_data) != 2:
        continue

    current_item, current_cost = mapped_data

    if prev_item and prev_item != current_item:
        print(prev_item, "\t", total_cost)
        total_cost = 0

    prev_item = current_item
    total_cost += float(current_cost)

if prev_item:
    print(prev_item, "\t", total_cost)
