import os
import pickle
import random

from helpingmethods import gettonenameint
from playback import playnote, playsongfile
from structs import makerandomtimes, makerandomnotes


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
            " [1] play song\n [2] save as\n [3] add new random measure\n [4] remove last added measure from song\n \
            [0] quit\nchoice? "
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
