import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

   if line[0].isdigit():
        if line[5] == "answer" or line[5] == "comment":
            print(line[7], "\t", line[3])
        if line[5] == "question":
            print(line[0], "\t", line[3])
