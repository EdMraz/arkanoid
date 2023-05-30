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
            if temp:
                if coord_ball[0] >= x[2]:
                    movement = [movement[0]*-1, movement[1]]
                elif coord_ball[1] >= x[3]:
                    movement = [movement[0], movement[1]*-1]
                elif coord_ball[2] <= x[0]:
                    movement = [movement[0]*-1, movement[1]]
                elif coord_ball[3] <= x[1]:
                    movement = [movement[0], movement[1]*-1]
            break


def obstacle1():
    global movement
    coord_ball = canvas.coords(ball)
    items_listt = canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
    for a in items_listt:
        if a in obs1:
            x = canvas.coords(a)
            if temp:
                if coord_ball[0] >= x[2]:
                    movement = [movement[0]*-1, movement[1]]
                elif coord_ball[1] >= x[3]:
                    movement = [movement[0], movement[1]*-1]
                elif coord_ball[2] <= x[0]:
                    movement = [movement[0]*-1, movement[1]]
                elif coord_ball[3] <= x[1]:
                    movement = [movement[0], movement[1]*-1]
            break


def obstacle2():
    global movement
    coord_bal = canvas.coords(ball)
    items_l = canvas.find_overlapping(coord_bal[0],coord_bal[1],coord_bal[2],coord_bal[3])
    for aa in items_l:
        if aa in obs2:
            y = canvas.coords(aa)
            if temp:
                if coord_bal[0] >= y[2]:
                    movement = [movement[0]*-1, movement[1]]
                elif coord_bal[1] >= y[3]:
                    movement = [movement[0], movement[1]*-1]
                elif coord_bal[2] <= y[0]:
                    movement = [movement[0]*-1, movement[1]]
                elif coord_bal[3] <= y[1]:
                    movement = [movement[0], movement[1]*-1]
            break

def ball_move():
    global ball, movement, desk, a
    canvas.move(ball, movement[0], movement[1])
    destroy_brick()
    pos = canvas.coords(ball)
    desk_pos = canvas.coords(desk)
    overlap = canvas.find_overlapping(desk_pos[0], desk_pos[1], desk_pos[2], desk_pos[3])
    if pos[2] >= w:     # prava hranica
        movement = [movement[0] * -1, movement[1]]
    elif pos[3] >= h:  # spodna hranica
        canvas.delete('all')
        a = False
        #canvas.delete('time')
        canvas.create_text(w//2, h//2, text='Prehral si!',font="arial 20 bold",fill="black")
    elif pos[0] <= 0:       # lava hranica
        movement = [movement[0] * -1, movement[1]]
    elif pos[1] <= 0:       # vrchna hranica
        movement = [movement[0], movement[1] * -1]
    elif ball in overlap:
        movement = bounce(pos, desk_pos)
    if len(bricks) == 0:
        canvas.delete('all')
        a = False
        canvas.create_text(w//2,h//2-20,text="Vyhral si!",font="arial 20 bold",fill="black")
        canvas.create_text(w//2,h//2+20,text="Tvôj čas: "+str(time)+" sekúnd",font="arial 20 bold",fill="black")
    obstacle1()
    obstacle2()
    canvas.after(2, ball_move)


def bounce(ball_pos, rec_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    rec_middle = (rec_pos[0] + rec_pos[2])//2
    ball_to_rec = ball_pos - rec_middle
    return [ball_to_rec//(rec_w//3), -1]


def starter(e):
        ball_move()
        timer()
        canvas.delete('start')

def move_right(e):
        canvas.move(desk,15,0)


def move_left(e):
        canvas.move(desk,-15,0)


def prepare_bricks():
    for y in range(brick_count_y):
        for x in range(w//brick_w):
            bricks.append(canvas.create_rectangle(x*brick_w,y*brick_h,x*brick_w+brick_w, y*brick_h+brick_h, fill = colours[y%brick_count_y],  width=5, outline="white"))

def timer():
    global time
    if a == True:
        time += 1
        canvas.delete('cas')
        canvas.create_text(520,330,text=time,font="Arial 20",tag='cas',fill="black")
        canvas.after(1000,timer)

colours = ["purple", "spring green", "turquoise"]

#width, height
w = 550
h = 350
rec_w = 25
canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.pack()
temp = True
a = True
movement = [0,10]

brick_count_x = 4
brick_count_y = len(colours)
brick_w = w//brick_count_x
brick_h = 40
time = 0
bricks = []

obs1 = []
obs2 = []

ball = canvas.create_oval(w//2-20,h//2-20,w//2+20,h//2+20, fill="white",outline="black",width=2)
desk = canvas.create_rectangle(w/2-60, h-15, w/2+60, h, fill="white",outline="black",width=2)

obs1.append(canvas.create_rectangle(w//2-190,h//2+10,w//2-70,h//2, fill="light grey",outline="dark grey",width=4))
obs2.append(canvas.create_rectangle(w//2+190,h//2,w//2+65,h//2-10, fill="light grey",outline="dark grey",width=4))
print(obs1)
print(obs2)

canvas.create_text(w//2,h//2+80,text="Press SPACE to start,\nmove with arrow keys",tag="start",fill="black",font="Arial 20")

prepare_bricks()
print(bricks)
win.bind("<space>", starter)

win.bind("<Right>",move_right)
win.bind("<Left>",move_left)

win.mainloop()
