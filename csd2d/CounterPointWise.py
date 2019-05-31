#----------------------------------------Info--------------------------------------------------#
'''

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
function        = []
inputPitches    = []
inputDurations  = []
newPitches      = []
newDurations    = []

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

def melodyTransform(length):
    layer1 = melodyInput.copy() # Start first layer with user inputted melody
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
    # Combine old and new pitches and durations to form melody
    for i in range(0, length-len(inputPitches)):
        layer1.append([newPitches[i], newDurations[i], 120])
    return layer1

# ContrapuntInator

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
                            duration = int(value)
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
print("Example: D8 C4 E8 d2 E8 F4\n")
time.sleep(4)
print("****************\n")
print("Okay, time to type your melody!\n")

melodyInput = melodyInput()

print("\nTransforming...\n")
layer1 = melodyTransform(length)
time.sleep(2)
print("CounterPointing...\n")
#call ContrapuntInator
time.sleep(2)
