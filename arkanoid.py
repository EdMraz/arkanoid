import tkinter
import random

win = tkinter.Tk()
win.title("Arkanoid")

WIDTH = 600
HEIGHT = 500

canvas = tkinter.Canvas(width = WIDTH, height = HEIGHT, bg = "white")
canvas.pack()


movement = [10,10]

ball = canvas.create_oval(20,20,40,40, fill="black")


def move():
    global movement
    canvas.move(ball,movement[0],movement[1])
    if canvas.coords(ball)[0] < 0:
        movement[0] *= (-1)
    if canvas.coords(ball)[1] < 0:
        movement[1] *= (-1)
    if canvas.coords(ball)[2] > WIDTH:
        movement[0] *= (-1)
    if canvas.coords(ball)[3] > HEIGHT:
        movement[1] *= (-1)
    canvas.after(50,move)


move()

win.mainloop()
