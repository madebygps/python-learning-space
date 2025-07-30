---
mode: agent
---
# Generate a List Comprehension Exercise

Generate a Python exercise that teaches list comprehensions through progressive, hands-on practice. 

## Exercise Creation Process

1. **Analyze existing exercises**: Read all files in `list-comps` directory to understand current difficulty progression and avoid duplication.
2. **Determine next exercise**: Create a new python file following the naming convention `listcomp_<number>.py` where `<number>` is the next sequential number.
3. **Select appropriate difficulty**: Choose from these complexity levels and ensure logical progression:
   - **Basic (1-3)**: Simple filtering or transformation with single conditions
   - **Intermediate (4-6)**: Multiple conditions, nested structures, or function calls  
   - **Advanced (7+)**: Complex logic, multiple list comprehensions, or performance optimization
4. **Create exercise content**: Write a Python exercise using this exact structure:
```python
"""
Exercise: [Descriptive Title]
Description: [Clear explanation of the problem scenario and context]

Requirements:
[Single clear requirement describing what they need to accomplish - outcome focused]

Learning objective: [What specific list comprehension concept this teaches]
"""

# Data
[variable_name] = [sample_data]  # Can be list, dict, tuple, set, or any iterable structure

# Your code here


# Uncomment to test your solution
# expected_result = [expected_output]
# print(f"Your result: {your_variable_name}")
# print(f"Expected:    {expected_result}")
# print(f"Match:       {your_variable_name == expected_result}")
``` 
## Quality Requirements

**Educational Value**:
- Exercise must teach a specific list comprehension concept (filtering, mapping, nested loops, conditionals)
- Difficulty should progress logically from existing exercises
- Include real-world context to make the problem meaningful
- **Single focused task**: Each exercise should have one clear objective requiring one list comprehension
- Ensure the task has a clear purpose and learning outcome
- **Maintain productive struggle**: Task should require thinking but not be frustrating
- **Avoid over-scaffolding**: Don't provide step-by-step solutions in comments
- **Force discovery**: Students must figure out syntax, variable names, and approach independently
- **Real problem focus**: Present authentic challenges that naturally require list comprehensions

**Technical Standards**:
- Solution must genuinely require list comprehensions (not just be possible with them)
- Expected result must be mathematically/logically correct
- Data should be realistic and diverse enough to test edge cases
- Use Python 3.13 features and modern best practices
- **Appropriate challenge level**: Should require 5-15 minutes of focused thinking
- **No trivial solutions**: Avoid tasks that are immediately obvious from the data
- **Single list comprehension**: Exercise should be solvable with exactly one list comprehension
- **Natural data choice**: Select data structure that makes the problem feel authentic

**Clarity Standards**:
- **Outcome-focused requirements**: Tell students WHAT to achieve, not HOW to do it
- **Minimal scaffolding**: Provide context and goals, let students discover the method
- **No syntax hints**: Students should research/experiment with list comprehension syntax
- **No variable names**: Let students choose their own meaningful variable names
- **Problem-driven learning**: Present real scenarios, let students determine the approach

## Content Guidelines

**Real-World Scenarios**: Use practical contexts like:
- E-commerce (products, prices, categories)
- Education (students, grades, courses) 
- Data processing (logs, records, measurements)
- Text analysis (documents, words, patterns)
- Gaming (scores, players, achievements)

**Data Design**:
- Use realistic, diverse datasets (6-10 items minimum for lists, appropriate size for other structures)
- **Flexible data types**: Choose the most natural structure for the problem:
  - **Lists**: For sequences, collections, ordered data
  - **Dictionaries**: For key-value pairs, records, mappings  
  - **Tuples**: For structured records, coordinate pairs, immutable data
  - **Sets**: For unique collections, membership testing
  - **Strings**: For character manipulation, text processing
  - **Mixed structures**: Lists of dicts, nested data, etc.
- Include edge cases and boundary conditions
- Make data relatable and memorable
- Ensure data naturally leads to a single list comprehension solution

**Task Progression**:
- Present business/real-world problems that need solving
- Focus on WHAT needs to be accomplished, not HOW
- **No method hints**: Students discover that list comprehensions are the right tool
- **Graduated complexity**: Each exercise should be slightly more challenging than previous ones
- **Authentic scenarios**: Use problems that developers actually face
- **Single objective**: Each exercise focuses on one clear goal

## Exercise Topics
(Choose One or More but make sure they genuinely require list comprehensions and benefit from them)
- **Filtering**: Extract elements based on conditions (single and multiple criteria)
- **Mapping**: Transform elements using functions or expressions  
- **Nested Lists**: Work with 2D data structures or multiple iterables
- **Conditional Logic**: Use if-else expressions within comprehensions
- **Function Integration**: Combine list comprehensions with function calls or methods
- **Performance**: Compare comprehensions vs. traditional loops
- **String Processing**: Text manipulation and pattern matching
- **Data Analysis**: Working with dictionaries, CSV-like data, or structured records
- **Mathematical Operations**: Calculations, aggregations, and number theory
- **Complex Filtering**: Multiple conditions with and/or logic

## Grading and Feedback

When asked to grade an exercise:

1. **Execute the solution**: Run `uv run list-comps/listcomp_<number>.py` to test the user's code.
2. **Verify correctness**: Compare actual output with expected result.
3. **Analyze approach**: Evaluate if the solution properly uses list comprehensions and follows Python best practices.
4. **Check implementation**: Ensure the student used exactly one list comprehension as intended.
5. **Provide detailed feedback**:
   - **If correct**: Praise the approach and suggest potential optimizations or alternative solutions
   - **If incorrect**: 
     - Explain what went wrong (logic, syntax, or approach)
     - Provide specific hints without giving the complete solution
     - Suggest debugging techniques or testing strategies
     - Point out any non-list-comprehension solutions if they used loops instead
5. **Educational guidance**: Connect the exercise to broader Python concepts and suggest next learning steps.