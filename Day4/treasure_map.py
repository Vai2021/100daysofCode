
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
hor = int(position[0])
ver = int(position[1])
map[ver][hor]= '🛎️'

print(f"{row1}\n{row2}\n{row3}")