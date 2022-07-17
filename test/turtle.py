# Python program to draw star
import turtle
star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
	star.right(144)
	star.forward(100)
	
turtle.done()
# Python program to draw hexagon
import turtle
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
	polygon.forward(side_length)
	polygon.right(angle)
	
turtle.done()


import turtle
t = turtle.Turtle()
t.speed(1)
t.shape("turtle")
t.color('blue', 'black')
t.fd(100)
t.rt(90)
t.fd(100)
t.lt(90)
t.bk(100)
t.lt(90)
t.fd(100)
t.lt(45)
t.bk(140)
t.rt(45)
t.penup()
t.fd(100)
t.pendown()
t.rt(45)
t.bk(140)
t.home()
t.goto(100, 100)
t.rt(90)
t.fd(100)
t.home()
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.lt(45)
t.bk(140)
t.penup()
t.home()
t.pendown()
turtle.done()
#Star
import turtle
t = turtle.Turtle()

t.rt(75)
t.fd(100)

for i in range(4):
	t.rt(144)
	t.fd(100)

turtle.done()
#Octagon
import turtle 
shape = turtle.Turtle()
shape.speed(10)
sides = 8
length = 100
angle = 360 / sides

for i in range(8):
	shape.forward(length)
	shape.rt(angle)
	
turtle.done()

#Right Triangle
import turtle 
t = turtle.Turtle()
t.rt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.home()
turtle.done()

import turtle 
shape = turtle.Turtle()
shape.speed(1)
sides = 5
length = 100
angle = 360 / sides

for i in range(5):
	shape.forward(length)
	shape.rt(angle)
	
turtle.done()

import turtle 
shape = turtle.Turtle()
shape.speed(1)
sides = 15
length = 100
angle = 360 / sides

for i in range(15):
	shape.forward(length)
	shape.rt(angle)
	
turtle.done()

import turtle as t
t.speed(0)
t.bgcolor('black')
t.pencolor('purple')
for i in range(220):
	t.rt(i)
	t.circle(120, i)
	t.fd(i)
	t.rt(90)
t.done()

import turtle as shape
shape.shape('turtle')
shape.speed(0)
shape.bgcolor('blue')
shape.pencolor('dark cyan')
for i in range(60):
	shape.rt(i)
	shape.circle(200)
	shape.fd(i)
	shape.rt(45)
shape.ht()
shape.done()

import turtle as t
t.speed(0)
for i in range(200):
	t.rt(i)
	t.circle(100)
t.done()

import turtle as t
t.bgcolor('dark blue')
t.pencolor('cyan')
for i in range(4):
	t.fd(100)
	t.lt(90)

t.goto(50, 50)

for i in range(4):
	t.fd(100)
	t.lt(90)

t.goto(150,50)
t.goto(100,0)
  
t.goto(100,100)
t.goto(150,150)

t.goto(50,150)
t.goto(0,100)
t.done()


import turtle as turt
tur = turtle.Screen()
tur.bgcolor("black")
turt = turtle.Turtle()
turt.color("blue")           

for i in range(4):
    turt.forward(100)
    turt.left(90)

turt.goto(50,50)
  
for i in range(4):
    turt.forward(100)
    turt.left(90)

turt.goto(150,50)
turt.goto(100,0)
  
turt.goto(100,100)
turt.goto(150,150)

turt.goto(50,150)
turt.goto(0,100)
turtle.done()
