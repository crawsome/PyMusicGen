import random
from structs import makeRandomTimes,makeRandomNotes
from playback import playNote, playSongFile
from helpingmethods import getNoteName, getBaseInt_ToneName, getOffset_ToneName, getOffset_ToneInt, getIntToneName, getRangeCount, getToneNameInt, rotate, floatEqual
import time
import pickle
import os

#saves song to file
def saveSong(KeyInfoDict,ourSong):
    fileName = raw_input("save as:")
    saveFolder = "./SONGS/"
    filePath = saveFolder+fileName
    if not os.path.isdir(saveFolder):
        os.makedirs(saveFolder)
    with open(filePath, 'wb') as f:
        pickle.dump([KeyInfoDict,ourSong], f, -1)
    return

#gives user option to play, save, go back to random adding, or to remove the last measure from the song
def review(KeyInfoDict,ourSong):
    inMenu = 1
    while inMenu:
        opt = input(" [1] Play song\n [2] Save as\n [3] Add new random measure\n [4] Remove last added measure from song\n [0] Quit\nChoice? ")
        if opt==1:
			if(not ourSong):
				print "You have to add measures to your song, first!"
			else:
				playSongFile(KeyInfoDict,ourSong)
			continue
        elif opt==2:
            if(not ourSong):
				print "You have to add measures to your song, first!"
            else:
                saveSong(KeyInfoDict,ourSong)
            continue
        elif opt==3:
            nextSeed = input("Please enter next Measure's Seed")
            KeyInfoDict["ourSeeds"].append(nextSeed)
            random.seed(nextSeed)
            #have them generated for you
            #masterRand = random.randint(0,9001)
            #KeyInfoDict["ourSeeds"].append(random.randint(0,9001))
            return
        elif opt==4:
			try:
				del ourSong[-1]
			except IndexError:
				continue
			continue
        elif opt==0:
			inMenu=0
			quit()
		
# 2-octave range in the middle of the piano
# With an array of a random quantity, or random rest times.
# With an array of note values, which correspond the the quantity of rests. 
# User will get the option to deny, or to accept the measure as it is
def IntelligentPlay(KeyInfoDict,ourSong):
    ourTimes = []
    ourNotes = []
    ourScale = KeyInfoDict["ourScale"]
    measureCount = KeyInfoDict["ourMeasures"]
    ourSeeds = KeyInfoDict["ourSeeds"]
    loopOffset=0
    i=0
    while (i < measureCount):
        for measures in range(0,measureCount):
            nextSeed = input("Please enter next Measure's Seed")
            random.seed(nextSeed)
            KeyInfoDict["ourSeeds"].append(nextSeed)
            ourTimes = makeRandomTimes(ourTimes,KeyInfoDict["beatsPerMeasure"])
            ourNotes = makeRandomNotes(ourScale,ourNotes,ourTimes)
            print('-----MEASURE %d START-----\n'%(i))
            for notes,sleeps in zip(ourNotes,ourTimes):
                print "Note: %s"%(getToneNameInt(notes))
                print "Sleep Time: %f seconds\n"%(sleeps)
                playNote(notes,sleeps)
            keep = raw_input("Keep this measure? Y/N? \n")
            if keep=="Y" or keep == "y":
                if(i == measureCount):
                    print "All measures are filled. Song is ready."
                    ourTimes = []
                    ourNotes = []
                    break
                else:
                    i+=1
                    ourSong.append(zip(ourNotes,ourTimes))
                    ourTimes = []
                    ourNotes = []
            elif keep =="N" or keep =="n":
                if i>0: 
                    i-=1
                    ourTimes = []
                    ourNotes = []
                    continue
            keep = raw_input("R to review song, Y to keep going")
            if keep =="R" or keep =="r":
                if i>0:
                    i-=1
                ourTimes = []
                ourNotes = []
                review(KeyInfoDict,ourSong)
                continue
            elif keep == "Y" or keep == "Y":
                i+=1
                break
		#this is a catch-all in case the song tries to exit prematurely. 
        review(KeyInfoDict,ourSong)
       
