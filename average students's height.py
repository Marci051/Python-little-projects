student_heights = input("input a list of student heights, seprated by space:\n").split(" ")
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
i = 0
for i in student_heights:
    total += i
final= total / (n+1)
print(f"the average height is:{round(final)}")
    




