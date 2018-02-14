"""Let's play rock-paper-scissors, or as it's called in Japan, jan-ken-po. This program will simulate a game of rock paper scissors that you'd play with your friend, but in this version, you don't have to have any friens at all!"""
#need to import function for rps
from random import randint
#sleep will be to help build suspense
from time import sleep

options = ["R", "P", "S"]
LOSS_MESSAGE = "You lose! Better luck next time"
WIN_MESSAGE = "Congrats! You got lucky!"
DRAW_MESSAGE = "Hmmmm. Let's go again!"

def decide_winner(user_choice, computer_choice):
  print "You select: %s" % user_choice
  # print message here
  # now sleep for 2 seconds for suspense
  sleep(2)
  print "And the computer chooses: %s" % computer_choice
  # now sleep for 2 seconds
  sleep(2)
  
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
 
  if user_choice_index == 0 and computer_choice_index == 2:
    print WIN_MESSAGE
  elif user_choice_index == 1 and computer_choice_index == 0:
    print WIN_MESSAGE
  elif user_choice_index == 2 and computer_choice_index == 1:
    print WIN_MESSAGE
  elif user_choice_index > 2:
    print "Hey, you can't do that!"
  else:
    print LOSS_MESSAGE
    
def play_RPS():
  print "Rock, Paper, or Scissors?"
  user_choice = raw_input("Select R for Rock, P for paper, or S for Scissors: ")
  user_choice = user_choice.upper()
  sleep(2)
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)
  print "Play again?"
  response = raw_input("Y or N: ")
  response = response.upper()
  if response == "Y":
    return play_RPS()
  else:
    print "Goodbye!"
    return
             
play_RPS()