"""Task: Give salesbreakdown by product category across all of stores. Input file purchases.txt,
reducer: reducer_sales_per_category.py"""
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        # date, time, store, item, cost, payment = data
        item = data[3]
        cost = data[4]
        print("{0}\t{1}".format(item, cost))