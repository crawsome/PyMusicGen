import random

from helpingmethods import getnotename, getoffset_tonename


# returns a scale of 16 notes, from the key tonic + 24
def makescale(keyroot, keyopt):
    rangejump = 24  # starting point on keyboard
    lenvar = 16  # of notes we use (2 octaves of key notes)
    ouroffset = getoffset_tonename(keyroot)
    keystring = getnotename(abs(ouroffset))
    keywheel = []
    if 1 == keyopt:
        print(keystring + " Major selected")
        keywheel.extend([0, 2, 2, 1, 2, 2, 2, 1])
    if 2 == keyopt:
        print(keystring + " Natural Minor selected")
        keywheel.extend([0, 2, 1, 2, 2, 1, 2, 2])
    if 3 == keyopt:
        print(keystring + " Harmonic Minor selected")
        keywheel.extend([0, 2, 1, 2, 2, 1, 3, 1])
    if 4 == keyopt:
        print(keystring + " Melodic selected")
        keywheel.extend([0, 2, 1, 2, 2, 2, 2, 2])
    if 5 == keyopt:
        print(keystring + " Dorian selected")
        keywheel.extend([0, 2, 1, 2, 2, 2, 1, 2])
    if 6 == keyopt:
        print(keystring + " Mixolydian selected")
        keywheel.extend([0, 2, 2, 1, 2, 2, 1, 2])
    if 7 == keyopt:
        print(keystring + " Phrygian dominant selected")
        keywheel.extend([0, 1, 3, 1, 2, 1, 2, 2])
    if 8 == keyopt:
        print(keystring + " Minor Pentatonic selected")
        keywheel.extend([0, 3, 2, 2, 3, 2])
    if 9 == keyopt:
        print(keystring + " Pentatonic selected")
        keywheel.extend([0, 2, 2, 3, 2, 3])
    filler = 0
    # fill array with 16 notes relevant to key and option.
    ourscale = []
    for inte in range(lenvar):
        filler += keywheel[inte % len(keywheel)]
        ourscale.append(filler + ouroffset + rangejump)
    return ourscale


# Make rhythms that are associated with a genre. Each choice is 4 beats long, and will repeat until it fills an
# empty array with sleep values, which represent note holds
# If you want to make your own rhythms, just know:
# 1.0    0.5	  0.25    0.1666	0.0
# 1/2    1/4    1/8     1/16      Plays with next note
def maketimes(type):
    if 1 == type:
        times = [1.5, 1.0, .50, .50, .50]


def makerandomtimes(ourtimes, beatspermeasure):
    times = [0.0, 0.0, .25, .25, .5, .5, 1.0, 1.0]
    while abs(sum(ourtimes) - float(beatspermeasure)) > .001:
        nexttime = random.choice(times)
        ourtimes.append(nexttime)
        if abs(nexttime - ourtimes[-1]) < .01:
            del ourtimes[-1]
            nexttime = random.choice(times)
            ourtimes.append(nexttime)
        if (sum(ourtimes) - float(beatspermeasure) > .2):
            del ourtimes[-1]
            continue
        if sum(ourtimes) - float(beatspermeasure) < .1:
            continue
    return ourtimes
    # You can specify a special rhythm here


# Fills an n=#sleeps array with notes from that scale that hopefully travel well. 
def makerandomnotes(ourscale, notes, ourtimes):
    notes = []
    for sleeps in ourtimes:
        going = 1
        while going:
            # add something to it if it's empty
            if not notes:
                notes.append(random.choice(ourscale))
            lastnote = notes[-1]
            # foo = raw_input("our last note was %s"%lastnote)
            nextjump = random.choice(ourscale)
            absjump = abs(nextjump - lastnote)
            # foo = raw_input("our nextjump was %d"%(nextjump))
            flip = 1

            # no jump higher than 10, no minor 5th"
            if absjump >= 10 or absjump == 6:
                # print "%s was more than 10 or equal to 6"%(absjump)
                nextjump = random.choice(ourscale)
                absjump = abs(nextjump - lastnote)
                flip = 0

                # not a minor second or second away at any time.
            elif (absjump == 2 or absjump == 1) and sleeps < 0.01:
                # print "%s was a mashed note next to another"%(absjump)
                nextjump = random.choice(ourscale)
                absjump = abs(nextjump - lastnote)
                # print "failed"
                flip = 0

            elif abs(absjump - lastnote == lastnote) and sleeps < 0.01:
                # print "%s was the same as last note"%(absjump)
                nextjump = random.choice(ourscale)
                absjump = abs(nextjump - lastnote)
                print "failed"
                flip = 0

            if flip == 1:
                print "success with %s" % (nextjump)
                notes.append(nextjump)
                print notes
                break
    return notes
