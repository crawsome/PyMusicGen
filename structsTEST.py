import random
from time import sleep
from helpingmethods import getNoteName, getBaseInt_ToneName, getOffset_ToneName, getOffset_ToneInt, getIntToneName, getRangeCount, getToneNameInt, rotate, floatEqual

# returns a scale of 16 notes, from the key tonic + 24
def makeScale(keyRoot,keyOpt):
    rangeJump = 24 # starting point on keyboard
    lenVar = 16 # of notes we use (2 octaves of key notes)
    ourOffset = getOffset_ToneName(keyRoot)
    keyString = getNoteName(abs(ourOffset))
    keyWheel = []
    if  1  == keyOpt:
        print(keyString + " Major selected") 
        keyWheel.extend([0,2,2,1,2,2,2,1])
    if  2  == keyOpt:
        print(keyString + " Natural Minor selected")         
        keyWheel.extend([0,2,1,2,2,1,2,2])
    if  3  == keyOpt:
        print(keyString + " Harmonic Minor selected") 
        keyWheel.extend([0,2,1,2,2,1,3,1])
    if  4  == keyOpt:
        print(keyString + " Melodic selected") 
        keyWheel.extend([0,2,1,2,2,2,2,2])
    if  5  == keyOpt:
        print(keyString + " Dorian selected") 
        keyWheel.extend([0,2,1,2,2,2,1,2])
    if  6  == keyOpt:
        print(keyString + " Mixolydian selected")
        keyWheel.extend([0,2,2,1,2,2,1,2])
    if  7  == keyOpt:
        print(keyString + " Phrygian dominant selected") 
        keyWheel.extend([0,1,3,1,2,1,2,2])
    if  8  == keyOpt:
        print(keyString + " Minor Pentatonic selected") 
        keyWheel.extend([0,3,2,2,3,2])
    if  9  == keyOpt:
        print(keyString + " Pentatonic selected") 
        keyWheel.extend([0,2,2,3,2,3])
    filler=0
    #fill arrray with 16 notes relevant to key and option. 
    ourScale = []
    for inte in range(lenVar):
        filler+=keyWheel[inte%len(keyWheel)]
        ourScale.append(filler+ourOffset+rangeJump)
    return ourScale

## Make rhythms that are associated with a genre
## Each choice is 4 beats long, and will repeat through a 
## Measure if the beats-per-measure is large enough
def makeTimes(type):
    if  1  == type:
        times = [1.5,1.0,.50,.50,.50]

# Randomly fills an empty array with sleep values, which represent note holds
# If you want to make your own arrays, just know:
	#	1.0    0.5	  0.25    0.1666	0.0 
	# 	1/2    1/4    1/8     1/16      Plays with next note
def makeRandomTimes(ourTimes,beatsPerMeasure):
    times = [0.0,0.0,.25,.25,.5,.5,1.0,1.0]
    while abs(sum(ourTimes) - float(beatsPerMeasure))>.001:
        nextTime = random.choice(times)
        ourTimes.append(nextTime)
        if abs(nextTime - ourTimes[-1]) < .01:
            del ourTimes[-1]
            nextTime = random.choice(times)
            ourTimes.append(nextTime)
        if (sum(ourTimes) - float(beatsPerMeasure)>.2):
            del ourTimes[-1]
            continue
        if sum(ourTimes) - float(beatsPerMeasure)<.1:
            continue
    return ourTimes
    #You can specify a special rhythm here

def makeCounterPointNotes(ourScale,ourNotes,ourTimes):    
    return ourNotes

#fills an n=#sleeps array with notes from that scale that hopefully travel well. 
def makeRandomNotes(ourScale,ourNotes,ourTimes):
    ourNotes = []
    for sleeps in ourTimes:
        nextJump = random.choice(ourScale)
        foo = raw_input("our nextJump was %s"%nextJump)
        try: 
            lastNote = ourNotes[-1]
            absJump = abs(nextJump-lastNote)
            foo = raw_input("no index error")
        # If it's empty, add a random starting note.     
        except IndexError:
            absJump = 0
            foo = raw_input("index error")
        ourNotes.append(nextJump)
        lastNote = ourNotes[-1]
        #No jump higher than 10, no minor 5th"
        while (absJump>=10 or absJump==6):
			print "was more than 10 or equal to 6"
			print absJump
			#not a minor second or second away at any time. 
			while (absJump==2 or absJump==1) and sleep*sleep<.125:
				print "was a mashed note next to another"
				while (((nextJump-absJump)==lastNote or (nextJump+absJump)==lastNote)):
					print "Avoided a(n) %s: "%(absJump)
					del ourNotes[-1]
					nextJump = random.choice(ourScale)
					try: 
						absJump = abs(nextJump-ourNotes[-1])
					except IndexError:
						absJump = abs(nextJump%12)
					ourNotes.append(nextJump)
					if not ourScale[0] in ourNotes:
						ourNotes.append(ourScale[0])
    return ourNotes
