### This is the sound effects loops to make coder cleaner
from pygame import mixer


def mother_sounds():
    i = 1
    while i < 2:
        mixer.init()
        mixer.music.load('mother.wav')
        print("music starting")
        mixer.music.set_volume(0.2)
        mixer.music.play()
        i += 1
