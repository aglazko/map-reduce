import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

prev_tag = 0
result = []
total_count = 0

for line in reader:
    # print(line)
    current_tag, count = line
    # print(tag)
    # print(len(result))
    if prev_tag and prev_tag != current_tag:
        if len(result) < 10:
            result.append((prev_tag, total_count))
            result.sort(key=lambda num:num[1])
        else:
            if result[0][1] < total_count:
                result.pop(0)
                result.append((prev_tag, total_count))
                result.sort(key=lambda num: num[1])
        total_count = 0
    prev_tag = current_tag
    total_count += 1

if prev_tag:
    if len(result) < 10:
        result.append((prev_tag, total_count))
        result.sort(key=lambda num: num[1])
        result.reverse()
    else:
        if result[0][1] < total_count:
            result.pop(0)
            result.append((prev_tag, total_count))
            result.sort(key=lambda num: num[1])
            result.reverse()

for item in result:
    print(item)
