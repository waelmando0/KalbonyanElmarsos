var perStudentPetCount = [0, 1, 2, 3, 0, 2, 6, 2, 3, 1, 2, 3, 4, 0, 1, 2, 1, 0]
var numOfStudent = perStudentPetCount.count


print(perStudentPetCount[2])
// print(perStudentPetCount[200])
print(numOfStudent)


// for loop example
var sum = 0
for individualPetCount in perStudentPetCount {
    sum = sum + individualPetCount
}
print(sum)


var average = sum / numOfStudent
print(average)