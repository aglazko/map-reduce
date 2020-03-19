import sys
import re
#
# # for line in sys.stdin:
# #     data = line.strip().split()
# #     if len(data) == 10:
# #         ip, nothing, nothing, time, nothing, action_code, url, http_version, return_code, size = data
# #         print("{0}\t{1}".format(url, size))
# counter = 0
# with open("purchases1.txt") as my_file:
#     for line in my_file.readlines():
#         result = re.split(r'[/]', line, maxsplit=3)
#         # print(result[3])
#         mapped_data = result[3].strip().replace('"', "")
#         print("/assets/js/the-associates.js")
#         # import pdb; pdb.set_trace()
#         # print(mapped_data)
#         if mapped_data.find("/assets/js/the-associates.js") != -1:
#             counter += 1
#
#
# print(counter)
# # for line in sys.stdin:
# #     result = re.split(r'[/]', line, maxsplit=3)
# #     print(result[3])
import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, nothing, nothing1, time, nothing2, action_code, url, http_version, return_code, size = data
        print("{0}\t{1}".format(url, size))