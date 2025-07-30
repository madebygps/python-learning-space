---
mode: agent
---
# Generate a List Comprehension Exercise

Generate a Python exercise that focuses on list comprehensions. 

## Task list

1. Read all files in `list-comps` directory.
2. Create a new python file in the `list-comps` directory following the naming convention `listcomp_<number>.py` where `<number>` is the next available number.
3. In that file, write a Python exercise that requires the use of list comprehensions following this structure:
```python
"""
Exercise: Title of the Exercise
Description of the exercise.
Instructions:
Data:
Expected result:
"""
# Your code here

expected_result = None  # Replace with the expected result of the exercise
``` 
4. Ensure the exercise is clear and concise, providing enough context for the user to understand what is required.
5. Verify that the expected result is correct and can be derived from the data provided in the exercise.
6. Verify that the exercise is suitable for the use of list comprehensions.

## Grading

When asked to grade the exercise:

1. Run `uv run listcomp_<number>.py` to execute the code.
2. Check if the output matches the expected result.
3. With output, provide feedback on the correctness of the solution.
4. If the output does not match, provide hints or suggestions for improvement.