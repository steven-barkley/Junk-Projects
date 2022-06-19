#Purpose of AreaCalculator.py is to automate the area calculation of two shapes: circle and triangle.

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print ("The Calc is starting now.....")
print ("\n")
print ("%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute))

sleep(1)

hint = ("Don't forget to include the correct units! Exiting...")

option = raw_input("Enter C for Circle or T for Triangle:")

option = option.upper()

if option == "C":
  radius = float(input("Input the radius:"))
  area = radius * pi**2
  print ("The pie is baking")
  sleep(2)
  print (area, hint)

elif option == "T":
  base = float(input("Enter base:"))
  height = float(input("Enter height:"))
  area = .5 * base * height
  print ("Uni Bi Tri...")
  sleep(2)
  print (area, hint)

else:
  print ("You entered an invalid value!")
