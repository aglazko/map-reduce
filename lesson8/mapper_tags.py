import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    if line[0].isdigit():
        if line[5] == "question":
            tags = line[2].strip().split()
            for word in tags:
                word = word.lower()
                print("{0}\t{1}".format(word, "1"))
