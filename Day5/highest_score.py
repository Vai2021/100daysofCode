student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

length=len(student_scores)
high = 0
for i in range (1,length):
  new = student_scores[i]
  if new > high:
    high = new
  else:
    high = high

print(f'The highest score in the class is: {high}')


