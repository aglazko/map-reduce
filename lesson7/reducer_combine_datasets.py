#!/usr/bin/python
import sys


def reducer():
    prev_key = 0
    users = {}
    nodes = []
    for line in sys.stdin:
        mapped_data = line.strip().split("\t")
        if len(mapped_data) < 6 or len(mapped_data) >  10:
            continue
        current_key = mapped_data[0]
        if prev_key:
            if prev_key == current_key:
                if mapped_data[-1] == 'A':
                    mapped_data.pop()
                    if prev_key not in users.keys():
                        users[prev_key] = mapped_data[1:]
                    else:
                        continue
                if mapped_data[-1] == 'B':
                    mapped_data.pop()
                    if prev_key in users.keys():
                        # print("res")
                        print('')
                        print(prev_key, end=" ")
                        for item in mapped_data[1:]:
                            print(item, end=" ")
                        for item in users[prev_key][1:]:
                            print(item, end=' ')
                    else:
                        nodes.append(mapped_data)
            if prev_key != current_key:
                if prev_key in users.keys() and nodes:
                    for item in nodes:
                        print('')
                        print(prev_key, end=' ')
                        for node in item[1:]:
                            print(node, end=' ')
                        for i in users[prev_key]:
                            print(i, end=' ')
                prev_key = current_key
                nodes = []
                users = {}
                if mapped_data[-1] == 'A':
                    mapped_data.pop()
                    users[current_key] = mapped_data[1:]
                if mapped_data[-1] == 'B':
                    mapped_data.pop()
                    nodes.append(mapped_data)
        else:
            prev_key = current_key
            if mapped_data[len(mapped_data)-1] == 'A':
                mapped_data.pop()
                users[current_key] = mapped_data[1:]
            if mapped_data[len(mapped_data)-1] == 'B':
                mapped_data.pop()
                nodes.append(mapped_data)












        # mapped_data.pop()
        # print(mapped_data)
        # if prev_key and prev_key != current_key:
        #     if prev_key in users.keys():
        #         print(nodes, users[prev_key])
        #         prev_key = current_key
        #         nodes = []
        #     else:
        #         print("sorry", nodes)
        #         prev_key = current_key
        # if prev_key and prev_key == current_key:
        #     if prev_key in users.keys():
        #         print(mapped_data, users[current_key])
        #     else:
        #         nodes.append(mapped_data)
        # if mapped_data[len(mapped_data)-1] == 'A':
        #     # print(mapped_data)
        #     mapped_data.pop()
        #     if current_key not in users.keys():
        #         users[current_key] = mapped_data[1:]
        # if mapped_data[len(mapped_data)-1] == 'B':
        #     # print(mapped_data)
        #     mapped_data.pop()
        #     if prev_key and prev_key != current_key:
        #         if prev_key in users.keys():
        #             print(nodes, users[prev_key])
        #             prev_key = current_key
        #         else:
        #             print("sorry", nodes)
        #     if prev_key and
        # current_key = mapped_data[0]
        # # print(users)
        # if not prev_key:
        #     prev_key = current_key
        # if len(mapped_data) == 5 and (mapped_data[0] not in users.keys()):
        #     users[current_key] = [item for item in mapped_data[1:]]
        # if len(mapped_data) == 9:
        #     if current_key == prev_key:
        #         if current_key in users.keys():
        #             for item in mapped_data[1:4]:
        #                 print(item, end=" ")
        #             print(current_key)
        #             for item in mapped_data[4:]:
        #                 print(item, end=" ")
        #             for item in users[current_key]:
        #                 print(item, end=" ")
        #         if current_key not in users.keys():
        #             nodes.append([item for item in mapped_data[1:]])
        #     if current_key != prev_key and prev_key in users.keys():
        #         for item in nodes:
        #             for node in item:
        #                 print(node[:4], end=" ")
        #                 print(item, end=" ")
        #                 print(node[4:])
        #                 print(users[current_key])
        #                 nodes.remove(item)
        # if prev_key and current_key != prev_key:
        #     for item in nodes:
        #         for node in item:
        #             print(node[:4], end=" ")
        #             print(item, end=" ")
        #             print(node[4:])
        #             for item in users[current_key]:
        #                 print(item)
        #             prev_key = current_key
        #             users.clear()



        # print(mapped_data[0])
        # print(mapped_data)
        # if len(mapped_data) < 5 or len(mapped_data) > 9:
        #     continue
        #
        # if len(mapped_data) == 5 and (mapped_data[0] not in users.keys()):
        #     # print(mapped_data[0])
        #     users[mapped_data[0]] = [item for item in mapped_data[1:]]
        # if len(mapped_data) == 9:
        #     # print(mapped_data, "l", users.keys())
        #     if mapped_data[0] in users.keys():
        #         print("res", mapped_data[1:4], end=" ")
        #         print(mapped_data[0], end=" ")
        #         print(mapped_data[4:], end=" ")
        #         print(users[mapped_data[0]])
        #         print(nodes)
        #
        #     else:
        #         nodes[mapped_data[0]] = [item for item in mapped_data[1:]]

    # print(users)



reducer()
