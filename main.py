import pickle

from algo import IntelligentPlay, review
from structs import makeScale


def __main():
    print("Welcome to Colin Burke's music program\n")
    print("Please donate to the ESU Computer Science Organization if you liked this program.\n")
    print("Main Menu")
    demo = 0
    inMenu = 1
    ourSong = []
    while inMenu:
        menuOption = input(" [1]Start new random song\n [2]Load exising song from file\n [3]Demo mode\n [0]Quit\n" \
                           "Choice? ")
        if menuOption == 1:
            break
        elif menuOption == 2:
            filePath = "./SONGS/" + raw_input("./SONGS/")
            ourPickle = open(filePath, "rb")
            songParts = pickle.load(ourPickle)
            keyinfodict = songParts[0]
            ourSong = songParts[1]
            review(keyinfodict, ourSong)
            continue
        elif menuOption == 3:
            demo = 1
            israndom = 1
            break
        elif menuOption == 0:
            inMenu = 0
            quit()

    if demo:
        ourmeasures = 4
        ourkey = 'Eb'
        ouroption = 1
        beatspermeasure = 8
        ourscale = []
        ourseeds = []
        keyinfodict = {"ourmeasures": ourmeasures, "ourkey": ourkey, "ouroption": ouroption,
                       "beatspermeasure": beatspermeasure, "ourscale": ourscale, "ourseeds": ourseeds}
    else:
        ourkey = raw_input("\nWhat Key Root? Acceptable values: C,Db,D,Eb,E,F,F#,G,Ab,A,Bb,B \n")
        ouroption = input(
            "\nPLEASE CHOOSE:\n--------------\n1. Major Scale\n2. Natural Minor Scale\n3. Harmonic Minor Scale\n" \
            "4. Melodic Minor Scale\n5. Dorian Mode\n6. Mixolydian Mode\n7. Ahava Raba Mode\n \
            8. Minor Pentatonic\n9. Pentatonic scale\nYourChoice: ")
        beatspermeasure = input("\nHow many beats per measure?")
        ourmeasures = input("\nHow many measures?")
        ourscale = []
        ourseeds = []
        keyinfodict = {"ourmeasures": ourmeasures, "ourkey": ourkey, "ouroption": ouroption,
                       "beatspermeasure": beatspermeasure, "ourscale": ourscale, "ourseeds": ourseeds}
    # Make our scale with our information
    keyinfodict["ourscale"] = makeScale(ourkey, ouroption)
    IntelligentPlay(keyinfodict, ourSong)


__main()
