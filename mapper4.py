import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, nothing, nothing, time, nothing, action_code, url, http_version, return_code, size = data
        print("{0}\t{1}".format(url, size))