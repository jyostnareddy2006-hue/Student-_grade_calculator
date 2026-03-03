from calculator import calculate_grade

print("Student Grade Calculator")

marks = float(input("Enter your marks: "))

grade = calculate_grade(marks)

print("Your Grade is:", grade)
