'''
### Exercise: Codebasics Student Performance Tracker
You're tracking quiz scores for students in a Python cohort. Each student has taken 3 quizzes, and you want to figure out who's passing, who's topping, and the class average.

```
students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}
```

Each key is a student name, and each value is a list of 3 quiz scores (out of 100).

Write code using for loops to do the following:

1. Calculate each student's average score and print it in this format:```Aarav: 84.33```
2. Classify each student based on their average:
    80 and above → "Topper"
    60 to 79 → "Pass"
    Below 60 → "Needs improvement"
3. Find the topper of the class (highest average) and print their name and score.
4. Calculate the class average across all students.

Expected output (roughly)

```
=== Student Averages ===
Aarav: 84.33 - Topper
Priya: 71.67 - Pass
Rohan: 48.33 - Needs improvement
Sneha: 95.00 - Topper
Manish: 65.00 - Pass

=== Class Topper ===
Sneha with average 95.00

=== Class Average ===
72.87
```

'''
students = {
    "Aarav":   [85, 90, 78],
    "Priya":   [72, 68, 75],
    "Rohan":   [45, 52, 48],
    "Sneha":   [95, 92, 98],
    "Manish":  [60, 65, 70],
}
#Calculate each student's average score and print it in this format:```Aarav: 84.33```
for name, marks in students.items():
    average = sum(marks)//3
    if(average > 80):
        grade = "Topper"
        print(f"{name} : {average} - {grade}")
    elif(average >= 65 and average < 80):
        grade = "Pass"
        print(f"{name} : {average} - {grade}")
    else:
        grade = "Need Improvement"
        print(f"{name} : {average} - {grade}")