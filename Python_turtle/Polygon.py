# Python program to draw hexagon 
import turtle  
polygon = turtle.Turtle() 
  
n_sides = 6
side_length = 70
angle = 360.0 / n_sides  
  
for i in range(n_sides): 
    polygon.forward(side_length) 
    polygon.right(angle) 
    
turtle.exitonclick()