import sys
import csv

csv_reader = csv.reader(sys.stdin, delimiter='\t')
for line in csv_reader:
    # print(line)
    if len(line) == 19:
        body = line[4].replace("<br>", "")
        res = body.strip().replace("\n", " ")
        # res1 = body.replace("\n", " ")
        # last_res = res1.replace("")
        if line[0].isdigit():
            id_b = line[0]
            print("{0}    {1}".format(id_b, res))
        else:
            continue

    # if len(line) == 19:
    #     # print(line)
    #     body = line[4]
    #     # print(body)
    #     # if "\\N" in body:
    #     #     body.
    #     if line[0].isdigit():
    #         id = line[0]
    #     else:
    #         id = None
    #     # id = line[0]
    #     # print(body)
    #     print(id, body)