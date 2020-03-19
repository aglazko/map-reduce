"""Task: Find the monetary value for the highest individual sale for each separate store. Input file purchases.txt,
reducer: reducer_highest_sale.py"""
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    store = data[2]
    cost = data[4]
    print("{0}\t{1}".format(store, cost))