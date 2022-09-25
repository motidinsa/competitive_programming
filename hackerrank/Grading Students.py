def gradingStudents(grades):
    finalGrades = []
    for i in range(len(grades)):
        if grades[i] < 38 or ((grades[i] // 5) + 1) * 5 - grades[i] >= 3:
            finalGrades.append(grades[i])
        elif ((grades[i] // 5) + 1) * 5 - grades[i] < 3:
            finalGrades.append(((grades[i] // 5) + 1) * 5)
    return finalGrades


print(gradingStudents([73, 67, 38, 33]))
