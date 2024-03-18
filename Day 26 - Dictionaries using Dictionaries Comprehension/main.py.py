import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_scores = {name:random.randint(0, 100) for name in names}

print(student_scores)

passed_student = {name:score for (name, score) in student_scores.items() if score > 60}

print(passed_student)