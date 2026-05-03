print ("----- Input Q1 Grades -----")

#The "score" and "total" variables simplifies what a user must input while the "percentage" variables turn the raw scores into percentages
q1_formative1_score = float(input("Formative Assessment 1 - Your score: "))
q1_formative1_total = float(input("Formative Assessment 1 - total points possible: "))
q1_formative1_percentage = q1_formative1_score / q1_formative1_total * 100

q1_formative2_score = float(input("Formative Assessment 2 - Your score: "))
q1_formative2_total = float(input("Formative Assessment 2 - total points possible: "))
q1_formative2_percentage = q1_formative2_score / q1_formative2_total * 100

q1_formative3_score = float(input("Formative Assessment 3 - Your score: "))
q1_formative3_total = float(input("Formative Assessment 3 - total points possible: "))
q1_formative3_percentage = q1_formative3_score / q1_formative3_total * 100

q1_formative4_score = float(input("Formative Assessment 4 - Your score: "))
q1_formative4_total = float(input("Formative Assessment 4 - total points possible: "))
q1_formative4_percentage = q1_formative4_score / q1_formative4_total * 100

#The strip of code below computes the Quarter 1 Formative Assessment percentage only taking 30 percent of its total value
q1_formative_assessment_percentage = ((q1_formative1_percentage + q1_formative2_percentage + q1_formative3_percentage + q1_formative4_percentage) / 4) * 0.3
print("your Quarter 1 Formative Assessment percentage is:", q1_formative_assessment_percentage)

#We use the same format from the Formative Assessment
q1_summative1_score = float(input("Summative Assessment 1 - Your score: "))
q1_summative1_total = float(input("Summative Assessment 1 - total points possible: "))
q1_summative1_percentage = q1_summative1_score / q1_summative1_total * 100

q1_summative2_score = float(input("Summative Assessment 2 - Your score: "))
q1_summative2_total = float(input("Summative Assessment 2 - total points possible: "))
q1_summative2_percentage = q1_summative2_score / q1_summative2_total * 100

q1_quarter_exam_score = float(input("Quarterly Exam - Your score: "))
q1_quarter_exam_total = float(input("Quarterly Exam - total points possible: "))
q1_quarter_exam_percentage = q1_quarter_exam_score / q1_quarter_exam_total * 100

#We multiply each Summative Assessment part to a certain degree because their percentages are not taken equally
q1_summative_assessment_percentage = q1_summative1_percentage * 0.25 + q1_summative2_percentage * 0.25 + q1_quarter_exam_percentage * 0.2
print("your Quarter 1 Summative Assessment percentage is:", q1_summative_assessment_percentage)

q1_percentage_grade = q1_formative_assessment_percentage + q1_summative_assessment_percentage
print("your Quarter 1 Grade Percentage is:", q1_percentage_grade)

if q1_percentage_grade >= 96:
    print("your Grade Point Equivalent is 1.00 (EXCELLENT):")
elif q1_percentage_grade >= 90:
    print("your Grade Point Equivalent is 1.25 (VERY GOOD)")
elif q1_percentage_grade >= 84:
    print("your Grade Point Equivalent is 1.50 (VERY GOOD)")
elif q1_percentage_grade >= 78:
    print("your Grade point Equivalent is 1.75 (GOOD)")
elif q1_percentage_grade >= 72:
    print("your Grade Point Equivalent is 2.00 (GOOD)")
elif q1_percentage_grade >= 66:
    print("your Grade Point Equivalent is 2.25 (SATISFACTORY)")
elif q1_percentage_grade >= 60:
    print("your Grade Point Equivalent is 2.50 (SATISFACTORY)")
elif q1_percentage_grade >= 55:
    print("your Grade Point Equivalent is 2.75 (FAIR)")
elif q1_percentage_grade >= 50:
    print("your Grade Point Equivalent is 3.00 (FAIR)")
elif q1_percentage_grade >= 40:
    print("your Grade Point Equivalent is 4.00 (FAILED ON CONDITION)")
elif q1_percentage_grade < 40:
    print("your Grade Point Equivalent is 5.00 (FAILED)")

print ("----- Input Q2 Grades -----")

#We use the same format for the Formative and Summative Assessments we used in Quarter 1
q2_formative1_score = float(input("Formative Assessment 1 - Your score: "))
q2_formative1_total = float(input("Formative Assessment 1 - total points possible: "))
q2_formative1_percentage = q2_formative1_score / q2_formative1_total * 100

q2_formative2_score = float(input("Formative Assessment 2 - Your score: "))
q2_formative2_total = float(input("Formative Assessment 2 - total points possible: "))
q2_formative2_percentage = q2_formative2_score / q2_formative2_total * 100

q2_formative3_score = float(input("Formative Assessment 3 - Your score: "))
q2_formative3_total = float(input("Formative Assessment 3 - total points possible: "))
q2_formative3_percentage = q2_formative3_score / q2_formative3_total * 100

q2_formative4_score = float(input("Formative Assessment 4 - Your score: "))
q2_formative4_total = float(input("Formative Assessment 4 - total points possible: "))
q2_formative4_percentage = q2_formative4_score / q2_formative4_total * 100

q2_formative_assessment_percentage = ((q2_formative1_percentage + q2_formative2_percentage + q2_formative3_percentage + q2_formative4_percentage) / 4) * 0.3
print("your Quarter 2 Formative Assessment percentage is:", q2_formative_assessment_percentage)

q2_summative1_score = float(input("Summative Assessment 1 - Your score: "))
q2_summative1_total = float(input("Summative Assessment 1 - total points possible: "))
q2_summative1_percentage = q2_summative1_score / q2_summative1_total * 100

q2_summative2_score = float(input("Summative Assessment 2 - Your score: "))
q2_summative2_total = float(input("Summative Assessment 2 - total points possible: "))
q2_summative2_percentage = q2_summative2_score / q2_summative2_total * 100

q2_quarter_exam_score = float(input("Quarterly Exam - Your score: "))
q2_quarter_exam_total = float(input("Quarterly Exam - total points possible: "))
q2_quarter_exam_percentage = q2_quarter_exam_score / q2_quarter_exam_total * 100

q2_summative_assessment_percentage = q2_summative1_percentage * 0.25 + q2_summative2_percentage * 0.25 + q2_quarter_exam_percentage * 0.2
print("your Quarter 2 Summative Assessment percentage is:", q2_summative_assessment_percentage)

#This is only the Tentative 2nd quarter grade, not the final
q2_tentative_percentage_grade = q2_formative_assessment_percentage + q2_summative_assessment_percentage
print("your Quarter 2 Tentative Grade Percentage is:", q2_tentative_percentage_grade)

q2_final_percentage_grade = (q1_percentage_grade + q2_tentative_percentage_grade * 2) / 3
print("your Quarter 2 Final Grade Percentage is:", q2_final_percentage_grade)

if q2_final_percentage_grade >= 96:
    print("your Grade Point Equivalent is 1.00 (EXCELLENT):")
elif q2_final_percentage_grade >= 90:
    print("your Grade Point Equivalent is 1.25 (VERY GOOD)")
elif q2_final_percentage_grade >= 84:
    print("your Grade Point Equivalent is 1.50 (VERY GOOD)")
elif q2_final_percentage_grade >= 78:
    print("your Grade point Equivalent is 1.75 (GOOD)")
elif q2_final_percentage_grade >= 72:
    print("your Grade Point Equivalent is 2.00 (GOOD)")
elif q2_final_percentage_grade >= 66:
    print("your Grade Point Equivalent is 2.25 (SATISFACTORY)")
elif q2_final_percentage_grade >= 60:
    print("your Grade Point Equivalent is 2.50 (SATISFACTORY)")
elif q2_final_percentage_grade >= 55:
    print("your Grade Point Equivalent is 2.75 (FAIR)")
elif q2_final_percentage_grade >= 50:
    print("your Grade Point Equivalent is 3.00 (FAIR)")
elif q2_final_percentage_grade >= 40:
    print("your Grade Point Equivalent is 4.00 (FAILED ON CONDITION)")
elif q2_final_percentage_grade < 40:
    print("your Grade Point Equivalent is 5.00 (FAILED)")

print ("----- Input Q3 Grades -----")

q3_formative1_score = float(input("Formative Assessment 1 - Your score: "))
q3_formative1_total = float(input("Formative Assessment 1 - total points possible: "))
q3_formative1_percentage = q3_formative1_score / q3_formative1_total * 100

q3_formative2_score = float(input("Formative Assessment 2 - Your score: "))
q3_formative2_total = float(input("Formative Assessment 2 - total points possible: "))
q3_formative2_percentage = q3_formative2_score / q3_formative2_total * 100

q3_formative3_score = float(input("Formative Assessment 3 - Your score: "))
q3_formative3_total = float(input("Formative Assessment 3 - total points possible: "))
q3_formative3_percentage = q3_formative3_score / q3_formative3_total * 100

q3_formative4_score = float(input("Formative Assessment 4 - Your score: "))
q3_formative4_total = float(input("Formative Assessment 4 - total points possible: "))
q3_formative4_percentage = q3_formative4_score / q3_formative4_total * 100

q3_formative_assessment_percentage = ((q3_formative1_percentage + q3_formative2_percentage + q3_formative3_percentage + q3_formative4_percentage) / 4) * 0.3
print("your Quarter 3 Formative Assessment percentage is:", q3_formative_assessment_percentage)

q3_summative1_score = float(input("Summative Assessment 1 - Your score: "))
q3_summative1_total = float(input("Summative Assessment 1 - total points possible: "))
q3_summative1_percentage = q3_summative1_score / q3_summative1_total * 100

q3_summative2_score = float(input("Summative Assessment 2 - Your score: "))
q3_summative2_total = float(input("Summative Assessment 2 - total points possible: "))
q3_summative2_percentage = q3_summative2_score / q3_summative2_total * 100

q3_quarter_exam_score = float(input("Quarterly Exam - Your score: "))
q3_quarter_exam_total = float(input("Quarterly Exam - total points possible: "))
q3_quarter_exam_percentage = q3_quarter_exam_score / q3_quarter_exam_total * 100

q3_summative_assessment_percentage = q3_summative1_percentage * 0.25 + q3_summative2_percentage * 0.25 + q3_quarter_exam_percentage * 0.2
print("your Quarter 3 Summative Assessment percentage is:", q3_summative_assessment_percentage)

q3_tentative_percentage_grade = q3_formative_assessment_percentage + q3_summative_assessment_percentage
print("your Quarter 3 Tentative Grade Percentage is:", q3_tentative_percentage_grade)

#We simply copy the strip of code from 2nd Quarter
q3_final_percentage_grade = (q2_final_percentage_grade + q3_tentative_percentage_grade * 2) / 3
print("your Quarter 3 Final Grade Percentage is:", q3_final_percentage_grade)

if q3_final_percentage_grade >= 96:
    print("your Grade Point Equivalent is 1.00 (EXCELLENT):")
elif q3_final_percentage_grade >= 90:
    print("your Grade Point Equivalent is 1.25 (VERY GOOD)")
elif q3_final_percentage_grade >= 84:
    print("your Grade Point Equivalent is 1.50 (VERY GOOD)")
elif q3_final_percentage_grade >= 78:
    print("your Grade point Equivalent is 1.75 (GOOD)")
elif q3_final_percentage_grade >= 72:
    print("your Grade Point Equivalent is 2.00 (GOOD)")
elif q3_final_percentage_grade >= 66:
    print("your Grade Point Equivalent is 2.25 (SATISFACTORY)")
elif q3_final_percentage_grade >= 60:
    print("your Grade Point Equivalent is 2.50 (SATISFACTORY)")
elif q3_final_percentage_grade >= 55:
    print("your Grade Point Equivalent is 2.75 (FAIR)")
elif q3_final_percentage_grade >= 50:
    print("your Grade Point Equivalent is 3.00 (FAIR)")
elif q3_final_percentage_grade >= 40:
    print("your Grade Point Equivalent is 4.00 (FAILED ON CONDITION)")
elif q3_final_percentage_grade < 40:
    print("your Grade Point Equivalent is 5.00 (FAILED)")

print ("----- Input Q4 Grades -----")

q4_formative1_score = float(input("Formative Assessment 1 - Your score: "))
q4_formative1_total = float(input("Formative Assessment 1 - total points possible: "))
q4_formative1_percentage = q4_formative1_score / q4_formative1_total * 100

q4_formative2_score = float(input("Formative Assessment 2 - Your score: "))
q4_formative2_total = float(input("Formative Assessment 2 - total points possible: "))
q4_formative2_percentage = q4_formative2_score / q4_formative2_total * 100

q4_formative3_score = float(input("Formative Assessment 3 - Your score: "))
q4_formative3_total = float(input("Formative Assessment 3 - total points possible: "))
q4_formative3_percentage = q4_formative3_score / q4_formative3_total * 100

q4_formative4_score = float(input("Formative Assessment 4 - Your score: "))
q4_formative4_total = float(input("Formative Assessment 4 - total points possible: "))
q4_formative4_percentage = q4_formative4_score / q4_formative4_total * 100

q4_formative_assessment_percentage = ((q4_formative1_percentage + q4_formative2_percentage + q4_formative3_percentage + q4_formative4_percentage) / 4) * 0.3
print("your Quarter 4 Formative Assessment percentage is:", q4_formative_assessment_percentage)

q4_summative1_score = float(input("Summative Assessment 1 - Your score: "))
q4_summative1_total = float(input("Summative Assessment 1 - total points possible: "))
q4_summative1_percentage = q4_summative1_score / q4_summative1_total * 100

q4_summative2_score = float(input("Summative Assessment 2 - Your score: "))
q4_summative2_total = float(input("Summative Assessment 2 - total points possible: "))
q4_summative2_percentage = q4_summative2_score / q4_summative2_total * 100

q4_quarter_exam_score = float(input("Quarterly Exam - Your score: "))
q4_quarter_exam_total = float(input("Quarterly Exam - total points possible: "))
q4_quarter_exam_percentage = q4_quarter_exam_score / q4_quarter_exam_total * 100

q4_summative_assessment_percentage = q4_summative1_percentage * 0.25 + q4_summative2_percentage * 0.25 + q4_quarter_exam_percentage * 0.2
print("your Quarter 4 Summative Assessment percentage is:", q4_summative_assessment_percentage)

q4_tentative_percentage_grade = q4_formative_assessment_percentage + q4_summative_assessment_percentage
print("your Quarter 4 Tentative Grade Percentage is:", q4_tentative_percentage_grade)

q4_final_percentage_grade = (q3_final_percentage_grade + q4_tentative_percentage_grade * 2) / 3
print("your 4th Quarter Final Grade Percentage for this subject is:", q4_final_percentage_grade)

if q4_final_percentage_grade >= 96:
    print("your Final Grade Point Equivalent for this subject is 1.00 (EXCELLENT):")
elif q4_final_percentage_grade >= 90:
    print("your Final Grade Point Equivalent for this subject is 1.25 (VERY GOOD)")
elif q4_final_percentage_grade >= 84:
    print("your Final Grade Point Equivalent for this subject is 1.50 (VERY GOOD)")
elif q4_final_percentage_grade >= 78:
    print("your Final Grade Point Equivalent for this subject is 1.75 (GOOD)")
elif q4_final_percentage_grade >= 72:
    print("your Final Grade Point Equivalent for this subject is 2.00 (GOOD)")
elif q4_final_percentage_grade >= 66:
    print("your Final Grade Point Equivalent for this subject is 2.25 (SATISFACTORY)")
elif q4_final_percentage_grade >= 60:
    print("your Final Grade Point Equivalent for this subject is 2.50 (SATISFACTORY)")
elif q4_final_percentage_grade >= 55:
    print("your Final Grade Point Equivalent for this subject is 2.75 (FAIR)")
elif q4_final_percentage_grade >= 50:
    print("your Final Grade Point Equivalent for this subject is 3.00 (FAIR)")
elif q4_final_percentage_grade >= 40:
    print("your Final Grade Point Equivalent for this subject is 4.00 (FAILED ON CONDITION)")
elif q4_final_percentage_grade < 40:
    print("your Final Grade Point Equivalent for this subject is 5.00 (FAILED)")
