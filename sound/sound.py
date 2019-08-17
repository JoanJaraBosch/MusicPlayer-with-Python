# Load the required library
from pygame import mixer #sound
from tkinter import * #gui
from tkinter import filedialog #search directories
from glob import glob #directoris
import pygame #sound with time
import time # to make sure to stop time to delete the thread
import os #directori
import threading #doing a thread to play music

	
#Fubction to search music in the actual directory and play it
def playMusic():
	global notPause
	global directory
	global close 
	mixer.init()
	
	for fitxer in glob(directory+"\*.mp3"):
		if(not close):
			mixer.music.load(fitxer)
			mixer.music.set_volume(1.0)
			mixer.music.play()
			print("You are listening "+fitxer.split('\\')[-1])
			i=0
			while mixer.music.get_busy(): 
				if(close):
					mixer.music.stop()
					break
					
				if(notPause and i == 1):
					mixer.music.unpause()
					i=0
					
				if(not notPause and i==0):
					mixer.music.pause()
					i=1
		else:
			mixer.music.stop()
			break
		
#Function to start the Thread			
def auxPlayMusic():
	global currentlyThread
	global close 
	global threads
	
	
	if(threads >0):
		close = True
		time.sleep(0.5)
		del currentlyThread
		close = False
		currentlyThread = threading.Thread(target=playMusic)
		
	threads = threads+1	
	currentlyThread.start()
	
#Function to search a Directory 	
def browse():
	global directory
	global threads
	
	directory = filedialog.askdirectory()
	if(threads >0):
		auxPlayMusic()

#Function to pause or unpause the music
def stopMusic():
	global currentlyThread
	global notPause 
	global btnPause
	
	if(notPause):
		btnPause.config(text='Unpause')
		notPause = False
	else:
		btnPause.config(text='Pause')
		notPause = True
	
#Function to stop and close the musci player with 0 errors	
def closeMusic():
	global close 
	close = True
	window.destroy()

#global variables
notPause = True
close = False
threads = 0
directory = os.getcwd()
currentlyThread = threading.Thread(target=playMusic)


#gui
window = Tk()
window.title("Jarr Music Player for Python") 
window.geometry('150x50')

btnPlay = Button(window, text="Play", command=auxPlayMusic)
btnPlay.grid(column=1, row=0)
btnPause = Button(window, text="Pause", command=stopMusic)
btnPause.grid(column=2, row=0)
btnClose = Button(window, text="Close", command= closeMusic)
btnClose.grid(column=3, row=0)
btnDirectory = Button(window, text="Search", command=browse)
btnDirectory.grid(column=2, row=1)
window.mainloop()
