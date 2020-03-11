import sys
#
# salesCount = 0
# salesTotal = 0
# oldKey = None
#
# for line in sys.stdin:
#     data_mapped = line.strip().split("\t")
#     if len(data_mapped) != 2:
#         continue
#
#     thisKey, thisSale = data_mapped
#
#     if oldKey and oldKey != thisKey:
#         print(oldKey, "\t", salesCount, "\t", salesTotal)
#         oldKey = thisKey
#         salesCount = 0
#         salesTotal = 0
#
#     oldKey = thisKey
#     salesCount += 1
#     salesTotal += float(thisSale)
#
# if oldKey != None:
#     print(oldKey, "\t", salesCount, "\t", salesTotal)

total_cost = 0
counter = 0
prev_store = 0
for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    if len(mapped_data) != 2:
        continue
    current_store, current_cost = mapped_data
    if not prev_store:
        prev_store = current_store
        total_cost = float(current_cost)
        counter += 1
    if prev_store:
        total_cost += float(current_cost)
        counter += 1
print(total_cost, "\t", counter)
