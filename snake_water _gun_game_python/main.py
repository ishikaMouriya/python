import random
'''
1 for snake
-1 for water
0 for gun'''

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
    if(computer ==-1 and you==1):#-2 <-computer-you
     print("You win!")
    elif(computer ==-1 and you==0):#-1
     print("You Lose!")
    elif(computer ==-1 and you==0):#-1
     print("You Lose!")
    elif(computer ==1 and you==-1):#2
     print("You Lose!")
    elif(computer ==1 and you==0):#1
     print("You win!")
    elif(computer ==0 and you==1):#-1
     print("You lose!")
    elif(computer ==0 and you==-1):#1
     print("You win!")
    else:
      print("Something went wrong!")
else:
 print("Invalid choice")
 







