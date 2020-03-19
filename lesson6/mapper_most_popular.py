import sys

BASE_URL = "http://www.the-associates.co.uk"

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, nothing, nothing1, time, nothing2, action_code, url, http_version, return_code, size = data

        if url.find(BASE_URL) != -1:
            url = url[len(BASE_URL):]

        print("{0}\t{1}".format(url, size))