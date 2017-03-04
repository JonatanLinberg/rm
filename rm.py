#!/usr/bin/env python3.6

from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()

#const
sqside = 50
xsq = 9
ysq = 9
loadedchunks = 9

wwidth = xsq * sqside
wheight = ysq* sqside

#declare arrays
#'black' = wall
#'white' = open
#'gray' = cake
chunk = [[["" for y in range(ysq)] for x in range(xsq)] for c in range(loadedchunks)]

#'' = no wall
#'u' = wall up
#'l' = wall left
#'r' = wall right
#'d' = wall down
withwall = [[['' for y in range(ysq)] for x in range(xsq)] for c in range(loadedchunks)]

#Player
px = 4
py = 4

w = Canvas(root, width=wwidth, height=wheight, highlightthickness=0)
w.pack()

def paint():
	#ground
	for x in range(xsq):
		for y in range(ysq):
			w.create_rectangle(x*sqside, y*sqside, (x+1)*sqside, (y+1)*sqside, \
				fill = chunk[5][x][y], outline = 'black')
	w.create_oval(px*sqside, py*sqside, (px+1)*sqside, (py+1)*sqside, fill='blue')

def move(event):
	print ("struggling to move...")

def genWorld(c):
		for x in range(xsq):
			for y in range(ysq):
				#print('trying square ' + str(c) + str(x) + str(y))
				p=6
				if x > 0 and y > 0 and x < xsq-1 and y < ysq-1:
					if chunk[c][x-1][y] == 'black':
						p -= 2
						withwall[c][x-1][y] += 'r'
						if withwall[c][x-1][y] == 'l':
							p -=5
						if withwall[c][x-1][y] == 'd' or withwall[c][x-1][y] == 'u':
							p +=20
						print ('left ' + withwall[c][x-1][y])

					if chunk[c][x+1][y] == 'black':
						p -= 2
						withwall[c][x+1][y] += 'l'
						if withwall[c][x+1][y] == 'r':
							p -= 5
						if withwall[c][x+1][y] == 'd' or withwall[c][x+1][y] == 'u':
							p += 20
						print ('right ' + withwall[c][x+1][y])

					if chunk[c][x][y-1] == 'black':
						p -= 2
						withwall[c][x][y-1] += 'd'
						if withwall[c][x][y-1] == 'u':
							p -= 5
						if withwall[c][x][y-1] == 'r' or withwall[c][x][y-1] == 'l':
							p += 20
						print ('up ' + withwall[c][x][y-1])

					if chunk[c][x][y+1] == 'black':
						p -= 2
						withwall[c][x][y+1] += 'u'
						if withwall[c][x][y+1] == 'd':
							p -= 5
						if withwall[c][x][y+1] == 'r' or withwall[c][x][y+1] == 'l':
							p += 20
						print ('down ' + withwall[c][x][y+1])

				if p <= 0 or randint(0, p) == 0:
					chunk[c][x][y] = 'black'
				else:
					chunk[c][x][y] = 'white'
					if randint(0, 100)==0:
						chunk[c][x][y] = 'gray'
				print('Chunk ' + str(c) + '\n' + str(x) + str(y) +' is ' + chunk[c][x][y] + '\np =' + str(p) + '\n\n')
		chunk[5][4][4] = 'white'

def init():
	for c in range(loadedchunks):
		genWorld(c)
	paint()

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