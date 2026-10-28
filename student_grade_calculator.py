
# Student Grade Calculator

name = input("Enter student name: ")

m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))
m4 = float(input("Enter marks in Subject 4: "))
m5 = float(input("Enter marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\n----- Student Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)

if min(m1, m2, m3, m4, m5) < 0 or max(m1, m2, m3, m4, m5) > 100:
    print("Please enter marks between 0 and 100.")
elif min(m1, m2, m3, m4, m5) < 40:
    print("Result: Fail")
else:
    print("Result: Pass")

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)
