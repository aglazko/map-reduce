#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if not line[0].isdigit():
        continue
    auth_id = line[3]
    post_date = line[8].split(' ')
    post_time = (post_date[1].split(':'))[0]
    if len(line) != 19:
        continue
    else:
        print('{}\t{}'.format(auth_id, post_time))