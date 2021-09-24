student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Sum of student_heights without using sum()
sum_of_height = 0
for heights in student_heights:
    sum_of_height += heights
print("sum is:", sum_of_height)

# Lenth of student_heights without using len()
lenth = 0
for students in student_heights:
    lenth += 1
print("lenth is:", lenth)

# Average height
print("Average heights is:", sum_of_height // lenth)
