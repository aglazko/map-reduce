import sys

salesCount = 0
salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", salesCount, "\t", salesTotal)
        oldKey = thisKey
        salesCount = 0
        salesTotal = 0

    oldKey = thisKey
    salesCount += 1
    salesTotal += float(thisSale)

if oldKey != None:
    print(oldKey, "\t", salesCount, "\t", salesTotal)