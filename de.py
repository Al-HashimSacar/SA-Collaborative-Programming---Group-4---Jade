print ("----- Input Grades -----")

formative1 = float(input("Formative Assessment 1 - Your percentage: "))
formative2 = float(input("Formative Assessment 2 - Your percentage: "))
formative3 = float(input("Formative Assessment 3 - Your percentage: "))
formative4 = float(input("Formative Assessment 4 - Your percentage: "))

formativetotal = (formative1 + formative2 + formative3 + formative4) / 4 * 0.3
print("Your average formative percentage is:", formativetotal)

quarterlyexam = float(input("Quarterly Exam - Your percentage: "))
longtest1 = float(input("Long Test 1 - Your percentage: "))
longtest2 = float(input("Long Test 2 - Your percentage: "))
project = float(input("Project - Your percentage: "))   

summativetotal = (longtest1 + longtest2 + project + quarterlyexam) / 4 * 0.7
print("Your average summative percentage is:", summativetotal)

finalgrade = formativetotal + summativetotal
if finalgrade >= 96:
    print("Your final grade is:", finalgrade, "which is equivalent to 1.00 (Excellent)")
elif finalgrade >= 94:
    print("Your final grade is:", finalgrade, "which is equivalent to 1.25 (Very Good)")