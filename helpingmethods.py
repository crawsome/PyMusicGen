
def getNoteName(toneName):
	noteDict  = ['A','Bb','B','C','Db','D','Eb','E','F','F#','G','Ab']
	return noteDict[toneName%12]

#return the 0-12 INT of the tone by giving a NAME
def getBaseInt_ToneName(toneName):
	scaleRef = {'A':0,'Bb':1,'B':2,'C':3,'Db':4,'D':5,'Eb':6,'E':7,'F':8,'F#':9,'G':10,'Ab':11}
	return scaleRef[toneName%12]

#dictionary containing offsets for each key
#if you add this offset to noteDict, it will always go to this letter. 
def getOffset_ToneName(toneName):
	scaleRef = {'A':0,'Bb':1,'B':2,'C':3,'Db':4,'D':5,'Eb':-6,'E':-5,'F':-4,'F#':-3,'G':-2,'Ab':-1}
	return scaleRef[toneName]

def getOffset_ToneInt(ourInt):
	scaleRef = [0,1,2,3,4,5,-6,-5,-4,-3,-2,-1]
	return scaleRef[ourInt]

def getGoodJumpsByNote(ourNote):
	ourNote=ourNote%12
	illegals = [1,3,6,8,10]

#return the 0-96 INT of the tone by giving a NAME+NUM
def getIntToneName(toneName):
	toneRef={"A0":0,"Bb0":1,"B0":2,"C0":3,"Db0":4,"D0":5,"Eb0":6,"E0":7,"F0":8,"F#0":9,"G0":10,"Ab0":11,"A1":12,"Bb1":13,"B1":14,"C1":15,"Db1":16,"D1":17,"Eb1":18,"E1":19,"F1":20,"F#1":21,"G1":22,"Ab1":23,"A2":24,"Bb2":25,"B2":26,"C2":27,"Db2":28,"D2":29,"Eb2":30,"E2":31,"F2":32,"F#2":33,"G2":34,"Ab2":35,"A3":36,"Bb3":37,"B3":38,"C3":39,"Db3":40,"D3":41,"Eb3":42,"E3":43,"F3":44,"F#3":45,"G3":46,"Ab3":47,"A4":48,"Bb4":49,"B4":50,"C4":51,"Db4":52,"D4":53,"Eb4":54,"E4":55,"F4":56,"F#4":57,"G4":58,"Ab4":59,"A5":60,"Bb5":61,"B5":62,"C5":63,"Db5":64,"D5":65,"Eb5":66,"E5":67,"F5":68,"F#5":69,"G5":70,"Ab5":71,"A6":72,"Bb6":73,"B6":74,"C6":75,"Db6":76,"D6":77,"Eb6":78,"E6":79,"F6":80,"F#6":81,"G6":82,"Ab6":83,"A7":84,"Bb7":85,"B7":86,"C7":87,"Db7":88,"D7":89,"Eb7":90,"E7":91,"F7":92,"F#7":93,"G7":94,"Ab7":95,"A8":96,"Bb8":97,"B8":98,"C8":99}
	return toneRef[toneName]

#get the starting integer note by subtracting the ranges
def getRangeCount(a,b):
	return abs(getIntToneName(a)-getIntToneName(b))

#return the NAME of the tone by giving an INT
def getToneNameInt(index):
	intRef=['A0','Bb0','B0','C0','Db0','D0','Eb0','E0','F0','F#0','G0','Ab0','A1','Bb1','B1','C1','Db1','D1','Eb1','E1','F1','F#1','G1','Ab1','A2','Bb2','B2','C2','Db2','D2','Eb2','E2','F2','F#2','G2','Ab2','A3','Bb3','B3','C3','Db3','D3','Eb3','E3','F3','F#3','G3','Ab3','A4','Bb4','B4','C4','Db4','D4','Eb4','E4','F4','F#4','G4','Ab4','A5','Bb5','B5','C5','Db5','D5','Eb5','E5','F5','F#5','G5','Ab5','A6','Bb6','B6','C6','Db6','D6','Eb6','E6','F6','F#6','G6','Ab6','A7','Bb7','B7','C7','Db7','D7','Eb7','E7','F7','F#7','G7','Ab7','A8','Bb8','B8','C8']
	return intRef[index]

#return array that is rotated circular 
def rotate(l,n):
    return l[-n:] + l[:-n]

#compare two floats against an error returns TRUE if both floats are ~=
def floatEqual(l,r):
	return abs(l-r)<.01		
