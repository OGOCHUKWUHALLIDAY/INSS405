num_courses = 18 # choose 18 as number of courses taken by the user
total_score = 0

#create a loop of 18 numbers and calculate a total score
for i in range(18):
    score = int(input(f"Enter final score for course {i+1}: "))
    total_score += score


average_score = total_score / num_courses
# To determine the grades: use #If and elf conditions:

if average_score > 90:
    grade = "A"
elif average_score > 80:
    grade = "B"
elif average_score >= 75:
    grade = "C"
elif average_score > 60:
    grade = "D"
else:
    grade = "F"
#To carryout conditional statements:
print(f"Total score: {total_score}")
print(f"Average score: {average_score}")
print(f"Grade:{grade}")