#Task 1

students_marks = {
    'Alice' : 85 ,
    'Sam' : 90 ,
    'John' : 70 ,
    'Max' : 75
}

student = input("Enter student's name: ")

if student in students_marks:
    print(f"{student}'s marks: {students_marks[student]}.")
else:
    print("Student not found.")