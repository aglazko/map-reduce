import sys
prev_key = 0
count_of_hours = {}
res = {}
hours = []

for line in sys.stdin:
    mapped_data = line.strip().split('\t')
    if len(mapped_data) != 2:
        continue
    user_id, post_hour = mapped_data
    current_key = user_id
    if prev_key and prev_key != current_key:
        max_val = max(count_of_hours.values())
        for item in count_of_hours:
            if count_of_hours[item] == max_val:
                print(prev_key, '\t', item)
        #         hours.append(item)
        count_of_hours = {}
        # res[prev_key] = hours
        # hours = []
        # if len(res[prev_key]) == 1:
        #     print(prev_key, '\t', res[prev_key])
        #     res.pop(prev_key)
        prev_key = current_key
    if not prev_key:
        prev_key = current_key
    if prev_key and prev_key == current_key:
        if post_hour in count_of_hours.keys():
            count_of_hours[post_hour] += 1
        else:
            count_of_hours[post_hour] = 1
max_val = max(count_of_hours.values())
for item in count_of_hours:
    if count_of_hours[item] == max_val:
        print(prev_key, '\t', item)
# print(res)
