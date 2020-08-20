from pynput.keyboard import Key, KeyCode, Listener
from pygame import mixer
import keyboard

''' Info:
- At this current stage only one track at a time can be executed.
'''

#--------------------------------------Music-Menu----------------------------------- #Enphasis on implementing a GUI.
def Main_Menu(): #Temporary Interface
    print ("################################################")
    print ("                  StreamDeck                    ")
    print ("################################################")
    print ("Press ! - Song 1")
    print ('Press " - Song 2')
    print ("Press £ - Song 3")
    print ("Press $ - Song 4")
    print ("Press % - Song 5")
    print ("Press ^ - Song 6")
    print ("Press & - Song 7")
    print ("Press * - Song 8")
    return
#----------------------------------------------------------------------------

#8 Playable Tracks. 
def Song_1():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song1.mp3") #Redirect this path depends on where your music is located.
    mixer.music.play()
    print ("Song1 Completed!") #Confirmation that the track 1 is running.

def Song_2():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song2.mp3")
    mixer.music.play()
    print ("Song2 Completed!")
    
def Song_3():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song3.mp3")
    mixer.music.play()
    print ("Song3 Completed!")

def Song_4():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song4.mp3")
    mixer.music.play()
    print ("Song4 Completed!")

def Song_5():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song5.mp3")
    mixer.music.play()
    print ("Song5 Completed!")

def Song_6():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song6.mp3")
    mixer.music.play()
    print ("Song6 Completed!")

def Song_7():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song7.mp3")
    mixer.music.play()
    print ("Song7 Completed!")

def Song_8():
    mixer.init()
    mixer.music.load("C:\\Users\\Matthew\\Desktop\\Algato-StreamDeck\\Song8.mp3")
    mixer.music.play()
    print ("Song8 Completed!")

Main_Menu()

while True:
    if keyboard.read_key() == "!": #Press "Shift + 1" to play function 1.
        print("Song1 Started!")
        Song_1()
    elif keyboard.read_key() == '"': #Press "Shift + 2" to play function 2.
        print("Song2 Started!")
        Song_2()
    elif keyboard.read_key() == "£": #Press "Shift + 3" to play function 3.
        print("Song3 Started!")
        Song_3()
    elif keyboard.read_key() == "$": #Press "Shift + 4" to play function 4.
        print("Song4 Started!")
        Song_4()
    elif keyboard.read_key() == "%": #Press "Shift + 5" to play function 5.
        print("Song5 Started!")
        Song_5()
    elif keyboard.read_key() == "^": #Press "Shift + 6" to play function 6.
        print("Song6 Started!")
        Song_6()
    elif keyboard.read_key() == "&": #Press "Shift + 7" to play function 7.
        print("Song7 Started!")
        Song_7()
    elif keyboard.read_key() == "*": #Press "Shift + 8" to play function 8.
        print("Song8 Started!")
        Song_8()
    elif keyboard.read_key() == "¬": #Work in progress still unuseable!
        mixer.music.pause() #Halt current loaded music track.
        mixer.music.unload()
        print("Song Stopped!")
        break
    else:
        Main_Menu() #Another key pressed displays the main interface.
