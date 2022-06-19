
import turtle
import random
import math

sc = turtle.Screen()
tim = turtle.Turtle()
ray = turtle.Turtle()

tim.color('blue')
tim.speed(8)
ray.color('red')
ray.speed(8)

def rd(x,y):
   return random.randrange(x,y)

def move_turtle(tut):
   tut.pd()
   tut.left( rd(-180,180))
   tut.forward( rd(-100,100))
   tut.pu()

def cross_boundary(x,y,tut):
   if math.fabs(tut.xcor()) > x or math.fabs(tut.ycor()) > y:
       return True

x_cor = sc.window_width()/2
y_cor = sc.window_height()/2

tim.goto( rd(-x_cor,x_cor), rd(-y_cor,y_cor))
ray.goto( rd(-x_cor,x_cor), rd(-y_cor,y_cor))

cont=True

while cont:
   move_turtle(tim)
   move_turtle(ray)
   if cross_boundary(x_cor,y_cor,tim) or cross_boundary(x_cor,y_cor,ray):
       cont=False

print('END OF RACE')

x_cor = sc.window_width()
y_cor = sc.window_height()

tim.goto(rd(x_cor,x_cor), rd(y_cor,y_cor))
ray.goto(rd(x_cor,x_cor), rd(y_cor,y_cor))

cont=True

while cont:
    move_turtle(tim)
    move_turtle(ray)
    if cross_boundary(x_cor, y_cor, tim) or cross_boundary(x_cor, y_cor, ray):
        cont=False

print('End of RACE')