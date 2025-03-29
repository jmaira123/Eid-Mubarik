import turtle
import random
import time

def draw_moon(x, y, size):
    turtle.penup()
    turtle.goto(x, y - size)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    
    # Crescent effect
    turtle.penup()
    turtle.goto(x + size * 0.4, y - size * 0.2)
    turtle.pendown()
    turtle.color("midnight blue")
    turtle.begin_fill()
    turtle.circle(size * 0.85)
    turtle.end_fill()

def draw_star(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_mosque():
    turtle.penup()
    turtle.goto(-150, -100)
    turtle.pendown()
    turtle.color("gold")
    turtle.pensize(3)
    
    # Mosque base
    turtle.begin_fill()
    turtle.goto(150, -100)
    turtle.goto(150, 0)
    turtle.goto(-150, 0)
    turtle.goto(-150, -100)
    turtle.end_fill()
    
    # Main dome
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(0, 80)
    turtle.goto(100, 0)
    turtle.goto(-100, 0)
    turtle.end_fill()
    
    # Minarets
    for x in [-140, 140]:
        turtle.penup()
        turtle.goto(x, -100)
        turtle.pendown()
        turtle.begin_fill()
        turtle.goto(x + 20, -100)
        turtle.goto(x + 20, 50)
        turtle.goto(x, 50)
        turtle.goto(x, -100)
        turtle.end_fill()

def draw_text():
    turtle.penup()
    turtle.goto(-90, -180)
    turtle.color("gold")
    turtle.pendown()
    turtle.write("Eid Mubarak", font=("Arial", 32, "bold"))

def draw_twinkle_stars():
    for _ in range(50):
        x = random.randint(-350, 350)
        y = random.randint(-50, 300)
        size = random.randint(3, 8)
        draw_star(x, y, size)

def setup_screen():
    turtle.bgcolor("dark blue")  # More attractive background color
    turtle.speed(0)

def main():
    setup_screen()
    draw_moon(-50, 120, 50)
    draw_twinkle_stars()
    draw_mosque()
    draw_text()
    turtle.hideturtle()
    turtle.done()

main()
