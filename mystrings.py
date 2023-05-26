#Strings are alphanumeric characters. Alphabets, numbers and characters. UTF8.
#Certain operations or methods are done on strings ONLY. 
#1.Converting casing. To lower case or upper case.
#2.Spliting values
#3.Count the number of times a word appears
#..etc
#To accees these operations or methods we use a . after the variable name.

#mydata = "(omo|tv|2),(ariel|radio|4)"

first_name = "John"
first_name = first_name.lower()
print(first_name)

last_name="  doe    "
last_name = last_name.strip()

email="       MaiL2@Mail.com"
email = email.strip().lower()
# print(email.count("m"))

mypara = "The day has started well. I woke up at 5. My shchedule is packed"
mysent = mypara.split(".")
# print(type(mysent))

#Indexing is accessing a character in a variable by counting starting from 0. 
myname = "John Doe "
print(myname[-5])
#Slicing is when you want to access multiple characters in a variable.
#First part is using the index of where to start
#Second part is the count of where to stop
print(myname[0:4])

#Display Doe using slicing. Try with both negative and positive numbers
print(myname[])
print(myname[])

#len
print(len(myname))
