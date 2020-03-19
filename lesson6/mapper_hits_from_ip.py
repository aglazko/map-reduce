import sys

for line in sys.stdin:
    data = line.strip().split()
    ip = data[0]
    size = data[len(data) - 1]
    if len(data) == 10:
        print("{0}\t{1}".format(ip, size))