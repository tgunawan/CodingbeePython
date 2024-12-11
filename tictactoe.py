import os
card=[i+1 for i in range(9)]

def print_board():
   os.system('cls')
   for i in range(3):
      print("|",end=" ")
      for j in range(3):
         print(card [i*3+j],end=" | ")
      print()
      if i<2:
        print("-"*12)

print_board()

if card[0] == "O" and card[1] == "O" and card[2] == "O":
   print("O wins!")