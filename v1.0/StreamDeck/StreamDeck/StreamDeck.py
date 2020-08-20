from pynput.keyboard import Key, KeyCode, Listener
from pygame import mixer
import keyboard

#--------------------------------------Music-Menu-----------------------------------
def Main_Menu():
    print ("################################################")
    print ("                  StreamDeck                    ")
    print ("################################################")
    print ("1 - I CAN SMELL THE SALSA")
    print ("2 - PULL_THE_TRIGGER")
    print ("3 - YEAH_BOY")
    print ("4 - STOP_RUNNING")
    print ("5 - AAAAAA - Spongebob")
    print ("6 - When someone says I need healing 4 times")
    print ("7 - GODA_GO_FAST_AMARITE")
    print ("8 - AHHHHH - Cowboy")
    return
#----------------------------------------------------------------------------

#8 Playable Tracks. 
def Song_1():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\I_CAN_SMELL_THE_SALSA.mp3")
    mixer.music.play()
    print ("Song1 Completed!")

def Song_2():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\PULL_THE_TRIGGER.mp3")
    mixer.music.play()
    print ("Song2 Completed!")
    
def Song_3():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\YEAH_BOY.mp3")
    mixer.music.play()
    print ("Song3 Completed!")

def Song_4():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\STOP_RUNNING.mp3")
    mixer.music.play()
    print ("Song4 Completed!")

def Song_5():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\AAAAAA.mp3")
    mixer.music.play()
    print ("Song5 Completed!")

def Song_6():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\When someone says I need healing 4 times.mp3")
    mixer.music.play()
    print ("Song6 Completed!")

def Song_7():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\GODA_GO_FAST_AMARITE.mp3")
    mixer.music.play()
    print ("Song7 Completed!")

def Song_8():
    mixer.init()
    mixer.music.load("E:\\Windows_Profiles_Data\\Matthew\\Desktop\\Algato-StreamDeck\\StreamDeck_Music\\AHHHHH.mp3")
    mixer.music.play()
    print ("Song8 Completed!")

Main_Menu()

while True:
    if keyboard.read_key() == "!":
        print("Song1 Started!")
        Song_1()
    elif keyboard.read_key() == '"':
        print("Song2 Started!")
        Song_2()
    elif keyboard.read_key() == "£":
        print("Song3 Started!")
        Song_3()
    elif keyboard.read_key() == "$":
        print("Song4 Started!")
        Song_4()
    elif keyboard.read_key() == "%":
        print("Song5 Started!")
        Song_5()
    elif keyboard.read_key() == "^":
        print("Song6 Started!")
        Song_6()
    elif keyboard.read_key() == "&":
        print("Song7 Started!")
        Song_7()
    elif keyboard.read_key() == "*":
        print("Song8 Started!")
        Song_8()
    elif keyboard.read_key() == "¬":
        mixer.music.pause() # Halt current loaded music track.
        mixer.music.unload()
        print("Song Stopped!")
        break
    else:
        Main_Menu()
