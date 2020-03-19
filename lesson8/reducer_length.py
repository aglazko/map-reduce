import sys

prev_id = 0
prev_type = 0
total_length = 0
avg_ans_length = 0
count_of_ans = 0
question_length = 0

for line in sys.stdin:
    mapped_data = line.strip().split(' ')
    current_type = mapped_data[1]
    current_id = mapped_data[0]
    body_length = float(mapped_data[-1])

    if prev_id and prev_id != current_id:
        print(prev_id, "    ",question_length, "    ", avg_ans_length)
        prev_id = current_id
        prev_type = current_type
        post_length = 0
        avg_ans_length = 0
        count_of_ans = 0
        total_length = 0

    prev_id = current_id
    prev_type = current_type

    if prev_type == 'A':
        count_of_ans += 1
        total_length += body_length
        avg_ans_length = total_length / count_of_ans
    if prev_type == 'Q':
        question_length = body_length
print(prev_id, "    ",question_length, "    ", avg_ans_length)
