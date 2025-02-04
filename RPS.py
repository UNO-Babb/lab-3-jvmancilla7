#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  computer= random.choice(["R","P","S"])
  player= input("Pick your weapon (R, P, S): ")
  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  if computer == "R" :
    print("computer chose Rock")
  elif computer == "P" :
    print("computer chose Paper")
  else:
    print("Computer chose Scissors")

  if player == "R" :
    print("player chose Rock")
  elif player== "P" :
    print("player chose Paper")
  else:
    print("player chose Scissors")
  if player == "R" and computer == "R":
    print("tie")
    ties= ties + 1
  if player == "R" and computer == "P":
    print("computer wins.")
    losses = losses + 1
  if player == "R" and computer == "S":
    print("you win.")
    wins= wins + 1

  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
