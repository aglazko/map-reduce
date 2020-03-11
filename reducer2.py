import sys

biggestSale = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

# for line in sys.stdin:
#     data_mapped = line.strip().split("\t")
#     if len(data_mapped) != 2:
#         # Something has gone wrong. Skip this line.
#         continue
#
#     thisKey, thisSale = data_mapped
#
#     if oldKey and oldKey != thisKey:
#         print(oldKey, "\t", biggestSale)
#         oldKey = thisKey
#         biggestSale = float(thisSale)
#
#     oldKey = thisKey
#     if float(thisSale) > biggestSale:
#         biggestSale = float(thisSale)
#
#
# if oldKey:
#     print(oldKey, "\t", biggestSale)

# res = {}
# old_store = 0
# biggest_sale = 0
# for line in sys.stdin:
#     mapped_data = line.strip().split("\t")
# #     if current_store not in res.keys():
# #         res[current_store] = current_sale
# #     if current_store in res.keys() and res[current_store] < current_sale:
# #         res[current_store] = current_sale
# # for item in res:
# #     print(item, res[item])
#     if len(mapped_data) != 2:
#         continue
#     current_store, current_sale = mapped_data
#     if old_store and old_store != current_store:
#         print(old_store, "\t", biggest_sale)
#         old_store = current_store
#         biggest_sale = float(current_sale)
#     old_store = current_store
#     if float(current_sale) > float(biggest_sale):
#         biggest_sale = current_sale
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
        # else:
        #     prev_store = current_store
    if prev_store and prev_store != current_store:
        print(prev_store, "\t", float(biggest_cost))
        prev_store = current_store
        biggest_cost = float(current_cost)






