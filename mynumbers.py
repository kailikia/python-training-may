import math

#1
temp = 56.8926
temp1 = math.ceil(temp)
print(temp1)
#2
num=(round(temp,2))
print(num)
#3
temp4 = round(temp, 3)
print(temp4)
#4
#convert to string then slice
temp = str(temp)
temp = temp[3:]
temp = temp[0:1] + "." + temp[1:]
temp = float(temp)
print(temp)

num = input("Enter a value: ")
print(num)
#Prompt the user for 2 numbers separately, add them up and return the result