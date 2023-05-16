import tkinter as tk
win = tk.Tk()

win.title("Arkanoid")
def destroy_brick():
    global movement
    coord_ball = canvas.coords(ball)
    items_list = canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
    for i in items_list:
        if i in bricks:
            if movement[0] > 0 and movement[1] < 0:
                movement = [movement[0]*(1), movement[1]*(1)]
            if movement[0] > 0 and movement[1] > 0:
                movement = [movement[0]*(1), movement[1]*(-1)]
            if movement[0] < 0 and movement[1] < 0:
                movement = [movement[0]*(-1), movement[1]*(1)]
            if movement[0] < 0 and movement[1] > 0:
                movement = [movement[0]*(-1), movement[1]*(1)]
            bricks.remove(i)
            canvas.delete(i)


# def obstacles():
#     global movement
#     coord_ball = canvas.coords(ball)
#     items_list = canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
#     for i in items_list:
#         if i in obs1 or obs2:
#             if movement[0] > 0 and movement[1] < 0:
#                 movement = [movement[0]*(1), movement[1]*(1)]
#             elif movement[0] > 0 and movement[1] > 0:
#                 movement = [movement[0]*(1), movement[1]*(-1)]
#             elif movement[0] < 0 and movement[1] < 0:
#                 movement = [movement[0]*(-1), movement[1]*(1)]
#             elif movement[0] < 0 and movement[1] > 0:
#                 movement = [movement[0]*(-1), movement[1]*(1)]

def ball_move():
    global ball, movement, desk
    canvas.move(ball, movement[0], movement[1])
    pos = canvas.coords(ball)
    desk_pos = canvas.coords(desk)
    overlap = canvas.find_overlapping(desk_pos[0], desk_pos[1], desk_pos[2], desk_pos[3])
    if pos[2] >= w:     # prava hranica
        # movement = [-1, 1]
        movement = [movement[0] * -1, movement[1]]
        # faker(0)
    elif pos[3] >= h:  # spodna hranica
        canvas.delete('all')
        text = canvas.create_text(w//2, h//2, text='YOU LOST')
    elif pos[0] <= 0:       # lava hranica
        # movement = [1, -1]
        movement = [movement[0] * -1, movement[1]]
        # faker(0)
    elif pos[1] <= 0:       # vrchna hranica
        # movement = [1, 1]
        movement = [movement[0], movement[1] * -1]
        # faker(1)
    elif ball in overlap:
        # movement = [-1, -1]
        # faker(1)
        movement = bounce(pos, desk_pos)
    destroy_brick()
    canvas.after(4, ball_move)



def bounce(ball_pos, rec_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    rec_middle = (rec_pos[0] + rec_pos[2])//2
    ball_to_rec = ball_pos - rec_middle
    return [ball_to_rec//(rec_w//3), -1]    # rec_w//3 => vector x je 0-3


def starter(e):
        ball_move()

def move_right(e):
        canvas.move(desk,30,0)


def move_left(e):
        canvas.move(desk,-30,0)


def prepare_bricks():
    for y in range(brick_count_y):
        for x in range(w//brick_w):
            bricks.append(canvas.create_rectangle(x*brick_w,y*brick_h,x*brick_w+brick_w, y*brick_h+brick_h, fill = colours[y%brick_count_y],  width=5, outline="white"))


colours = ["purple","red", "yellow", "spring green", "blue", "orange"]

#width, height
w = 650
h = 450
rec_w = 25
canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.pack()
d=3
movement = [1*d,1*d]

brick_w = 65
brick_h = 20
brick_count_x = 10
brick_count_y = len(colours)
bricks = []

obs1 = []
obs2 = []

ball = canvas.create_oval(w/2-20,h/2-20,w/2,h/2, fill="white",outline="black",width=2)
desk = canvas.create_rectangle(w/2-70, h-10, w/2+70, h, fill="white",outline="black",width=2)

obs1.append(canvas.create_rectangle(w/2-190,h/2-30,w/2-70,h/2-50, fill="light grey",outline="dark grey",width=4))
obs2.append(canvas.create_rectangle(w/2+190,h/2,w/2+65,h/2-20, fill="light grey",outline="dark grey",width=4))

prepare_bricks()

win.bind("<space>", starter)

win.bind("<Right>",move_right)
win.bind("<Left>",move_left)

win.mainloop()
