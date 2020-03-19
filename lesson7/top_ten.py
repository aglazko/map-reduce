#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    res = {}
    res_list = []
    for line in reader:
        for item in line:
            if item:
                new_line = str(item)
                res[len(new_line)] = line
    while res and len(res_list) != 10:
        max_key_val = max(res.keys())
        res_list.append(res[max_key_val])
        res.pop(max_key_val)
    res_list.reverse()
    for item in res_list:
        writer.writerow(item)


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""


# This function allows you to test the mapper with the provided test string
def main():
    from io import StringIO
    sys.stdin = StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__


main()
