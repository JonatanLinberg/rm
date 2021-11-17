#!/Users/jonatanlinberg/.pyenv/versions/3.6.12/bin/python
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from time import sleep
from random import randint
import sys
import platform
from pygame import mixer

resourcePath = sys.path[0]+'/rsrc/'

def getResourcePath(file):
	return resourcePath + file

def MacOS_App_GetResourcePath(file):
	file = NSBundle.mainBundle().pathForResource_ofType_(file.split('.')[0], file.split('.')[1])
	return file

if (platform.system() == "Darwin" and sys.path[0].split('/')[-1] == "MacOS"):		#Inside MacOS Application
	from AppKit import NSBundle
	getResourcePath = MacOS_App_GetResourcePath
	
pos = 3
count = 1
cakeArray = [False for c in range(0, 7)]
points = 0
cakecount = 0
running = False
win_w, win_h = 400, 300
intro_speed = 10

root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("%dx%d" % (win_w, win_h))

mixer.pre_init(44100, -16, 2, 4096)
mixer.init()
mixer.music.load(getResourcePath("mus.wav"))

eat_sound = mixer.Sound(getResourcePath("eat.wav"))

img_head = ImageTk.PhotoImage(Image.open(getResourcePath("rasmus.png")).convert('RGBA'))
img_cake = ImageTk.PhotoImage(Image.open(getResourcePath("cake.png")).convert('RGBA'))
img_bg = ImageTk.PhotoImage(Image.open(getResourcePath("bg.png")))

canvas = tk.Canvas(root, bd=0, highlightthickness=0, width=win_w, height=win_h)
canvas.pack()

bg_id = canvas.create_image(0, 0, anchor='nw', image=img_bg)

cake_ids = [-1 for c in range(0, 7)]
for i, _ in enumerate(cake_ids):
	cake_ids[i] = canvas.create_image(60+i*40, 100, anchor='nw', image=img_cake, state='hidden')

head_id = canvas.create_image(180, win_h, anchor='nw', image=img_head)

pts_str = tk.StringVar()
pts_str.set("You have eaten 0 cakes.")
pts_label = tk.Label(textvariable=pts_str)
pts_label.place(x=0, y=0)


def update_pts_label():
	global points
	pts_str.set("You have eaten %d cakes."%(points))

def Left(e):
	global pos, running
	if (running):
		if pos > 0:
			pos -= 1
			canvas.move(head_id, -40, 0)

def Right(e):
	global pos, running
	if (running):
		if pos < 6:
			pos += 1
			canvas.move(head_id, 40, 0)

def eat(e):
	global pos, points, cakeArray, cakecount, running
	if (running):
		if cakeArray[pos] == False:
			gameOver()
		else:
			eat_sound.play()
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
	global running
	_, h = canvas.coords(head_id)
	if (h > 200):
		canvas.move(head_id, 0, -1)
		root.after(intro_speed, startGame)
	else:
		running = True
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
