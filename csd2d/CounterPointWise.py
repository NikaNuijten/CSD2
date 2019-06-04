#----------------------------------------Info--------------------------------------------------#
'''
For this program you need to install music21 and musescore version 2.3.2
'''
#----------------------------------------Imports-----------------------------------------------#
import simpleaudio as sa
import random
import midiutil
from midiutil import MIDIFile
import inquirer
import re
import time
import os
import music21 as m21

#----------------------------------------Variables---------------------------------------------#

instruments     = []
instrument1     = 1
instrument2     = 1
instrument3     = 1

inputMelody     = []
melody          = []
splittedMelody  = []
melodyInput     = []
layer1          = []
layer2          = []
layerOne        = []
layerOneCopy    = []
layer01         = []
function        = []
inputPitches    = []
inputDurations  = []
newPitches      = []
newDurations    = []
durations       = []
durations2      = []
options         = []

layerAmount     = 0
octaveRange     = 1
stepSize        = 0
length          = 0
bpmDef          = 100


NOTES = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)


#----------------------------------------Functions---------------------------------------------#

# MelodyTransform
def shuffleTransform(list): # Randomly shuffles the note or duration values
    random.shuffle(list)
    return list

def invertTransform(list): # Inverts the note or duration values
    list.reverse()
    return list

def transform(list): # Chooses a transform function an transforms list once
    transformations = ["shuffle", "invert"]
    newList = []
    function = random.choice(transformations)
    if function == "shuffle":
        newList = shuffleTransform(list)
    else:
        newList = invertTransform(list)
    return newList

def getMaxStepsize():
    maxStepsize = 0
    stepsize = 0
    for i in range(len(newPitches)-1):
        stepsize = (abs(newPitches[i] - newPitches[i+1]))
        if (stepsize > maxStepsize):
            maxStepsize = stepsize
    return maxStepsize

def melodyTransform(length):
    for note in melodyInput: # Seperate notes and durations from melody
        inputPitches.append(note[0])
        inputDurations.append(note[1])
    repeat = length/len(inputPitches) # Full length (input)/ length melodyInput
    while repeat > 0:
        # Transform pitches
        newList = transform(inputPitches)
        for pitch in inputPitches:
            newPitches.append(pitch)
        # Transform durations
        newList = transform(inputDurations)
        for duration in inputDurations:
            newDurations.append(duration)
        repeat -= 1 # Repeat until it reaches the inputted length
    while True:
        maxStepsize = getMaxStepsize()
        if (maxStepsize > 2):
            for i in range(len(newPitches)):
                if (abs(newPitches[i] - newPitches[i+1]) > 2):
                    newPitches.insert((i+1),(int(newPitches[i] + ((newPitches[i+1] - newPitches[i])/2))))
        else:
            break
    # Combine old and new pitches and durations to form melody
    for i in range(0, length):
        layer1.append([newPitches[i], newDurations[i], 120])
    return layer1

# ContrapuntInator
def getLastNote():
    global lastNote
    lastNote = layerOne[0]
    return lastNote

def parallel():
    global verschil
    layerTwo.append(layerOne[0] + verschil)
    getLastNote()
    layerOne.pop(0)
    return lastNote

def tegenbeweging():
    global verschil
    layerTwo.append(layerOne[0] - verschil)
    getLastNote()
    layerOne.pop(0)
    return lastNote

def zijdelings():
    layerTwo.append(layerOne[0])
    getLastNote()
    layerOne.pop(0)
    return lastNote

def zijdelings2():
    layerTwo.append(layerOne[0] + random.choice([2, -2]))
    getLastNote()
    layerOne.pop(0)
    return lastNote

def einde():
    afstand = abs(layerTwo[-1] - layerOne[-1])
    if (afstand != 3 or afstand != 4):
        if (afstand > 4):
            layerOne.append(layerOne[0])
            layerOneCopy.append(layerOne[0])
            layer1.append(layerOne[0])
            layerTwo.append(layerTwo[-1] + random.choice([1, 2]))
            einde()
        elif (afstand < 3):
            layerOne.append(layerOne[0])
            layerOneCopy.append(layerOne[0])
            layer1.append(layerOne[0])
            layerTwo.append(layerTwo[-1] - random.choice([1, 2]))
            einde()
        elif (afstand == 3):
            layerTwo.append(layerTwo[-1] + 1)
            layerOne.append(layerOne[0] - 2)
            layerOneCopy.append(layerOne[0] - 2)
            layer1.append(layerOne[0] - 2)
            return layerOne, layerTwo
        else:
            layerTwo.append(layerTwo[-1] + 2)
            layerOne.append(layerOne[0] - 2)
            layerOneCopy.append(layerOne[0] - 2)
            layer1.append(layerOne[0] - 2)
            return layerOne, layerTwo

def layer01Maker():
    for duration in layer2:
        durations.append(duration[1])
    for note in layerOneCopy:
        try:
            duration = float(durations[0])
            durations.pop(0)
        except:
            duration = 4
        layer01.append([note, duration, 120])

    return layer01

def layer2Maker():
    options.extend([1, 2, 4, 8])
    for note in layerTwo:
        durations2.append(random.choice(options))
        try:
            duration = float(durations[0])
            durations.pop(0)
        except:
            duration = durations2[-1]
        layer2.append([note, duration, 120])
    durations2.clear()
    options.clear()
    return layer2

def create_notes(input_notes):
    """
    <Copied from Ciska>
    Transforms a list of notes to m21 notes.

    Parameters:
    input_notes - a list of notes, each note defined as a list:
                  [pitch, quarter_note_length, velocity]

    Returns:
    A list of m21 notes.
    """
    notes =[]                       # instantiate new list
    for n in input_notes:
        note = m21.note.Note()      # create m21 note
        # to work with midi note values --> create a pitch object with
        # midi parameter and assign this pitch object to note.pitch
        note.pitch = m21.pitch.Pitch(midi=n[0])
        note.quarterLength=n[1]     # set notelength and velocity
        note.volume.velocity = n[2]
        notes.append(note)          # add note to m21 notes list
    return notes

def notes_to_stream(notes):
    """
    <Copied from Ciska>
    Creates a m21 stream adds the m21 notes in the passed list and returns the
    stream.

    Parameters:
    notes: - A list of m21 notes.

    Returns:
    A m21 stream.
    """
    clef = m21.clef.TrebleClef()    # instantiate treble clef
    stream = m21.stream.Stream()    # instantiate stream
    stream.clef = clef
    stream.append(notes)            # add notes
    return stream

def contrapuntInator():
    global lastNote
    global verschil
    verschil = (layerOne[1] - layerOne[0])
    interval = abs(layerTwo[0] - lastNote)
    if ( interval == 3 or interval == 4 or interval == 8 or interval == 9): #tertsen en sexten
        options.extend([0, 1, 2]) # 0 = zijdelings, 1 = tegenbeweging 2 = parallel
        choice = random.choice(options)
        options.clear()
        if (choice == 0):
            lastNote = parallel()
        elif (choice == 1):
            lastNote = tegenbeweging()
        else:
            lastNote = zijdelings()
    elif (interval == 5 or interval == 7):  #reine kwart en kwint
        options.extend([0, 1])
        choice = random.choice(options)
        options.clear()
        if (choice == 0):
            lastNote = tegenbeweging()
        else:
            lastNote = zijdelings()
    elif (interval == 0 or interval == 12): #prime en octaaf
        lastNote = tegenbeweging()
    elif (verschil == 0):   #reine prime
        lastNote = zijdelings2()
    else:                   #overige intervallen
        lastNote = zijdelings()
    if (len(layerOne) > 1):
        contrapuntInator()
    else:
        #TODO: cadens met tegenbeweging
        time.sleep(1)
        print("Here it is:")
        einde()

# Other
def note_to_number(note: str, octave: int) -> int:

    note = NOTES.index(note)
    note += (NOTES_IN_OCTAVE * octave)

    assert 0 <= note <= 127, errors['notes']

    return note


#----------------------------------------User-input--------------------------------------------#
# Tempo select
def selBPM():
    bpmFalse = True
    while True: # create loop
        bpmx = input("Bpm (press enter for default 100): ")
        if (bpmx==""): # if enter is pressed, bpm is default
            bpm=bpmDef
            break # answer recieved: stop loop
        else:
            try:
                bpm=int(bpmx) # checking whether input is integer
                break # answer recieved: stop loop
            except ValueError: #if input is not an integer replay loop
                print("False input: bpm input must be an integer, try again...")
    return bpm

# Instrument select
def selInstrument1():
    instrumentFalse = True
    while True:
        try:
            instrument1 = int(input("Insert midi channel: "))
            if 1 <= instrument1 <= 10:
                break
            else:
                print("False input: midichannel must be an integer between 1-10")
        except ValueError:
            print("False input: midichannel must be an integer between 1-10")
    return instrument1

# Step size select
def selStepSize():
    stepSize = input("Maximum step size: ") #TODO: errors
    return stepSize

# Melody input
def melodyInput():
    inputFalse = True
    while True:
        inputMelody.extend(input("Type your melody here:\n").split(' '))
        try:
            for element in inputMelody:
                melody.append([element])
            for list in melody:
                for note in list:
                    for value in note:
                        try:
                            durationvalue = float(value)
                            duration = (4/durationvalue)
                        except:
                            note = value
                splittedMelody.append([note_to_number(note, 5), duration, 120])
            break
        except ValueError:
            inputMelody.clear()
            melody.clear()
            splittedMelody.clear()
            print("ERROR: Incorrect input\n")
    melodyInput = splittedMelody
    return melodyInput

# Length select
def selLength():
    lengthFalse = True
    while True:
        try:
            length = int(input("Length in notes (min 8 notes): "))
            if (length >= 8):
                break
            else:
                print("False input: input must be an integer (min 10 seconds)")
        except ValueError:
            print("False input: input must be an integer (min 10 seconds)")
    return length

# Octave range select

#----------------------------------------Program-----------------------------------------------#

# Explaination
os.system('clear')
print("Welcome to CounterPointWise!\n...")
time.sleep(2)
print("This program will create a two-part compostion, \nbased on your own melody and the counterpoint rules.\n...")
time.sleep(4)
print("Let's create some music together!\n...")
time.sleep(6)
os.system('clear')
print("Let's start by setting some rules\n...")
time.sleep(2)

# Selecting rules
selecting = True
while True:
    bpm = selBPM()
    instrument1 = selInstrument1()
    stepSize = selStepSize()
    length = selLength()
    os.system('clear')
    print("\nWell done! These are the rules you selected:\n")
    time.sleep(1)
    print("Bpm = ", bpm)
    print("Instrument layer 1 = ", instrument1)
    print("Stepsize = ", stepSize)
    print("Length (in notes) = ", length)
    time.sleep(1)
    answer = input("\nIs this correct?('yes' or 'no')\n")
    answerFalse = True
    while True:
        if answer == "no":
            print("\nYou can now reselect your rules.\n")
            break
        else:
            if answer == "yes":
                break
            else:
                print("Please answer with 'yes' or 'no'..")
                answer = input("\nIs this correct?('yes' or 'no')\n")
    if answer == "yes":
        break

# Melody explaination
os.system('clear')
print("Great!, now it's time to input your own melody...\n")
time.sleep(2)
print("***** Rules *****\n")
time.sleep(1)
print("Type the notename, followed by the duration.\nFor example: D4\nThis will give you a quarter note D.\n")
time.sleep(6)
print("For sharps, use lowercase.\nFor example: c2 \nThis will give you a half note C Sharp.\n")
time.sleep(6)
print("Separate the notes with a single spacebar.\n")
time.sleep(3)
print("Example: D8 C4 E8 F4 g8\n")
time.sleep(4)
print("****************\n")
print("Okay, time to type your melody!\n")

melodyInput = melodyInput()

print("\nTransforming...\n")
layer1 = melodyTransform(length)
time.sleep(2)
print("CounterPointing...\n")

for note in layer1:
    layerOne.append(note[0]) #alle midinootwaardes in een array
    layerOneCopy.append(note[0])
for duration in layer1:
    durations.append(duration[1]) #alle durations in een array

layerTwo = [(layerOne[0])] #eerste noot van layertwo is eerste noot van layerOne
verschil = 0;
lastNote = getLastNote()
contrapuntInator()
layer2Maker()
layer01Maker()
notes = create_notes(layer2)
stream = notes_to_stream(notes)
stream2 = m21.stream.Stream()
stream2.append(stream)
notes.clear()
notes = create_notes(layer01)
stream = notes_to_stream(notes)
s = m21.stream.Stream()
s.insert(0.0, stream)
s.insert(0.0, stream2)
s.show()
time.sleep(2)
