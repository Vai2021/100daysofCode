
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total =0
avg = 0
length = 0
for i in student_heights:
  length = length+1
  total = total+i

avg = round(total/length)
print(avg)





