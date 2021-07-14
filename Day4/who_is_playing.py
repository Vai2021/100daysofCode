
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

l= len(names)
bill_payee = random.randint(0,l-1)
print(f"{names[bill_payee]} is going to buy meal today.")





