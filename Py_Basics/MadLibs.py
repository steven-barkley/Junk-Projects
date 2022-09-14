"""
Program inserts string values into paragraph template and inserts variable values at given points to print the statement
"""
import time
print ("Starting up Mad Libs.....")
time.sleep(5)

user_name = input("What is your first name? ")

print ("Hello",user_name,"please follow instructions below. ")

adjective1 = input("Input a adjective1 ")
adjective2 = input("Input a adjective2 ")
adjective3 = input("Input a adjective3 ")

verb1 = input("Input a verb1 ")
verb2 = input ("Input a verb2 ")
verb3 = input("Input a verb3 ")

noun1 = input("Input a noun1 ")
noun2 = input("Input a noun2 ")
noun3 = input("Input a noun3 ")
noun4 = input("Input a noun4 ")

#More variables
animal = input("Input name of An animal ")
food = input("Input name of A food ")
fruit = input("Input name of A fruit ")
number = input ("Input name of A number ")
superhero = input("Input name of A superhero ")
country = input("Input name of A country ")
dessert = input("Input name of A dessert ")
year = input("Input name of Any year ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

#Order of the variables I chose
print (STORY % ( adjective1, user_name, verb1, adjective2, noun1, noun2, animal, food, verb2, noun3, fruit, adjective3, user_name, verb3, number, user_name, superhero, superhero, user_name, country, user_name, dessert, user_name, year, noun4))
