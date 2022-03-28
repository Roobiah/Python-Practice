'''
student_heights = input("Input a list of student heights ").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
count = 0
total = 0
max = 0
for height in student_heights:
    count = count + 1
    total += height
    if height > max:
       max = height
print(max)
average_height = round(total / count)
# print(average_height)
'''
total = 0
for n in range(2, 101, 2):
   total += n
print(total)