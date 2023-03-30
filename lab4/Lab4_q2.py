for i in range(10):
 temperature = input("enter temperature: ")
if(float(temperature) >= 50):
        print("Hot")
elif (float(temperature) >=30 and float(temperature) <50):
        print("warm")
elif (float(temperature) >=0 and float(temperature)<30):
     print("Cold")
elif(float(temperature) <0):
        print("Extreme cold")