import os
import subprocess
from time import sleep
from helpingmethods import getNoteName, getBaseInt_ToneName, getOffset_ToneName, getOffset_ToneInt, getIntToneName, getRangeCount, getToneNameInt, rotate, floatEqual

#Plays a single note by integer value
def playNote(noteInt,sleepTime):
    #Make a list of all files in the directory
    notes = next(os.walk("wav/"))[2]
    notes.sort()
    subprocess.Popen(['aplay','-q', 'wav/' + notes[noteInt]])
    sleep(sleepTime)
    
#Plays a whole chord by integer value
def playChordIntList(noteIntList,sleepTime):
    notes = next(os.walk("wav/"))[2]
    for ints in noteIntList:
        subprocess.Popen(['aplay','-q', 'wav/' + notes])
    sleep(sleepTime)    
    
#Plays a single note by filename
def playNoteFile(fileName,sleepTime):
    subprocess.Popen(['aplay','-q', 'wav/' + fileName])    
    sleep(sleepTime)
    
#Plays a whole chord by filename
def playChordFileList(fileNames,sleepTime):
    for notes in fileNames:
        subprocess.Popen(['aplay','-q', 'wav/' + notes])
    sleep(sleepTime)

def playSongFile(KeyInfoDict,ourSong):
    ourNotes = []
    ourTimes = []
    ourSeeds = KeyInfoDict["ourSeeds"]
    for seed,measure in zip(ourSeeds,ourSong):
        print ("Seed: %d"*(seed))
        print measure
        ourNotes,ourTimes = zip(*measure)
        for notes,times in zip(ourNotes,ourTimes):
            playNote(notes,times)
