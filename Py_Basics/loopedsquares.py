import turtle

s=turtle.Screen()

s.bgcolor("lightgreen")
leon=turtle.Turtle()
leon.color("hotpink")
leon.speed("normal")
leon.pensize(3)
leon.up()

leon.goto(-150,30)
def star(a):
    for move in range(5):
        a.left(-144)
        a.forward(80)

for i in range(5):
    leon.up()
    leon.forward(309)
    leon.down()
    star(leon)
    leon.left(-720/5)
s.exitonclick()
