import os
import pickle
import random

from helpingmethods \
    import getnotename, \
    getoffset_tonename, \
    gettonenameint
from playback \
    import playnote, \
    playsongfile


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


# UNUNSED
# Make your own note rhythm. GUI implementation soon...
# Each choice is 4 beats long, and will repeat until it fills an
# empty array with sleep values, which represent note holds
# If you want to make your own rhythms, just know:
# 1.0    0.5	  0.25    0.1666	0.0
# 1/2    1/4    1/8     1/16      Plays with next note
def makespecialrhythm(type):
    if 1 == type:
        times = [1.5, 1.0, .50, .50, .50]


# Makes a random quantity of rests to fill in a measure.
# Results may vary, and the end of the measure is more likely to have
# a higher amount of notes.
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

# saves song to file
def savesong(keyinfodict, oursong):
    filename = raw_input("save as:")
    savefolder = "./songs/"
    filepath = savefolder + filename
    if not os.path.isdir(savefolder):
        os.makedirs(savefolder)
    with open(filepath, 'wb') as f:
        pickle.dump([keyinfodict, oursong], f, -1)
    return


# gives user option to play, save, go back to random adding, or to remove the last measure from the song
def review(keyinfodict, oursong):
    inmenu = 1
    while inmenu:
        opt = input(
            " [1] play song\n [2] save as\n [3] add new random measure\n [4] remove last added measure from song\n "
            "[0] quit\nchoice? "
        )
        if opt == 1:
            if not oursong:
                print "you have to add measures to your song, first!"
            else:
                playsongfile(keyinfodict, oursong)
            continue
        elif opt == 2:
            if not oursong:
                print "you have to add measures to your song, first!"
            else:
                savesong(keyinfodict, oursong)
            continue
        elif opt == 3:
            nextseed = input("please enter next measure's seed")
            keyinfodict["ourseeds"].append(nextseed)
            random.seed(nextseed)
            # have them generated for you
            # masterrand = random.randint(0,9001)
            # keyinfodict["ourseeds"].append(random.randint(0,9001))
            return
        elif opt == 4:
            try:
                del oursong[-1]
            except IndexError:
                continue
            continue
        elif opt == 0:
            inmenu = 0
            quit()


# 2-octave range in the middle of the piano
# with an array of a random quantity, or random rest times.
# with an array of note values, which correspond the the quantity of rests.
# user will get the option to deny, or to accept the measure as it is
def intelligentplay(keyinfodict, oursong):
    ourtimes = []
    ournotes = []
    ourscale = keyinfodict["ourscale"]
    measurecount = keyinfodict["ourmeasures"]
    ourseeds = keyinfodict["ourseeds"]
    i = 0
    while i < measurecount:
        for measures in range(0, measurecount):
            nextseed = input("please enter next measure's seed")
            random.seed(nextseed)
            keyinfodict["ourseeds"].append(nextseed)
            ourtimes = makerandomtimes(ourtimes, keyinfodict["beatspermeasure"])
            ournotes = makerandomnotes(ourscale, ournotes, ourtimes)
            print('-----measure %d start-----\n' % i)
            for notes, sleeps in zip(ournotes, ourtimes):
                print "note: %s" % (gettonenameint(notes))
                print "sleep time: %f seconds\n" % sleeps
                playnote(notes, sleeps)
            keep = raw_input("keep this measure? y/n? \n")
            if keep == "Y" or keep == "y":
                if i == measurecount:
                    print "all measures are filled. song is ready."
                    ourtimes = []
                    ournotes = []
                    break
                else:
                    i += 1
                    oursong.append(zip(ournotes, ourtimes))
                    ourtimes = []
                    ournotes = []
            elif keep == "N" or keep == "n":
                if i > 0:
                    i -= 1
                    ourtimes = []
                    ournotes = []
                    continue
            keep = raw_input("r to review song, y to keep going")
            if keep == "R" or keep == "r":
                if i > 0:
                    i -= 1
                ourtimes = []
                ournotes = []
                review(keyinfodict, oursong)
                continue
            elif keep == "Y" or keep == "y":
                break
                # this is a catch-all in case the song tries to exit prematurely.
    review(keyinfodict, oursong)
