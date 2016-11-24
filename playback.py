import os
import subprocess
from time import sleep
from helpingmethods import getnotename, getbaseint_tonename, getoffset_tonename, getoffset_toneint, getinttonename, \
    getrangecount, gettonenameint, rotate, floatequal


# plays a single note by integer value
def playnote(noteint, sleeptime):
    # make a list of all files in the directory
    notes = next(os.walk("wav/"))[2]
    notes.sort()
    subprocess.popen(['aplay', '-q', 'wav/' + notes[noteint]])
    sleep(sleeptime)


# plays a whole chord by integer value
def playchordintlist(noteintlist, sleeptime):
    notes = next(os.walk("wav/"))[2]
    for ints in noteintlist:
        subprocess.popen(['aplay', '-q', 'wav/' + notes])
    sleep(sleeptime)


# plays a single note by filename
def playnotefile(filename, sleeptime):
    subprocess.popen(['aplay', '-q', 'wav/' + filename])
    sleep(sleeptime)


# plays a whole chord by filename
def playchordfilelist(filenames, sleeptime):
    for notes in filenames:
        subprocess.popen(['aplay', '-q', 'wav/' + notes])
    sleep(sleeptime)


# plays a song file
def playsongfile(keyinfodict, oursong):
    ournotes = []
    ourtimes = []
    ourseeds = keyinfodict["ourseeds"]
    for seed, measure in zip(ourseeds, oursong):
        print ("seed: %d" % (seed))
        print measure
        ournotes, ourtimes = zip(*measure)
        for notes, times in zip(ournotes, ourtimes):
            playnote(notes, times)
