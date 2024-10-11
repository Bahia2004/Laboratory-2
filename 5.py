students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]

highest_score = students_scores[0][1]  
top_student = students_scores[0][0]

for i in range(len(students_scores)):  
    if students_scores[i][1] > highest_score:
        highest_score = students_scores[i][1]
        top_student = students_scores[i][0]

print("Student with the highest score is:", top_student, "with a score of", highest_score)
