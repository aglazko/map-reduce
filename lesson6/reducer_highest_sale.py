import sys

prev_store = 0
prev_cost = 0
biggest_cost = 0

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    if len(mapped_data) != 2:
        continue
    current_store, current_cost = mapped_data
    if not prev_store:
        prev_store = current_store
        biggest_cost = float(current_cost)
    if prev_store and prev_store == current_store:
        if float(current_cost) > float(biggest_cost):
            biggest_cost = float(current_cost)
            prev_store = current_store
    if prev_store and prev_store != current_store:
        print(prev_store, "\t", float(biggest_cost))
        prev_store = current_store
        biggest_cost = float(current_cost)






