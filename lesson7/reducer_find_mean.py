import sys

prev_key = 0
counter = 0
res = 0
final_res = 0

for line in sys.stdin:
    mapped_data = line.strip().split("-")
    if len(mapped_data) != 2:
        continue
    current_weekday, current_sale = mapped_data
    if not prev_key:
        prev_key = current_weekday
        res = float(current_sale)
        counter = 1
        # print(prev_key, res)
    elif prev_key and prev_key == current_weekday:
        counter += 1
        res += float(current_sale)
        prev_key = current_weekday
        # print("reeee", prev_key, res)
    elif prev_key and prev_key != current_weekday:
        # import pdb; pdb.set_trace()
        final_res = res / counter
        # print(final_res)
        print(prev_key, final_res)
        # final_res = 0
        prev_key = current_weekday
        counter = 1
        res = float(current_sale)
    # print(counter)
    # print(res)
final_res = res / counter
print(prev_key, final_res)

