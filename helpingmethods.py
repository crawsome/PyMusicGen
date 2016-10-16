

def getNoteName(toneName):
	noteDict  = ['C','Db','D','Eb','E','F','F#','G','Ab','A','Bb','B']
	return noteDict[toneName%12]

#return the 0-12 INT of the tone by giving a NAME
def getBaseInt_ToneName(toneName):
	scaleRef = {'C':0,'Db':1,'D':2,'Eb':3,'E':4,'F':5,'F#':6,'G':7,'Ab':8,'A':9,'Bb':10,'B':11}
	return scaleRef[toneName%12]

#dictionary containing offsets for each key
#if you add this offset to noteDict, it will always go to this letter. 
def getOffset_ToneName(toneName):
	scaleRef = {'C':0,'Db':1,'D':2,'Eb':3,'E':4,'F':5,'F#':-6,'G':-5,'Ab':-4,'A':-3,'Bb':-2,'B':-1}
	return scaleRef[toneName]

def getOffset_ToneInt(ourInt):
	scaleRef = [0,1,2,3,4,5,-6,-5,-4,-3,-2,-1]
	return scaleRef[ourInt]
	
#get the starting integer note by subtracting the ranges
def getRangeCount(a,b):
	return abs(getIntToneName(a)-getIntToneName(b))
#return the 0-96 INT of the tone by giving a NAME+NUM

# Returns the integer of the tone name
def getIntToneName(toneName):
	toneRef={"C0":0,"Db0":1,"D0":2,"Eb0":3,"E0":4,"F0":5,"F#0":6,"G0":7,"Ab0":8,"A0":9,"Bb0":10,"B0":11,"C1":12,"Db1":13,"D1":14,"Eb1":15,"E1":16,"F1":17,"F#1":18,"G1":19,"Ab1":20,"A1":21,"Bb1":22,"B1":23,"C2":24,"Db2":25,"D2":26,"Eb2":27,"E2":28,"F2":29,"F#2":30,"G2":31,"Ab2":32,"A2":33,"Bb2":34,"B2":35,"C3":36,"Db3":37,"D3":38,"Eb3":39,"E3":40,"F3":41,"F#3":42,"G3":43,"Ab3":44,"A3":45,"Bb3":46,"B3":47,"C4":48,"Db4":49,"D4":50,"Eb4":51,"E4":52,"F4":53,"F#4":54,"G4":55,"Ab4":56,"A4":57,"Bb4":58,"B4":59,"C5":60,"Db5":61,"D5":62,"Eb5":63,"E5":64,"F5":65,"F#5":66,"G5":67,"Ab5":68,"A5":69,"Bb5":70,"B5":71,"C6":72,"Db6":73,"D6":74,"Eb6":75,"E6":76,"F6":77,"F#6":78,"G6":79,"Ab6":80,"A6":81,"Bb6":82,"B6":83,"C7":84,"Db7":85,"D7":86,"Eb7":87,"E7":88,"F7":89,"F#7":90,"G7":91,"Ab7":92,"A7":93,"Bb7":94,"B7":95,"C8":96}
	return toneRef[toneName]

#return the NAME of the tone by giving an INT
def getToneNameInt(index):	
	intRef=["C0","Db0","D0","Eb0","E0","F0","#0","G0","Ab0","A0","Bb0","B0","C1","Db1","D1","Eb1","E1","F1","F#1","G1","Ab1","A1","Bb1","B1","C2","Db2","D2","Eb2","E2","F2","F#2","G2","Ab2","A2","Bb2","B2","C3","Db3","D3","Eb3","E3","F3","F#3","G3","Ab3","A3","Bb3","B3","C4","Db4","D4","Eb4","E4","F4","F#4","G4","Ab4","A4","Bb4","B4","C5","Db5","D5","Eb5","E5","F5","F#5","G5","Ab5","A5","Bb5","B5","C6","Db6","D6","Eb6","E6","F6","F#6","G6","Ab6","A6","Bb6","B6","C7","Db7","D7","Eb7","E7","F7","F#7","G7","Ab7","A7","Bb7","B7","C8"]
	return intRef[index]

#return array that is rotated circular 
def rotate(l,n):
    return l[-n:] + l[:-n]

#compare two floats against an error returns TRUE if both floats are ~=
def floatEqual(l,r):
	return abs(l-r)<.01		
