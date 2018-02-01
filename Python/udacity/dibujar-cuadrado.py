import turtle
def tortuga():
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color("yellow")
    tortuga.speed(10)
    for i in range(36): #36 veces = a 360º
        for e in range(4):
            tortuga.forward(100)
            tortuga.right(90)
        tortuga.right(10)
def dibujarcirculo():
    fondo = turtle.Screen()
    fondo.bgcolor("red")
    tortuga()
    fondo.exitonclick()
dibujarcirculo()