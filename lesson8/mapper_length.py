import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    # print(line[7])
    if line[0].isdigit():
        if line[5] == "answer":
            print(line[7], "A", len(line[4]))
        if line[5] == "question":
            print(line[0], "Q", len(line[4]))

