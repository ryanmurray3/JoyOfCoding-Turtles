# Turtle Party Project
# By Ryan Murray
# Jan 12, 2025
# 3 separate programs so be sure to run only the portion you want

import turtle
import random

turtle.color("green")

random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
no_sides = 6
poly_len = 50

def polygon(no_sides, poly_Len):
  if no_sides < 3:
    print("Error: Less than three sides")
  else:
    for i in range(no_sides):
      turtle.forward(poly_len)
      turtle.right(360 / no_sides)

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def forward(len):
  turtle.penup()
  turtle.forward(len)
  turtle.pendown()
 
angle = 1/8 * 360
 
def repeat_function(polygon, times, no_sides, poly_len):
    for _ in range(times):
      turtle.color(random_color)
      turtle.penup()
      turtle.back(360 / no_sides)
      turtle.left(angle)
      turtle.pendown()
      polygon(no_sides, poly_len)

polygon(12, 50)
repeat_function(polygon, 12, no_sides, poly_len)
repeat_function(polygon, 12, no_sides, poly_len)

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
 
# forward helper function 
def move(len):
  back(-1 * len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)

spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)

for n in range(3, 10):
  move(50) # forward
  polygon(n, 100 / n)
  back(50)
  turtle.right(360 / 7)


