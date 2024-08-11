
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# Printing the Sum of the numbers in a List

# Option 1
sum_of_scores = sum(student_scores)
print(sum_of_scores)

# Option 2
sum_of_scores = 0
for student_score in student_scores:
    sum_of_scores += student_score
print(sum_of_scores)

# Printing the Highest number in a List

# Option 1
highest_score = max(student_scores)
print(highest_score)

# Option 2
highest_score = 0
for student_score in student_scores:
    if student_score > highest_score:
        highest_score = student_score
print(highest_score)
