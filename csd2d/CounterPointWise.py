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

#----------------------------------------Variables---------------------------------------------#

instruments     = []
instrument1     = 1
instrument2     = 1
instrument3     = 1

inputMelody     = []
melody          = []
splittedMelody  = []
melodyInput     = []

layerAmount     = 0
octaveRange     = 1
stepSize        = 0
length          = 0
bpmDef          = 100

layer1          = []
layer2          = []

NOTES = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)


#----------------------------------------Functions---------------------------------------------#

# Contrapuntinator

# MelodyTransform

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
        inputMelody.extend(input("Type your melody here: ").split(' '))
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
            print("ERROR: Incorrect input")
    melodyInput = splittedMelody
    return melodyInput

# Length select
def selLength():
    lengthFalse = True
    while True:
        try:
            length = int(input("Length in seconds (min 10 seconds): "))
            if (length >= 10):
                break
            else:
                print("False input: input must be an integer (min 10 seconds)")
        except ValueError:
            print("False input: input must be an integer (min 10 seconds)")
    return length


# Octave range select

#----------------------------------------Program-----------------------------------------------#

bpm = selBPM()
print(bpm)
instrument1 = selInstrument1()
print(instrument1)
stepSize = selStepSize()
print(stepSize)
melodyInput = melodyInput()
print(melodyInput)
length = selLength()
print(length)
