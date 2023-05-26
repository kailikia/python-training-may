days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")

#1. Use an index to get  Wednesday
wed=days[2]
print(wed)

#2. Slice to get Wednesday to Friday
days2= days[2:5]
print(days2)

#3. Try to replace the value of Sat to Saturday 
#It is not possible to change a value that is in a tuple
t=list(days)
t[5]="Saturday"
days=tuple(t)
print(days)
