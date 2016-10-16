import os
import re
import subprocess
from time import sleep
import random
import struct
import pickle
import sys

from structs import  makeRandomNotes, makeRandomTimes, makeScale
from algo import IntelligentPlay, review
from playback import playNote, playChordIntList, playNoteFile, playChordFileList, playSongFile
from helpingmethods import getNoteName, getBaseInt_ToneName, getOffset_ToneName, getOffset_ToneInt, getIntToneName, getRangeCount, getToneNameInt, rotate, floatEqual

def __main():
    print("Welcome to Colin Burke's music program\n")
    print("Please donate to the ESU Computer Science Organization if you liked this program.\n")
    print("Main Menu")
    masterRand = 0
    demo = 0
    inMenu = 1
    ourSong = []
    while inMenu:
        menuOption = input(" [1]Start new random rong\n [2]Load exising song from file\n [3]Demo mode\n [0]Quit\nChoice? ")
        if menuOption==1:
            isRandom = 1
            break
        if menuOption==2: 
            filePath = "./SONGS/" + raw_input("./SONGS/")
            ourPickle = open(filePath, "rb")
            songParts = pickle.load(ourPickle)
            KeyInfoDict = songParts[0]
            ourSong = songParts[1]
            review(KeyInfoDict,ourSong)
            continue
        elif menuOption==3:
            demo = 1
            isRandom = 1
            break
        elif menuOption==0:
            inMenu = 0
            quit()
            
    if demo:
        ourMeasures = 4
        #ourKey = random.choice(getNoteName(random.randint(0,11)))
        ourKey = 'Eb'
        #ourOption = random.randint(1,9)
        ourOption = 1
        beatsPerMeasure = 4
        ourScale = []
        ourSeeds = []
        KeyInfoDict = {"ourMeasures":ourMeasures,"ourKey":ourKey,"ourOption":ourOption,"beatsPerMeasure":beatsPerMeasure,"ourScale":ourScale,"ourSeeds":ourSeeds}
    else:
        ourKey = raw_input("\nWhat Key Root? Accepable values: C,Db,D,Eb,E,F,F#,G,Ab,A,Bb,B \n")
        ourOption = input("\nPLEASE CHOOSE:\n--------------\n1. Major Scale\n2. Natural Minor Scale\n3. Harmonic Minor Scale\n4. Melodic Minor Scale\n5. Dorian Mode\n6. Mixolydian Mode\n7. Ahava Raba Mode\n8. Minor pentatonicn\9. Pentatonic scale\nYourChoice: ")
        beatsPerMeasure = input("\nHow many beats per measure?")
        ourMeasures = input("\nHow many measures?")
        ourScale = []
        ourSeeds = []
        KeyInfoDict = {"ourMeasures":ourMeasures,"ourKey":ourKey,"ourOption":ourOption,"beatsPerMeasure":beatsPerMeasure,"ourScale":ourScale,"ourSeeds":ourSeeds}
    #Make our scale with our information
    KeyInfoDict["ourScale"] = makeScale(ourKey,ourOption)
    IntelligentPlay(KeyInfoDict,ourSong)

__main()
