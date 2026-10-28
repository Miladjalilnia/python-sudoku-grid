import turtle
import random

turtle.speed(8)
turtle.shape("turtle")

for i in range(10):
        if i in (0, 9):
                    turtle.pensize(5)
        elif i in (3, 6):
                    turtle.pensize(3)
        else:
                    turtle.pensize(1)

        y = -180 + i * 40
        turtle.penup()
        turtle.goto(-180, y)
        turtle.pendown()
        turtle.goto(180, y)

for i in range(10):
        if i in (0, 9):
                    turtle.pensize(5)
        elif i in (3, 6):
                    turtle.pensize(3)
        else:
                    turtle.pensize(1)

        x = -180 + i * 40
        turtle.penup()
        turtle.goto(x, -180)
        turtle.pendown()
        turtle.goto(x, 180)
turtle.penup()
turtle.color("black")

rows = [set() for _ in range(9)]
cells = set()

while len(cells) < 15:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if (row, col) in cells:
                continue

        available = [
                n for n in range(1, 10)
                if n not in rows[row]
                   ]

        if not available:
                continue

        number = random.choice(available)
        cells.add((row, col))
        rows[row].add(number)

        turtle.goto(-160 + col * 40, 152 - row * 40)
        turtle.write(
                number,
                align="center",
                font=("Arial", 18, "normal")
        )

turtle.hideturtle()
turtle.done()
