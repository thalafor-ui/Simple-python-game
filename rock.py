import random
print("Lets play a game:rock,paper,scissor")
choices=("rock","paper","scissor")
player_score=0
comp_score=0
while True:
 player=input("\nYou:  ").lower()
 if(player=="exits"):
  break
 computer=random.choice(choices)
 print("computer:",computer,"\n")
 if(player=="rock" and computer=="paper"):
     print("computer wins")
     comp_score+=1
 elif(player=="rock"and computer=="scissor"):
     print("You wins")
     player_score+=1
 elif(player=="paper"and computer=="rock"):
     print("You wins")
     player_score+=1
 elif(player=="paper"and computer=="scissor"):
     print("computer wins")
     comp_score+=1
 elif(player=="scissor"and computer=="rock"):
     print("computer wins")
     comp_score+=1
 elif(player=="scissor"and computer=="paper"):
     print("You wins")
     player_score+=1
 elif(player==computer):
     print("None of you wins,both are same")
 else:
     print("invalid choice")
 print(f"\nmy score: {player_score}\ncomputer score: {comp_score}")
print("\nGood bye") 
            