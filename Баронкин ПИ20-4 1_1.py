from tkinter import *
from math import sin, cos, radians

WIDTH = 600
HEIGHT = 600
SPEED = 600


def animate():
    global angle
    x = x0 + R * cos(radians(angle))
    y = y0 + R * sin(radians(angle))
    canvas.coords(point, x - r, y - r, x + r, y + r)
    angle += SPEED / 1000
    root.after(1, animate)


if __name__ == '__main__':
    root = Tk()
    canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='#6666ff')
    canvas.pack()
    x0 = WIDTH // 2
    y0 = HEIGHT // 2
    R = HEIGHT // 3
    r = 13
    angle = 0
    circle = canvas.create_oval(x0 - R, y0 - R, x0 + R, y0 + R)
    point = canvas.create_oval(0, 0, 0, 0, fill='Red')
    animate()
    root.mainloop()