from Tkinter import *
import tkSnack

# initialize tk object to use tksnack
root = Tk()
tkSnack.initializeSnack(root)

# play sound
snd = tkSnack.Sound()
snd.read('note.wav')
print('playing sound using tkSnack')
snd.play(blocking=1)