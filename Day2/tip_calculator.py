input("Welcome to the tip calculator.")
total_bill=input("What was the total bill?")
tip_per= input("What percentage of tip would you like to give?10,12, or 15?")
people= input("How many people to split the bill?")
x= float(total_bill)
y= int(tip_per)
z= int(people)

bill = y/100 * x+ x
Each_person_bill = bill/z
print(Each_person_bill)
print("Each person should pay:")

#t=round(Each_person_bill,2)
t = "{:.2f}".format(Each_person_bill)
print(t)
