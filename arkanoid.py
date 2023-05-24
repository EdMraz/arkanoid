import tkinter as tk
win = tk.Tk()

win.title("Arkanoid")
def destroy_brick():
    global movement
    coord_ball = canvas.coords(ball)
    items_list = canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
    for i in items_list:
        if i in bricks:
            x = canvas.coords(i)
            bricks.remove(i)
            canvas.delete(i)
            if coord_ball[0] >= x[2]:
                movement = [movement[0]*-1, movement[1]]
            elif coord_ball[1] >= x[3]:
                movement = [movement[0], movement[1]*-1]
            elif coord_ball[2] <= x[0]:
                movement = [movement[0]*-1, movement[1]]
            elif coord_ball[3] <= x[1]:
                movement = [movement[0], movement[1]*-1]


def obstacle1():
    global movement
    coord_ball = canvas.coords(ball)
    items_list = canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
    for a in items_list:
        if a in obs1:
            x = canvas.coords(a)
            if coord_ball[0] >= x[2]:
                movement = [movement[0]*-1, movement[1]]
            elif coord_ball[1] >= x[3]:
                movement = [movement[0], movement[1]*-1]
            elif coord_ball[2] <= x[0]:
                movement = [movement[0]*-1, movement[1]]
            elif coord_ball[3] <= x[1]:
                movement = [movement[0], movement[1]*-1]

def obstacle2():
    global movement
    coord_ball = canvas.coords(ball)
    items_list = canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
    for aa in items_list:
        if aa in obs2:
            x = canvas.coords(aa)
            if coord_ball[0] >= x[2]:
                movement = [movement[0]*-1, movement[1]]
            elif coord_ball[1] >= x[3]:
                movement = [movement[0], movement[1]*-1]
            elif coord_ball[2] <= x[0]:
                movement = [movement[0]*-1, movement[1]]
            elif coord_ball[3] <= x[1]:
                movement = [movement[0], movement[1]*-1]

def ball_move():
    global ball, movement, desk
    canvas.move(ball, movement[0], movement[1])
    destroy_brick()
    pos = canvas.coords(ball)
    desk_pos = canvas.coords(desk)
    overlap = canvas.find_overlapping(desk_pos[0], desk_pos[1], desk_pos[2], desk_pos[3])
    if pos[2] >= w:     # prava hranica
        movement = [movement[0] * -1, movement[1]]
    elif pos[3] >= h:  # spodna hranica
        canvas.delete('all')
        text = canvas.create_text(w//2, h//2, text='Prehral si!',font="arial 20 bold",fill="white")
    elif pos[0] <= 0:       # lava hranica
        movement = [movement[0] * -1, movement[1]]
    elif pos[1] <= 0:       # vrchna hranica
        movement = [movement[0], movement[1] * -1]
    elif ball in overlap:
        movement = bounce(pos, desk_pos)
    if len(bricks) == 0:
        canvas.delete('all')
        canvas.create_text(w//2,h//2,text="Vyhral si",font="arial 20 bold",fill="white")
    obstacle1()
    obstacle2()
    canvas.after(4, ball_move)



def bounce(ball_pos, rec_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    rec_middle = (rec_pos[0] + rec_pos[2])//2
    ball_to_rec = ball_pos - rec_middle
    return [ball_to_rec//(rec_w//3), -1]


def starter(e):
        ball_move()

def move_right(e):
        canvas.move(desk,30,0)


def move_left(e):
        canvas.move(desk,-30,0)


def prepare_bricks():
    for y in range(brick_count_y):
        for x in range(w//brick_w):
            bricks.append(canvas.create_rectangle(x*brick_w,y*brick_h,x*brick_w+brick_w, y*brick_h+brick_h, fill = colours[y%brick_count_y],  width=5, outline="black"))


colours = ["purple", "spring green", "turquoise"]

#width, height
w = 550
h = 400
rec_w = 25
canvas = tk.Canvas(width = w, height = h, bg = "black")
canvas.pack()

movement = [0,1]

brick_count_x = 10
brick_count_y = len(colours)
brick_w = w//brick_count_x
brick_h = 40

bricks = []

obs1 = []
obs2 = []

ball = canvas.create_oval(w//2-10,h//2-10,w//2+10,h//2+10, fill="white",outline="black",width=2)
desk = canvas.create_rectangle(w/2-40, h-15, w/2+40, h, fill="white",outline="black",width=2)

obs1.append(canvas.create_rectangle(w/2-190,h/2-30,w/2-70,h/2-50, fill="light grey",outline="dark grey",width=4))
obs2.append(canvas.create_rectangle(w/2+190,h/2,w/2+65,h/2-20, fill="light grey",outline="dark grey",width=4))

prepare_bricks()

win.bind("<space>", starter)

win.bind("<Right>",move_right)
win.bind("<Left>",move_left)

win.mainloop()
