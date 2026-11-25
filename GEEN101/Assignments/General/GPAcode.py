# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:22:53 2026

@author: pjpri
"""

classes = ["Chemistry", "Chemistry Lab", "Calculus", "English", "Eng Soft", "Eng Design", "Eng Col" ]
grades = ["B", "A-", "A+", "A+", "A-", "B", "B-"]
credits = [3, 1, 4, 3, 2, 2, 1]

grade_points = {
    'A+': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0,
    'D-': 0, 'F': 0
    }

total_quality_points = 0
total_credits = 0

print("----------Semester GPA Calculation----------")

for i in range(len(classes)):
    current_class = classes[i]
    current_grade = grades[i]
    current_credit = credits[i]
    points_per_credit = grade_points[current_grade]
    class_points = points_per_credit * current_credit
    total_quality_points = total_quality_points + class_points
    total_credits = total_credits + current_credit
    print(f"{current_class}: {current_grade} | {current_credit} Credits")
    
print("---------------------------------")

final_gpa = total_quality_points / total_credits

print(f"Total Credit Hours: {total_credits}")
print(f"GPA: {final_gpa}")
