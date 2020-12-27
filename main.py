from structs import makescale, intelligentplay, review
import pickle

def __main__():
    print("Welcome to Colin Burke's music program\n")
    print("Please donate to the ESU Computer Science Organization if you liked this program.\n")
    print("Main Menu")
    demo = 0
    inmenu = 1
    oursong = []
    while inmenu:
        menuoption = int(
            input(" [1]Start new random song\n [2]Load exising song from file\n [3]Demo mode\n [0]Quit\n Choice? "))
        if menuoption == 1:
            break
        elif menuoption == 2:
            filepath = "./songs/" + str(input("./songs/"))
            ourpickle = open(filepath, "rb")
            songparts = pickle.load(ourpickle)
            keyinfodict = songparts[0]
            oursong = songparts[1]
            review(keyinfodict, oursong)
            continue
        elif menuoption == 3:
            demo = 1
            israndom = 1
            break
        elif menuoption == 0:
            inmenu = 0
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
        ourkey = str(input("\nWhat Key Root? Acceptable values: C,Db,D,Eb,E,F,F#,G,Ab,A,Bb,B \n"))
        ouroption = int(input(
            "\nplease choose:\n--------------\n1. major scale\n2. natural minor scale\n3. harmonic minor scale\n"
            "4. melodic minor scale\n5. dorian mode\n6. mixolydian mode\n7. ahava raba mode\n8. minor pentatonic\n9. "
            "pentatonic scale\nyour choice: "))
        beatspermeasure = int(input("\nhow many beats per measure?"))
        ourmeasures = int(input("\nhow many measures?"))
        ourscale = []
        ourseeds = []
        keyinfodict = {"ourmeasures": ourmeasures, "ourkey": ourkey, "ouroption": ouroption,
                       "beatspermeasure": beatspermeasure, "ourscale": ourscale, "ourseeds": ourseeds}
    # make our scale with our information
    keyinfodict["ourscale"] = makescale(ourkey, ouroption)
    intelligentplay(keyinfodict, oursong)


__main__()
