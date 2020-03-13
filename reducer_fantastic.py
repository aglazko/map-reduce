import sys
import re
counter = 0
word = re.compile(r'\b({0})\b'.format("fantastic"), flags=re.IGNORECASE)
id_list = []
for line in sys.stdin:
    if line:
        data = line.strip("").split(" ")
        for item in data:
            # item = item.strip("<br>")
            if re.search(word, item):
                counter += 1
            # print(item)
        # print(data)

print(counter)
