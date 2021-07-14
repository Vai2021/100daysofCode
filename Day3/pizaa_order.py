
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


Total_amt = 0

if size == 'S':
  Total_amt = 15
  if add_pepperoni == 'Y':
    Total_amt= Total_amt+2
    if extra_cheese =='Y':
      Total_amt= Total_amt+1
    else:
      Total_amt= Total_amt
  else:
    Total_amt= Total_amt
#print(Total_amt)

elif size == 'M':
  Total_amt = 20
  if add_pepperoni == 'Y':
    Total_amt = Total_amt+3
    if extra_cheese == 'Y':
      Total_amt = Total_amt+1
    else:
      Total_amt =  Total_amt
  else:
    Total_amt = Total_amt

elif size == 'L':
  Total_amt = 25
  if add_pepperoni == 'Y':
    Total_amt = Total_amt+3
    if extra_cheese == 'Y':
      Total_amt = Total_amt+1
    else:
      Total_amt = Total_amt
  else:
    Total_amt = Total_amt

print(f"Your final bill is: ${Total_amt}")








