#If we have multiple conditions then if else wont work for us, if elif else.
#It picks the FIRST True one and ignores the other elif.
#Find the grade of the mark below using the below table
# >= 70 - A
# < 70 and >= 60 - B
# < 60 and >= 50 - C
# < 50 and >=40 - D
# < 40 - E
marks = 70
if marks >= 70:
    print("A")
elif marks < 70 and marks >= 60:
    print("B")
elif marks < 60 and marks >= 50:
    print("C")
elif marks < 50 and marks >= 40:
    print("D")
else:
    print("E")