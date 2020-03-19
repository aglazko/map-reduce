import sys
import re
word = re.compile(r'\b({0})\b'.format("fantastically"), flags=re.IGNORECASE)
id_list = []
for line in sys.stdin:
    res = line.strip("\n").split("    ")
    # print(res)
    if len(res) != 2:
        continue
    id_f, data = res
    if re.search(word, data):
        if id_f and id_f not in id_list:
            id_list.append(int(id_f))
id_list = sorted(id_list)
print(id_list)