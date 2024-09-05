# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter your score\n"))

if score >= 90 and score < 100:
    print("Grade is -> ", "A")
elif score <=89 and score > 85:
    print("Grade is ->", "B")
elif score > 100:
    print("Grade is ->", "F")
elif score > 70:
    print("Grade is ->", "C")
else:
    print("Grade is ->", "FAIL")
