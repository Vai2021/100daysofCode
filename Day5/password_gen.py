#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwrd = [ ]

for i in range(0,nr_letters):

  number_c = random.randint(0,len(letters)-1)
  #print(number_c)
  passwrd.append(letters[number_c])

#print(passwrd)

for j in range(0,nr_numbers):

  number_num = random.randint(0,len(numbers)-1)
  #print(number_num)
  passwrd.append(numbers[number_num])

for k in range(0,nr_symbols):

  number_sym = random.randint(0,len(symbols)-1)
  #print(number_sym)
  passwrd.append(symbols[number_sym])

#print(passwrd)
final_arr =[ ]
for p in range (0,len(passwrd)):

  final_pass = random.randint(0,len(passwrd)-1)
  final_arr.append(passwrd[final_pass])
  
print("".join(final_arr))
 
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P