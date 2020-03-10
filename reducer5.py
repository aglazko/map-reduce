import sys

count = 0
oldKey = None


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", count)
        oldKey = thisKey
        count = 0

    oldKey = thisKey
    count += 1

if oldKey:
    print(oldKey, "\t", count)