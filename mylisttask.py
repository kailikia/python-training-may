trainees = ["John", [2, ["James","Mary"]]]
#1
two=trainees[1][0]
print(two)

#2
trainees2 = trainees[1][1][0]
print(trainees2)

#3
trainees.append(56)
print(trainees)

#4
trainees[1][1].insert(1, "Mike")
print(trainees)

#5
trainees[1][0]=8
print(trainees)

#6
del trainees[0]
del trainees[0][1][-1]
print(trainees)

#7
print(len(trainees))