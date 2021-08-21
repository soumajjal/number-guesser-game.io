import random
i=0
j=0
exact= random.randint(0,100)
while (i>=0):
    while(j>=0):
      num = int(input("enter your guess number:\n"))
    #   print(exact) 
      j= j+1
      print("NO OF TURNS LEFT \n",10-j)
      if( num > exact):
          print("go less")
      if(num == exact):
          print("BINGO \n right guess")
          break
      if(num< exact):
          print("go high")
      if(j>10):
          print("GAME OVER!\n NO MORE GUESSES")            
          break
i=i+1
