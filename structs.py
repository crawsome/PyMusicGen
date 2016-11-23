import random

from helpingmethods import getNoteName, getOffset_ToneName


# returns a scale of 16 notes, from the key tonic + 24
def makeScale(keyRoot, keyOpt):
    rangeJump = 24  # starting point on keyboard
    lenVar = 16  # of notes we use (2 octaves of key notes)
    ourOffset = getOffset_ToneName(keyRoot)
    keyString = getNoteName(abs(ourOffset))
    keyWheel = []
    if 1 == keyOpt:
        print(keyString + " Major selected")
        keyWheel.extend([0, 2, 2, 1, 2, 2, 2, 1])
    if 2 == keyOpt:
        print(keyString + " Natural Minor selected")
        keyWheel.extend([0, 2, 1, 2, 2, 1, 2, 2])
    if 3 == keyOpt:
        print(keyString + " Harmonic Minor selected")
        keyWheel.extend([0, 2, 1, 2, 2, 1, 3, 1])
    if 4 == keyOpt:
        print(keyString + " Melodic selected")
        keyWheel.extend([0, 2, 1, 2, 2, 2, 2, 2])
    if 5 == keyOpt:
        print(keyString + " Dorian selected")
        keyWheel.extend([0, 2, 1, 2, 2, 2, 1, 2])
    if 6 == keyOpt:
        print(keyString + " Mixolydian selected")
        keyWheel.extend([0, 2, 2, 1, 2, 2, 1, 2])
    if 7 == keyOpt:
        print(keyString + " Phrygian dominant selected")
        keyWheel.extend([0, 1, 3, 1, 2, 1, 2, 2])
    if 8 == keyOpt:
        print(keyString + " Minor Pentatonic selected")
        keyWheel.extend([0, 3, 2, 2, 3, 2])
    if 9 == keyOpt:
        print(keyString + " Pentatonic selected")
        keyWheel.extend([0, 2, 2, 3, 2, 3])
    filler = 0
    # fill array with 16 notes relevant to key and option.
    ourScale = []
    for inte in range(lenVar):
        filler += keyWheel[inte % len(keyWheel)]
        ourScale.append(filler + ourOffset + rangeJump)
    return ourScale


## Make rhythms that are associated with a genre
## Each choice is 4 beats long, and will repeat through a 
## Measure if the beats-per-measure is large enough
def makeTimes(type):
    if 1 == type:
        times = [1.5, 1.0, .50, .50, .50]

    # Randomly fills an empty array with sleep values, which represent note holds
    # If you want to make your own arrays, just know:
    #	1.0    0.5	  0.25    0.1666	0.0
    # 	1/2    1/4    1/8     1/16      Plays with next note


def makeRandomTimes(ourTimes, beatsPerMeasure):
    times = [0.0, 0.0, .25, .25, .5, .5, 1.0, 1.0]
    while abs(sum(ourTimes) - float(beatsPerMeasure)) > .001:
        nextTime = random.choice(times)
        ourTimes.append(nextTime)
        if abs(nextTime - ourTimes[-1]) < .01:
            del ourTimes[-1]
            nextTime = random.choice(times)
            ourTimes.append(nextTime)
        if (sum(ourTimes) - float(beatsPerMeasure) > .2):
            del ourTimes[-1]
            continue
        if sum(ourTimes) - float(beatsPerMeasure) < .1:
            continue
    return ourTimes
    # You can specify a special rhythm here


def makeCounterPointNotes(ourScale, ourNotes, ourTimes):
    return ourNotes


# This method is ready for verbose, just take off the comments, and it
# will display what intervals fail and which ones succeed. 

# Fills an n=#sleeps array with notes from that scale that hopefully 
# travel well. 
def makeRandomNotes(ourScale, ourNotes, ourTimes):
    ourNotes = []
    for sleeps in ourTimes:
        going = 1
        while (going):
            # Add something to it if it's empty
            if not ourNotes:
                ourNotes.append(random.choice(ourScale))
            lastNote = ourNotes[-1]
            # foo = raw_input("our last note was %s"%lastNote)
            nextJump = random.choice(ourScale)
            absJump = abs(nextJump - lastNote)
            # foo = raw_input("our nextJump was %d"%(nextJump))
            flip = 1

            # No jump higher than 10, no minor 5th"
            if (absJump >= 10 or absJump == 6):
                # print "%s was more than 10 or equal to 6"%(absJump)
                # print ourNotes
                nextJump = random.choice(ourScale)
                absJump = abs(nextJump - lastNote)
                flip = 0
                # print "FAILED"

                # not a minor second or second away at any time.
            elif (absJump == 2 or absJump == 1) and sleeps < 0.01:
                # print "%s was a mashed note next to another"%(absJump)
                # print ourNotes
                nextJump = random.choice(ourScale)
                absJump = abs(nextJump - lastNote)
                # print "FAILED"
                flip = 0

            elif abs(absJump - lastNote == lastNote) and sleeps < 0.01:
                # print "%s was the same as last note"%(absJump)
                # print ourNotes
                nextJump = random.choice(ourScale)
                absJump = abs(nextJump - lastNote)
                print "FAILED"
                flip = 0

            if flip == 1:
                print "SUCCESS WITH %s" % (nextJump)
                ourNotes.append(nextJump)
                print ourNotes
                break
    return ourNotes
