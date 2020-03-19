#!/usr/bin/python
import sys
import csv

res_dict_users = {}
res_dict_node = {}


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 5:
            if line[0].isdigit():
                for item in line:
                    print("{}".format(item), end="\t")
                print("A")

        if len(line) > 19:
            for item in line[:4]:
                print("{}".format(item), end="\t")
            for item in line[4]:
                if item.isdigit():
                    print("{}".format(item), end='')
            print("\tA")
        if len(line) == 19:
            if line[0].isdigit():
                print("{}".format(line[3]), end='\t')
                for item in line[:3]:
                    print("{}".format(item), end="\t")
                for item in line[5:10]:
                    print("{}".format(item), end="\t")

            print("B")

mapper()
