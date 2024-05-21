import turtle

from random import randint

number_of_turtle = 10
steps_of_the_time_number = 100
pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtle)]

for unit in pool:
    unit.penup()
    unit.speed(randint(0, 10))
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.seth(randint(0, 360))
for i in range(steps_of_the_time_number):
    for g in range(len(pool)):
        angle1 = pool[g].heading()
        x1, y1 = pool[g].pos()
        for h in range(len(pool)):
            if g != h:
                x2, y2 = pool[h].pos()
                angle2 = pool[h].heading()
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                if dx <= 3 and dy <= 3:
                    pool[h].seth(-angle2)
                    pool[g].seth(-angle1)
                    pool[h].forward(5)
                    pool[g].forward(5)
        if x1 < -200 or x1 > 200:
            pool[g].seth(180 - angle1)
        elif y1 < -200 or y1 > 200:
            pool[g].seth(-angle1)
        pool[g].fd(5)