import sys
import csv

csv_reader = csv.reader(sys.stdin, delimiter="\t")
for line in csv_reader:
    # import pdb; pdb.set_trace()
    if len(line) == 19:
        body = line[4]
        print(body)