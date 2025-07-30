"""
Exercise: Filtering and Transforming Student Grades
Description: You have a list of student grades. Create a list comprehension that:
1. Filters out grades below 60 (failing grades)
2. Converts passing grades to letter grades using this scale:
   - 90-100: 'A'
   - 80-89: 'B' 
   - 70-79: 'C'
   - 60-69: 'D'

Instructions:
Use a single list comprehension to filter and transform the grades.
You'll need to use a conditional expression (ternary operator) within the comprehension.

Data:
grades = [45, 78, 92, 67, 55, 88, 74, 96, 61, 83, 59, 71]

Expected result:
['C', 'A', 'D', 'B', 'C', 'A', 'D', 'B', 'C']
"""

# Data
grades = [45, 78, 92, 67, 55, 88, 74, 96, 61, 83, 59, 71]

# Your code here

filtered_grades = ['A' if grade >= 90 else 'B' if grade >= 80 else 'C' if grade >= 70 else 'D' for grade in grades if grade >= 60]
print(filtered_grades)

expected_result = ['C', 'A', 'D', 'B', 'C', 'A', 'D', 'B', 'C']  # Replace with the expected result of the exercise

print(expected_result==filtered_grades)