# Mandy Mason
# M02_case_study.py
# Test cases in M02_case_study.png (screenshot)

# This app accepts student names and GPAs and tests if the student qualifies for 
# either the Dean's List or the Honor Roll. A GPA of 3.5 or greater qualifies for the
# Dean's List, while a GPA of 3.25 or greater qualifies for the Honor Roll. Entering
# 'ZZZ' as the last name will terminate the program.


last_name = ""
first_name = ""
student_gpa = 0.0

while last_name != "ZZZ":
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name == "ZZZ":
        break
    first_name = input("Enter the student's first name: ")
    student_gpa = float(input("Enter the student's GPA: "))
    
    if student_gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif student_gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify for the Dean's List or the Honor Roll.")