
import turtle

t=turtle.Turtle()
s=turtle.Screen()
# s.bgcolor("#000000")
s.bgcolor("black") 
t.speed(11)

for _ in range(36):
    t.pencolor("blue")
    t.circle(170)
    t.left(13)

    t.pencolor("gray")
    t.circle(150)
    t.left(14)

    t.pencolor("red")
    t.circle(120)
    t.left(13)

    t.pencolor("green")
    t.circle(100)
    t.left(10)

    t.pencolor("yellow")
    t.circle(90)
    t.left(11)

    t.pencolor("white")
    t.circle(70)
    t.left(12)

turtle.done() 
