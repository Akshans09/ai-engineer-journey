import numpy as np

# You are given exam scores for 4 students across 3 subjects
scores = np.array([
    [85, 92, 78],   # Student 1: Math, Science, English
    [90, 88, 95],   # Student 2
    [70, 65, 80],   # Student 3
    [60, 72, 68],   # Student 4
])


# Task 1: Print the shape. What does each number mean here?
print(scores.shape) # 4 rows and 3 columns hence shape is (4,3)

# Task 2: Print the Science scores (column index 1) for all students
print(scores[:, 1])

# Task 3: Print the average score per student (axis=1)
# Expected: each student gets one average number

print(scores.mean(axis=1))

# Task 4: Print the average score per subject (axis=0)
# Expected: each subject gets one average number
print(scores.mean(axis=0))

# Task 5: Find which students scored below 75 in Math (column 0)
# Print their Math scores only

print(scores[scores[:, 0]<75, 0])

# Task 6: Normalize the scores to 0-1 range using this formula:
# normalized = (scores - scores.min()) / (scores.max() - scores.min())
# Print the normalized array rounded to 2 decimal places
# Hint: np.round(array, 2)

x= scores.min()
y=scores.max()



normalized = (scores-x)/(y-x)
#print(np.round(normalized,2))

#print(scores[scores[:, 0]<75])

