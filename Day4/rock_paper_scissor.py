rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#print(rock)
print("Welcome to game!!!!")
in1 = input("Choose Rock,paper or scissors.... 0 for rock,1 for paper and 2 for scissors.")
player_in = int(in1)

print(player_in)
if player_in == 0:
  print(rock)
elif player_in == 1:
  print(paper)
elif player_in == 2:
  print(scissors)
#computer input
import random

arr = [rock,paper,scissors]

index = random.randint(0,2)
print("Player2")
print(arr[index])

#game conditions*******
if player_in == index:
  print("No one wins!!its Draw.")
elif player_in == 0 and index == 2:
  print("You Win..!!🥳🥳🥳🥳🥳")
elif player_in == 2 and index == 1:
  print("You Win..!!🥳🥳🥳🥳🥳")
elif player_in == 1 and index == 0:
  print("You Win..!!🥳🥳🥳🥳🥳")
else:
  print("You lose.😔😔")




