#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from time import sleep
from random import randint
import sys
from pygame import mixer

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
win_w, win_h = 400, 300
intro_speed = 10

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("%dx%d" % (win_w, win_h))

mixer.pre_init(44100, -16, 2, 4096)
mixer.init()
mixer.music.load(resourcePath + "mus.wav")

img_head = tk.PhotoImage(file = resourcePath + "rasmus.gif")
img_cake = tk.PhotoImage(file = resourcePath + "cake.gif")
img_bg = tk.PhotoImage(file = resourcePath + "bg.gif")

canvas = tk.Canvas(root, bd=0, highlightthickness=0, width=win_w, height=win_h)
canvas.pack()

bg_id = canvas.create_image(0, 0, anchor='nw', image=img_bg)

cake_ids = [-1 for c in range(0, 7)]
for i, _ in enumerate(cake_ids):
	cake_ids[i] = canvas.create_image(60+i*40, 100, anchor='nw', image=img_cake, state='hidden')

head_id = canvas.create_image(180, win_h, anchor='nw', image=img_head)

pts_str = tk.StringVar()
pts_label = tk.Label(textvariable=pts_str)
pts_label.place(x=0, y=0)


def update_pts_label():
	global points
	pts_str.set("You have eaten %d cakes."%(points))

def Left(e):
	global pos
	if pos > 0:
		pos -= 1
		canvas.move(head_id, -40, 0)

def Right(e):
	global pos
	if pos < 6:
		pos += 1
		canvas.move(head_id, 40, 0)

def eat(e):
	global pos, points, cakeArray, cakecount
	if cakeArray[pos] == False:
		gameOver()
	else:
		cakeArray[pos] = False
		points += 1
		canvas.itemconfigure(cake_ids[pos], state='hidden')

	cakecount -= 1

def quit(e):
	gameOver()

def gameOver():
	global running
	running = False
	messagebox.showinfo("Game Over", "You ate " + str(points) + " cakes.")
	root.quit()

def startGame():
	_, h = canvas.coords(head_id)
	if (h > 200):
		canvas.move(head_id, 0, -1)
		root.after(intro_speed, startGame)
	else:
		root.after(20, loop)

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
			canvas.itemconfigure(cake_ids[r], state='normal')

			cakecount += 1
			cakeArray[r] = True	

		update_pts_label()
		#paint canvas

		root.after(20, loop)

root.bind('<Left>', Left)
root.bind('<Right>', Right)
root.bind('<space>', eat)
root.bind('<Escape>', quit)

root.focus_set()
root.after(100, startGame)
mixer.music.play(-1)
root.mainloop()
