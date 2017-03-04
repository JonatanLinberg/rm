#!/usr/bin/env python3.6

from tkinter import *

root = Tk()

#const
sqside = 50
xsq = 8
ysq = 8

wwidth = xsq * sqside
wheight = ysq* sqside

#declare arrays
square = [["" for y in range(ysq)] for x in range(xsq)]

#Player
px = 0
py = 0

w = Canvas(root, width=wwidth, height=wheight, highlightthickness=0)
w.pack()

def move(event)
	

root.bind('<Up>', move)
root.bind('<Down>', move)
root.bind('<Left>', move)
root.bind('<Right>', move)


root.focus_set()

init()
mainloop()