import os
import subprocess
import thread
import sys
import winsound
from time import sleep


# plays a single note by integer value
def playnote(noteint, sleeptime):
    # make a list of all files in the directory
    notes = next(os.walk("wav/"))[2]
    notes.sort()
    if sys.platform in ('posix', 'linux'):
        subprocess.Popen(['aplay', '-q', 'wav/' + notes[noteint]])
    if sys.platform in ('win32', 'win64', 'windows'):
        #thread.start_new_thread(winsound.PlaySound,("wav/" + notes[noteint], winsound.SND_FILENAME | winsound.SND_ASYNC))
        winsound.PlaySound("wav/" + notes[noteint], winsound.SND_FILENAME | winsound.SND_ASYNC)
    sleep(sleeptime)


# plays a single note by filename
def playnotefile(filename, sleeptime):
    subprocess.Popen(['aplay', '-q', 'wav/' + filename])
    sleep(sleeptime)


# plays a song file
def playsongfile(keyinfodict, oursong):
    ournotes = []
    ourtimes = []
    ourseeds = keyinfodict["ourseeds"]
    for seed, measure in zip(ourseeds, oursong):
        print ("seed: %d" % seed)
        print measure
        ournotes, ourtimes = zip(*measure)
        for notes, times in zip(ournotes, ourtimes):
            playnote(notes, times)
