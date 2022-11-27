students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

#Create an empty dictionary called students
student_grades = {}


#Add the grades to the student_grades
for key in students_scores:
    grade = students_scores[key]
    if grade > 90:
        student_grades[key] =  "Outstanding"
    elif grade > 80 or grade <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif grade > 70 or grade <= 80 :
        student_grades[key] = "Acceptable"
    elif grade <= 70:
        student_grades[key] = "Fail"


print(student_grades)
