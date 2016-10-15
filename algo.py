import random
from structs import makeRandomTimes,makeRandomNotes
from playback import playNote, playSongFile
from helpingmethods import getNoteName, getBaseInt_ToneName, getOffset_ToneName, getOffset_ToneInt, getIntToneName, getRangeCount, getToneNameInt, rotate, floatEqual
import time
import pickle
import os

def saveSong(KeyInfoDict,ourSong):
    fileName = raw_input("save as:")
    #timestr = time.strftime("%Y%m%d_")
    saveFolder = "./SONGS/"
    #filePath = saveFolder+timestr+str(KeyInfoDict["masterRand"])
    filePath = saveFolder+fileName+str(KeyInfoDict["masterRand"])
    if not os.path.isdir(saveFolder):
        os.makedirs(saveFolder)
    with open(filePath, 'wb') as f:
        pickle.dump([KeyInfoDict,ourSong], f, -1)
    return

def review(KeyInfoDict,ourSong):
    inMenu = 1
    while inMenu:
        opt = input(" [1] Play song\n [2] Save as\n [3] Add new random measure\n [4] Remove last added measure from song\n [0] Quit\nChoice? ")
        if opt==1:
			if(not ourSong):
				print "You have to add measures to your song, first!"
			else:
				playSongFile(ourSong)
			continue
        elif opt==2:
            if(not ourSong):
				print "You have to add measures to your song, first!"
            else:
                saveSong(KeyInfoDict,ourSong)
            continue
        elif opt==3:
            KeyInfoDict["masterRand"]+=random.randint(0,9001)
            KeyInfoDict["ourMeasures"]+=1
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
		
def IntelligentPlay(KeyInfoDict,ourSong):
    ourTimes = []
    ourNotes = []
    ourScale = KeyInfoDict["ourScale"]
    measureCount = KeyInfoDict["ourMeasures"]
    loopOffset=0
    i=0
    while (i < measureCount):
        for measures in range(0,measureCount):
            ourTimes = makeRandomTimes(ourTimes,KeyInfoDict["beatsPerMeasure"])
            ourNotes = makeRandomNotes(ourScale,ourNotes,ourTimes)
            print('-----MEASURE %d START-----\n'%(i))
            for notes,sleeps in zip(ourNotes,ourTimes):
                print "Note: %s"%(getToneNameInt(notes))
                print "Sleep Time: %f seconds\n"%(sleeps)
                playNote(notes,sleeps)
            keep = raw_input("Keep this measure? Y/N? \n(Q to quit, R to review song)")
            if keep == "Q" or keep == "q":
                break
            elif keep=="Y" or keep == "y":
                if(measures == measureCount):
                    print "All measures are filled. Song is ready."
                    review(KeyInfoDict,ourSong)
                    ourTimes = []
                    ourNotes = []
                else:
                    ourSong.append(zip(ourNotes,ourTimes))
                    ourTimes = []
                    ourNotes = []
            elif keep =="N" or keep =="n":
                loopOffset+=1
                if i>0: 
                    i-=1
                ourTimes = []
                ourNotes = []
                continue
            elif keep =="R" or keep =="r":
                loopOffset+=1
                if i>0:
                    i-=1
                ourTimes = []
                ourNotes = []
                review(KeyInfoDict,ourSong)
                continue
            i+=1
       