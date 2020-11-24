import random
import time
from tkinter import Tk , Button , DISABLED


def showsym(x,y):
    global first
    global px , py
    butt[x,y]['text'] = butts[x,y]
    butt[x,y].update_idletasks()

    if first:
        px = x
        py = y
        first = False
    elif px != x or py != y:
        if butt[px,py]['text'] != butt[x,y]['text']:
            time.sleep(1.5)
            butt[px,py]['text'] = ' '
            butt[x,y]['text'] = ' '
        else:
            butt[px,py]['command'] = DISABLED
            butt[x,y]['command'] = DISABLED
        first = True



win = Tk()
win.title("GTAV")
win.resizable(width=False , height=False)
first =  True
px = 0
py = 0

butt = { }
butts = { }
symb = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
        u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728' ]


random.shuffle(symb)

for x in range(6):
    for y in range(4):
        but = Button(command = lambda x=x , y=y: showsym(x,y) , width = 10, height = 8)
        but.grid(column = x , row = y)
        butt[x,y] = but
        butts[x,y] = symb.pop()


win.mainloop()