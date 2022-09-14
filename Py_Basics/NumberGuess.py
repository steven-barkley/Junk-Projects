##Step 1-7
"""Dice Twice - this software will compare user input to a sum of two dice rolls and determine a winner if the user's input is greater than the total value of both random dice"""
# Import and use library functions
from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(input("What is your guess : "))
  return user_guess


##Step 8-15
def roll_dice(number_of_sides):
  first_roll = randint (1, number_of_sides)
  second_roll = randint (1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum value is: " + str(max_val))
  sleep(1)
##Step 16-21
  user_guess = get_user_guess()
  if user_guess > max_val:
    print ("Over the limit! Try again.")
    return
  else:
    print("Rolling...")
    sleep(2)
    print ("The first value is: %d" % (first_roll))
    sleep(1)
    print("The second value is: %d" % (second_roll))
    sleep(1)
#Step 22-27
    total_roll = first_roll + second_roll
    print (total_roll)
    print ("Result....")
    sleep(1)
    if user_guess > total_roll:
      print("You WIN!" +" "+ "May the odds ever be in your favor!")
    else:
      print("You LOSE!" + " " "May the odds ever be in your favor!")
roll_dice(6)
