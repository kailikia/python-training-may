task_list = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]
#1
money= task_list[3][2]["currency"]
print(money)

#2
fv=task_list[2]
print(fv)

#3. 
task_list3 = task_list[3][-2]
print(task_list3)

#4
task_list[3][2]["amount"] = 90
print(task_list)

#5
task_list5 = str(task_list[-2])
task_list5 =task_list5[::-1]
task_list[-2] = task_list5
print(task_list)

#6
list(task_list[-1])
task_list[-1] = "Jane"
task_list = tuple(task_list)
print(task_list)