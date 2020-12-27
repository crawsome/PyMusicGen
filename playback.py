import os
import subprocess
import sys
from time import sleep
from pygame import mixer

mixer.init()

notes = next(os.walk("wav/"))[2]
notes.sort()

# plays a single note by integer value
def playnote(noteint, sleeptime):
    # make a list of all files in the directory
    if sys.platform in ('posix', 'linux', 'linux2'):
        subprocess.Popen(['aplay', '-q', 'wav/' + notes[noteint]])
    if sys.platform in ('win32', 'win64', 'windows'):
        s = mixer.Sound(("wav/" + notes[noteint]))
        s.play()
    sleep(sleeptime)


# plays a single note by filename
def playnotefile(filename, sleeptime):
    subprocess.Popen(['aplay', '-q', 'wav/' + filename])
    sleep(sleeptime)


# plays a song file
def playsongfile(keyinfodict, oursong):
    ourseeds = keyinfodict["ourseeds"]
    for seed, measure in zip(ourseeds, oursong):
        print("seed: %d" % seed)
        print(*measure)
        for notes, times in zip(*measure):
            playnote(notes, times)
