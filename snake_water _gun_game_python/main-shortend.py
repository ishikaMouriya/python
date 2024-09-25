import random
'''
1 for snake
-1 for water
0 for gun'''
print('''s:snake , g:gun , w:water''')
computer=random.choice([-1,0,1])
youstr=input("enter your choice between s,w,g:")
youDict = {"s" : 1,"w":-1, "g":0}
reverseDict ={1:"Snake",-1:"Water",0:"Gun"}#use for printing

if (youstr=="s" or youstr=="w" or youstr=="g"):
   you =youDict[youstr]
   #By now we have 2 numbers(variables),you and computer

   print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

   if (computer == you):
     print("It's a draw")
   else:
     if((computer -you)== 1 or (computer -you)==-2):
       print("You Win!!")
     else:
       print("You Lose")
else:
  print("Invalid choice.")
  
  
"""here we use computer-you logicas follows:
   for win we will only get -2 or
     1 else we will lose.
"""


