def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

n = int(input("Enter number of subjects: "))
marks = []
for i in range(n):
    mark = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(mark)

avg = sum(marks) / n
print("Marks:", marks)
print("Average:", avg)
print("Grade:", calculate_grade(avg))
