
#choose 15 as the number of courses taken by the user

subjects = 15
sum= 0.00

#create a loop of 15 numbers and calculate the total score:

for i in range(15):
    score = input("Enter final score for course")
    sum=sum+int(score)

#To perform the average
average = sum / 15
print("Total sum=", sum)
print("Average", average)

#To determine the grades use the if and elif statement:
if(int(average) > 90):
    print("A")
elif(int(average) > 80):
    print("B")
elif(int(average) >= 75 and int(average) <= 79):
    print("C")
elif(int(average) > 60) and int(score)<=74:
    print("D")
else:
    print("F")
