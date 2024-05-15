import turtle
turtle.speed(0)
for i in range(2, 100):
    turtle.circle(2*i)
    turtle.circle(-2*i)
    turtle.left(i)

turtle.exitonclick()