
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")



low_name1 = name1.lower()
low_name2 = name2.lower()
string = low_name1+low_name2
#count1 = 0
#count2 = 0

T=string.count("t")
R= string.count("r")
U = string.count("u")
E =string.count("e")

true = T+R+U+E
#print(count1)

L = string.count("l")
O = string.count("o")
V = string.count("v")
E = string.count("e")

love = L+O+V+E

#print(f"{count1}{count2}")
final = str(true)+ str(love)

#print(final)
love_score = int(final)

if love_score <= 10 or love_score>= 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.") 

elif 40<love_score<50:
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")
