student_scores = input("input a list of student scores: \n").split(" ")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max=0
for i in range(n+1):
    if student_scores[i] > max:
        max = student_scores[i]
    


print(f"the highest score in the class is: {max}")

