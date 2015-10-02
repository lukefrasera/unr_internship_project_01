#!/usr/bin/env python
"""
Grade Average Calculator
"""



def Average(grades):
	index=0
	sum = 0.0
	while index<len(grades):
		sum = grades[index] + sum
		index = index + 1
	grade_average = sum/len(grades)
	return grade_average


mc_project_grades = [92.0,94.0,90.0,85.0,88.0]
mc_quiz_grades = [90.0,85.0,95.0]
mc_exam_grades = [90.0,92.0,85.0,70.0]

mc_project_average = Average(mc_project_grades)	
print "{0:0.2f}".format(mc_project_average)

mc_quiz_average = Average(mc_quiz_grades)
print "{0:0.2f}".format(mc_quiz_average)

mc_exam_average = Average(mc_exam_grades)
print "{0:0.2f}".format(mc_exam_average)

mc_final_grade = (mc_project_average + mc_quiz_average + mc_exam_average)/3
print "{0:0.2f}".format(mc_final_grade)


def PassingScores(final_grade):
	if final_grade > 75:
		return "You can pass CS135"
	else:
		return "You can't pass CS135"


mc_qualifying_score = PassingScores(mc_final_grade)
print (mc_qualifying_score)

