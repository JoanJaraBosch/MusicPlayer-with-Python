# Load the required library
from pygame import mixer #sound
from tkinter import * #gui
from glob import glob #directoris
import pygame #sound with time
import os #directori
import threading #doing a thread to play music

#Fubction to search music in the actual directory and play it
def playMusic():
	global notPause
	directori = os.getcwd()
	for fitxer in glob(directori+"\*.mp3"):
		mixer.init()
		mixer.music.load(fitxer)
		mixer.music.set_volume(1.0)
		mixer.music.play()
		print("You are listening "+fitxer.split('\\')[-1])
		i=0
		while mixer.music.get_busy(): 
			if(notPause and i == 1):
				mixer.music.unpause()
				i=0
				
			if(not notPause and i==0):
				mixer.music.pause()
				i=1
		
#Function to start the Thread			
def auxPlayMusic():
	global currentlyThread
	currentlyThread.start()

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

#global variables
notPause = True
currentlyThread = threading.Thread(target=playMusic)


#gui
window = Tk()
window.title("Jarr Music Player for Python") 
window.geometry('150x50')
btnPlay = Button(window, text="Play", command=auxPlayMusic)
btnPlay.grid(column=1, row=0)
btnPause = Button(window, text="Pause", command=stopMusic)
btnPause.grid(column=2, row=0)
btnClose = Button(window, text="Close", command=window.destroy)
btnClose.grid(column=3, row=0)
window.mainloop()

