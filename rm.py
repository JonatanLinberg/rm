#!/usr/bin/env python2.7
from Tkinter import *
from random import randint
import tkMessageBox
from os import system
import sys

if (sys.path[0].split('/')[-1] == "MacOS"):		#Inside MacOS Application
	resourcePath = '/'.join(sys.path[0].split('/')[:-1]) + '/Resources/'
else:
	resourcePath = sys.path[0]+'/rsrc/'
pos = 3
count = 1
cakeArray = [False for c in range(0, 7)]
points = 0
cakecount = 0
running = True

root = Tk()
root.resizable(width=False, height=False)
root.geometry("400x300")

img = PhotoImage(file = resourcePath + "rasmus.gif")
cake = PhotoImage(file = resourcePath + "cake.gif")
bg = PhotoImage(file = resourcePath + "bg.gif")

bgl = Label(image=bg, width = 400, height = 300)
bgl.image = bg # keep a reference!
bgl.pack()

label = Label(image=img, width = 40, height = 40)
label.image = img # keep a reference!

cl0 = Label(image=cake, width = 40, height = 40)
cl0.image = cake

cl1 = Label(image=cake, width = 40, height = 40)
cl1.image = cake

cl2 = Label(image=cake, width = 40, height = 40)
cl2.image = cake

cl3 = Label(image=cake, width = 40, height = 40)
cl3.image = cake

cl4 = Label(image=cake, width = 40, height = 40)
cl4.image = cake

cl5 = Label(image=cake, width = 40, height = 40)
cl5.image = cake

cl6 = Label(image=cake, width = 40, height = 40)
cl6.image = cake


pts_str = StringVar()
pts_label = Label(textvariable=pts_str)
pts_label.place(x=0, y=0)


def update_pts_label():
	global points
	pts_str.set("You have eaten %d cakes."%(points))

def Left(e):
	global pos
	if pos > 0:
		pos -= 1

def Right(e):
	global pos
	if pos < 6:
		pos += 1

def eat(e):
	global pos, points, cakeArray, cakecount
	if cakeArray[pos] == False:
		gameOver()
	else:
		cakeArray[pos] = False
		points += 1
	if pos == 0:
		cl0.place_forget()
	if pos == 1:
		cl1.place_forget()
	if pos == 2:
		cl2.place_forget()
	if pos == 3:
		cl3.place_forget()
	if pos == 4:
		cl4.place_forget()
	if pos == 5:
		cl5.place_forget()
	if pos == 6:
		cl6.place_forget()
	cakecount -= 1

def quit(e):
	gameOver()

def gameOver():
	global running
	running = False
	tkMessageBox.showinfo("Game Over", "You ate " + str(points) + " cakes.")
	root.quit()

def loop():
	global label, count, cakeArray, points, cakecount, running
	if running:
		if cakecount == 7:
			gameOver()
		count -= 1
		if count <= 0:
			count = randint(20, 50)/(0.05 * points + 1) + randint(10, 20)

			while (True):
				r = randint(0, 6)
				if cakeArray[r] == False:
					break

			if r == 0:
				cl0.place(x = 60, y = 100)
			if r == 1:
				cl1.place(x = 100, y = 100)
			if r == 2:
				cl2.place(x = 140, y = 100)
			if r == 3:
				cl3.place(x = 180, y = 100)
			if r == 4:
				cl4.place(x = 220, y = 100)
			if r == 5:
				cl5.place(x = 260, y = 100)
			if r == 6:
				cl6.place(x = 300, y = 100)
			cakecount += 1
			cakeArray[r] = True	

		label.place(x = 60 + (pos * 40), y = 200)
		update_pts_label()

		root.after(20, loop)

root.bind('<Left>', Left)
root.bind('<Right>', Right)
root.bind('<space>', eat)
root.bind('<Escape>', quit)

system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
root.focus_set()
root.after(100, loop)
mainloop()
