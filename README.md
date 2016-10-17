# Foreword - PyMusicGen:
 * Thanks for using my program. I wrote it in 2 months in my free time at my undergrad. 
 * It's in stasis / "when I feel like it" until I graduate, but then I want to really develop it an make it a contender in the python world. 
 * There are some flow control issues I need to work out. Expect bugs for now. 

# About the Author
If you liked this program, please consider the author (Colin Burke) for a job. He's well-rounded in all areas of IT including programming, deployment, asset management, and infrastructure. He also just graduated from ESU with a double major in Computer Science and Computer Security. 
   * https://www.linkedin.com/in/colingburke

# Known Issues:
 * Program will deviate from keeping proper track of measure numbers after so many N decisions, but it will not affect your ability to fill up the song's # of measures. 
 * Program will prematurely exit, so I left a catch "Review" statement until I can figure out a better overarching flow control scheme.
 
# Description:
 * From scratch, a piano tone generator that will try to randomly output nice-sounding music.
 * **Linux only for now**. Looking to make it platform-independent. 
 * Songs can be saved, loaded, or reproduced using the seeds. (You can write down some seeds, come back and get the same "Random" measure, without saving to disk)
 * A lot of effort was put into arbitrary-seeming logic in the makeRandomNotes() method. 
 
# Personal thoughts:
 * It's a little like an elevator music generator. Nothing special, but nothing to shake a stick at.
 * Program consists of a couple parts. 
    * One part is a remaking the MIDI wheel with WAV files, an array of note integers, and sleep() times. I found it liberating to not have to rely on MIDI, and to be able to add my very own samples in the folder. 
    * One other part is where the song generates a randomly-chosen array of notes, and rest values, which change with the random.seed(int) function. Each measure has it's own unique seed, which you can either keep track of yourself, or you can save the output to a file. 

## Future Ambitions:
 * **Implement a Whitelist** (tend to favor these intervals, based on current note)
    * The whitelist would benefit the program by requiring the program to arbitrarily add from a (LARGE) list of "those couple of notes sound nice" list. 
 * **Implement a Blacklist** (always remove these intervals, based on jump from current note)
    * Maybe a "Y","N", and a "X" option to add the to the blacklist. (B key is too close too N)
    * Blacklists would best be made on a 1-2 beat measure basis, and include lots of small, bad patterns for the script to check against before adding a note to the ourNotes[] list. 
 * **Implement a GUI**
    * PyQT4 maybe. 
 * **Implement 16 common note rhythms** that are associated with different styles of music. 
 * **Combine note rhythms**, and certain scales to create a real, original implementation of 
 * **Implement a reasonable counterpoint Algorithm** that can deviate only for accents, trills, etc. 
 * **Implement a midi analysis mode**, which crunches 2-part piano music files, and finds correlations on a large scale, using genetic algorithm(s) available. 
     * This could also help with generating a "Whitelist", by analyzing small parts of the music at a time. 
 * **Let users edit individual notes**
 * A "Thoughtless" mode, where the song plays 16 measures of a random key, and switches keys.
    * Possibly through cadences, and rotating around the circle of 5ths, in relative keys. 


# PYMUSICGEN v0.10.16:


### Launch Parameters:
 * No launch parameters for now, just run it. Works on linux. Will make platform-independent, and paramaterized soon. 
 
# Directions:
from Bash, navigate to the ./PyMusicGen directory, wherever you saved it, then execute:

	python main.py

## Main Menu:
**Main menu options:**
 1. [1]Start new random rong
 2. [2]Load exising song from file
 3. [3]Demo mode
 4. [0]Quit

  ### [1]. Start new random rong
  When you are starting a new song, you need to input a couple things. 
  
  1. **A Seed number**, (Int) which determines what "random" event happens. 
  		* This integer can be "loaded" from a piece of paper ;). 
  		* Meaning, if you start writing down each measure's seeds you like, if you'd prefer not to save to disk. 
  		* Don't worry, seeds are saved with the save file, too!
  2. **Key Tonic**, (String), a root note. Ex Ab, F#, D, and will determine where your song is rooted in the 12-tone scale. 
  
  3. **Choice of Scale** (Int): 
      1. Major Scale
      2. Natural Minor Scale
      3. Harmonic Minor Scale (Experimental)
      4. Melodic Minor Scale (Experimental)
      5. Dorian Mode (Experimental)
      6. Mixolydian Mode (Experimental)
      7. Ahava Raba Mode (Experimental)
      8. Minor pentatonic
      9. Pentatonic scale
  4. **Number of beats per measure**, (Int)
     * This is how many Notes can fit per measure in your song. The longer this is, the more likely the program will make a mistake (For now...)
  5. **Number of measures in your song**, (Int)
     * This is how many "Times" you can say "Y" to a measure in the song. Once the song is "full" as in, up to your Measure number, it will redirect to the "Review" menu. 
 

1. Hit **enter**, and you will hear a measure of a song. It might sound nice, it might not. Go to the next step to decide what to do with it!
2. A measure just played. Accept it with 'Y' or reject it with 'N'. 
3. You are then given the option to review the song (See "Review" below)

### [2]. Load exising song from file
You must specify a filename, a str, which will reference a previously-saved file, located in the local ./SONGS folder. Example: SONG.bpd

Notes:
 * Save folder parameters are changable in the code. 
 * It makes a SONGS directory for you if it doesn't exist.

 ### [3]. Demo mode
 Under demo mode, you can still create songs, but they will all be in a standard format. You can change this in main(). 
 
 Demo mode will pre-specify for you:

* Seed Number: (random(0,9001))
* Key Tonic: 'C'
* Scale: 1 (major Scale)
* Measures: 8
* Beats per measure: 4


### [0]. Quit
Quits the program. You will lose any unsaved data.


## Step 3. Review Mode
**Review Mode Options:**
 1. [1] Play song
 2. [2] Save as
 3. [3] Add new random measure
 4. [4] Remove last added measure from song
 5. [0] Quit

### [1]. Play Song
Will play the song as it was saved. Here's an example output of a measure. 

Seed: 124124

[(50, 0.0), (27, 1.0), (31, 0.5), (27, 0.0), (36, 0.5), (39, 0.0), (31, 1.0), (29, 0.5), (34, 0.25), (34, 0.0), (41, 0.0), (32, 0.0), (31, 0.0), (27, 0.0), (32, 0.25)

### [2]. Save as
Specify the name of the song, and you can save it to file. It will be saved in the ./SONGS/ directory. 

### [3]. Add new random measure
Attempt to add a new measure. 

**NOTE:** This doesn't work reliably if you already have a "Full" song. 

### [4]. Remove last measure added from song
This will attempt to remove the last measure in the song. If the song is empty, it will *kindly yell at you*. 

Expect some boundary bugs here.

### [0]. Quit
Quits the program
  
# Misc / FAQ: 

 * OMG THE PROGRAM EXITED AND I HEARD THE COOLEST THING EVAR! IS IT LOST?!
 	* Scroll up, write down your seeds, and just input them back in. 
 	* If you ran into a bug, please report it to me, and I'll work as fast as I can to fix it!
 * How can I change the algorithm in which the random notes are selected?
 	* In the "structs.py" script, within the "makeRandomNotes()" method,  you can edit the statement :
 	* (absJump==ourNotes[-1] or absJump>=10 or absJump==6 or ((absJump==2 or absJump==1) and sleep<=0.001))
 	* The way the program works now:
 		* Note is not supposed to be the last note played
 		* Note is not farther away than 10 semitones
 		* Note is not 6 semitones away
 		* Note is not a major  or minor 2nd, from the last played note, with a 0.0 sleep value (Makes them play together) 
 * How is the file saved? How can I retrieve it?
 	* The song stores the format in serialized pickle format. 
	* Save file structure: (For anyone wondering how I save songs)
 		1. [KeyInfoDict] pickle-dumped to the save file first. 
 		2. [OurSong] pickle-dumped to the save file last. 
		3. [OurSong] is a 2-array, zipped, array of tuples, which have
			1. A note value (Integer)
            2. A sleep value (float)

 * Can I please get the option to ourput an MP3 or WAV file?
 	* Very soon, yes. 

 * Can I export in MIDI format?
  	* Very soon, yes.

 * Can I please get a GUI with notes, and the ability to edit song metadata in the middle of the song?
  	* In a reasonable amount of time, yes ;)

 * Can you implement a genetic learning algorithm with perfect counterpoint?
  	* Pay for me to go to grad school, and we'll talk in 2 years. 

 * Why do some scales sound terrible?
   	* (in my snarky voice) You can use the "Keep measure(Y/N)" feature to remove measures.
  	* It's not perfect. Use the keep / remove measure features to remove things you do not like. 

 * Can I edit the notes individually?
	* Not for a while. :)





 
 
 
 
 
 
 
 
 
 
