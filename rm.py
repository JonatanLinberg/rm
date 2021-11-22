#!/Users/jonatanlinberg/.pyenv/versions/3.6.12/bin/python
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import font as tkFont
from time import sleep
from random import randint
import sys
import platform
from pygame import mixer

resourcePath = sys.path[0]+'/rsrc/'

def getResourcePath(file):
	return resourcePath + file

if (platform.system() == "Darwin"):		#Inside MacOS Application
	from AppKit import NSBundle
	if (NSBundle.mainBundle().bundleIdentifier() == "grattis_rasmus"):
		resourcePath = str(NSBundle.mainBundle().resourcePath() + '/')

win_w, win_h = 400, 300
intro_speed = 10

root = tk.Tk()
root.title("Grattis Rasmus")
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

_txtclr = (219, 15, 135)
txtclr = list(_txtclr)
pts_txt = canvas.create_text(win_w/2, 0, font=tkFont.Font(family='Arial', size=28, weight='bold'), justify=tk.LEFT)

cake_ids = [-1 for c in range(0, 7)]
for i, _ in enumerate(cake_ids):
	cake_ids[i] = canvas.create_image(60+i*40, 100, anchor='nw', image=img_cake, state='hidden')

head_id = canvas.create_image(0, 0, anchor='nw', image=img_head)

def getColourFor(r, g, b):
	return "#" + ("%x" % (int(r) % 256)).zfill(2) + ("%x" % (int(g) % 256)).zfill(2) + ("%x" % (int(b) % 256)).zfill(2)

def update_pts_label():
	global points
	canvas.itemconfigure(pts_txt, text="You have eaten %d cakes." % points)

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

def handle_esc(e):
	global running
	if (running):
		gameOver()
	else:
		root.quit()

def handle_space(e):
	global running
	if (running):
		eat()
	else:
		startGame()

def eat():
	global pos, points, cakeArray, cakecount, running
	if cakeArray[pos] == False:
		gameOver()
	else:
		eat_sound.play()
		cakeArray[pos] = False
		points += 1
		canvas.itemconfigure(cake_ids[pos], state='hidden')

	cakecount -= 1

def gameOver():
	global running
	running = False


def show_game_over():
	if (messagebox.askyesno("Game Over", "You ate " + str(points) + " cakes.\nWould you like to play again?")):
		initGame()
	else:
		root.quit()

def initGame():
	global pos, count, cakeArray, points, cakecount, running, win_h, in_intro, txtclr, _txtclr
	pos = 3
	count = 1
	cakeArray = [False for c in range(0, 7)]
	points = 0
	cakecount = 0
	running = False
	in_intro = False
	txtclr = list(_txtclr)

	## reset graphics
	canvas.itemconfigure(pts_txt, text="Press SPACE to play!", fill=getColourFor(*txtclr))
	_, pth = canvas.coords(pts_txt)
	canvas.move(pts_txt, 0, win_h/2-pth)
	for i in range(len(cakeArray)):
		canvas.itemconfigure(cake_ids[i], state='hidden')
	hx, hy = canvas.coords(head_id)
	canvas.move(head_id, 180-hx, win_h-hy)

def startGame():
	global in_intro, running
	if (not running and not in_intro):
		in_intro = True
		update_pts_label()
		intro_loop()

def intro_loop():
	global running, in_intro, txtclr
	_, h = canvas.coords(head_id)
	if (h > 180): # should be 120 times
		canvas.move(head_id, 0, -1)
		canvas.move(pts_txt, 0, 1)
		
		#	
		txtclr = [(txtclr[0]+0.3), (txtclr[1]+2), (txtclr[2]+1)]
		canvas.itemconfigure(pts_txt, fill=getColourFor(*txtclr))
		
		root.after(intro_speed, intro_loop)
	else:
		in_intro = False
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
		root.after(20, loop)
	else:
		show_game_over()

root.bind('<Left>', Left)
root.bind('<Right>', Right)
root.bind('<space>', handle_space)
root.bind('<Escape>', handle_esc)

initGame()
root.focus_set()
mixer.music.play(-1)
root.mainloop()
