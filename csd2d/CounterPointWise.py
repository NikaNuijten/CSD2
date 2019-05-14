#----------------------------------------Info--------------------------------------------------#
'''

'''
#----------------------------------------Imports-----------------------------------------------#
import simpleaudio as sa
import random
import midiutil
from midiutil import MIDIFile
import inquirer

#----------------------------------------Variables---------------------------------------------#

instruments = []
instrument1 = 1
instrument2 = 1
instrument3 = 1

inputMelody = []

layerAmount = 0
octaveRange = 1
stepSize    = 0
length      = 0
bpmDef      = 100

layer1      = []
layer2      = []

#----------------------------------------Functions---------------------------------------------#

# Contrapuntinator
    # MelodyTransform

#----------------------------------------User-input--------------------------------------------#
# Tempo select
def askBPM():
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
    instrument1 = input("Insert midi channel: ") #TODO: errors
    return instrument1
# Step size select

# Melody input

# Length select

# Octave range select

#----------------------------------------Program-----------------------------------------------#
bpm = askBPM()
print(bpm)
instrument1 = selInstrument1()
print(instrument1)
