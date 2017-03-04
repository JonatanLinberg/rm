#!/usr/bin/env python3.6

from tkinter import *
from tkinter import messagebox

root = Tk()

#const
sqside = 50
xsq = 8
ysq = 8
loadedchunks = 9

wwidth = xsq * sqside
wheight = ysq* sqside

#declare arrays
chunk = [[["" for y in range(ysq)] for x in range(xsq)] for c in range(loadedchunks)]

#Player
px = 0
py = 0

w = Canvas(root, width=wwidth, height=wheight, highlightthickness=0)
w.pack()

def move(event):
	print ("hej")

def genWorld():
	for c in range(loadedchunks):
		for x in range(xsq):
			for y in range(ysq):
				chunk[c][x][y] = (str(c) + str(x) + str(y))


def init():
	genWorld()
	print ("chunk " + chunk[3][2][1])

def pause(event):
	if (messagebox.askquestion('Please don\'t go','Are you sure you want to exit?')=='yes'):
		sys.exit()

	
root.bind('<Escape>', pause)
root.bind('<Up>', move)
root.bind('<Down>', move)
root.bind('<Left>', move)
root.bind('<Right>', move)


root.focus_set()

init()
mainloop()