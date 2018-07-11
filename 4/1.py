score = int(input())
grade = ""

if score <= 100 and score > 89:
    grade = "A"
elif score <= 89 and score > 79:
    grade = "B"
elif score <= 79 and score > 69:
    grade = "C"
elif score <= 69 and score > 59:
    grade = "D"
else:
    grade = "F"

print(grade)
