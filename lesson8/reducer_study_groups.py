import sys

prev_question_id = 0
students = []

for line in sys.stdin:
    mapped_data = line.strip().split("\t")
    if len(mapped_data) != 2:
        continue
    current_question_id, current_student_id = mapped_data
    if prev_question_id and prev_question_id != current_question_id:
        print(prev_question_id, students)
        students = []
    prev_question_id = current_question_id
    students.append(current_student_id)
if prev_question_id:
    print(prev_question_id, students)
