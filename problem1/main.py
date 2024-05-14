# input
student_score = 80

# Process: Your Solution Code Here
num = int(student_score)
grade = ""

if num >= 80:
        grade = "A"
elif num >= 50:
    if num >= 65:
        grade = "B+"
    else:
        grade = "B"
elif num >= 35:
    grade = "C"
else:
    grade = "D"

print("Nilai", grade)

# Output "Nilai A"