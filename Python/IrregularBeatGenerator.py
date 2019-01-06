#----------------------------------------Info--------------------------------------------------#
'''
Stappenplan:
    1. BPM user input
    2. (2) irregular time signatures (user input)
   (3. sample user input)
    4. Sequencer
    5. Random beat generator
    6. Save MIDI-file? (user-input)
    7. Return to step 4
    8. Stoppen
'''
#----------------------------------------Imports-----------------------------------------------#

import simpleaudio as sa
import time
import random
import inquirer
import threading
from threading import Thread
import midiutil
from midiutil import MIDIFile

#----------------------------------------Variables---------------------------------------------#

bpmDef = 120 # default BPM
hihat = sa.WaveObject.from_wave_file("audioFiles/HiHat.wav")
kick = sa.WaveObject.from_wave_file("audioFiles/Kick.wav")
snare = sa.WaveObject.from_wave_file("audioFiles/Snare.wav")
timestamps = []
timestampList = []
durationSum = 0
replay = True

#----------------------------------------Functions---------------------------------------------#

# Random beat generator
def beatGenerator(durationVar, durationVar2):
    durationList = []
    while True:
        durationSum = sum(durationList) # sum of all durations in durationList
        if durationSum>signatureVar: # durationSum greater than signatureVar?
            durationList=[] # limit exceeded: empty list, start over
        else:
            if durationSum==signatureVar: # durationSum equal to signatureVar?
                break # durationList complete
            else:
                duration = random.randint(1, durationVar)/durationVar2 # pick a random duration between 1 and 2, steps of 0.25
                durationList.append(duration) # add duration to durationList
    durationList = [0] + durationList # add zero at list start for later use
    return durationList # return list

# Durations to timestamps
def durationsToTimestamps(durationList):
    timestampList = [0]
    timestamps=[]
    times = len(durationList) # repeat for every element in list
    while(times>2):
        times -= 1
        durationList[1] = durationList[1]*4 + durationList[0] # change second item in durationList to timestamp
        timestampList.append(durationList[1]) # add timestamp to timestampList
        durationList.pop(0) # delete timestamp from durationList
    for timestamp in timestampList:
        timestamps.append(timestamp * 15/bpm) # turn 16th timestamps into bpm timestamps
    return timestamps # return list

# Sampleplayer
def sampleplayer(arg, samplename, timestampsFull):
    timestamps = timestampsFull.copy()
    timestamp = timestamps.pop(0)
    startTime = time.time() # retrieve the startime: current time
    keepPlaying = True # play the sequence
    while keepPlaying:
        currentTime = time.time() # retrieve current time
        if(currentTime - startTime >= timestamp): # check if the timestamp's time is passed
            samplePlay = samplename.play() # play sample
            if timestamps: # if there are timestamps left in the timestamps list
                timestamp = timestamps.pop(0) # retrieve the next timestamp
            else: # list is empty, stop loop
                keepPlaying = False
        else: # wait for a very short moment
            time.sleep(0.001)
    time.sleep(1)

def sampleplayers(durationList1, durationList2, durationList3): #Player with threads ending with askReplay function
    timestamps1 = durationsToTimestamps(durationList1.copy())
    timestamps2 = durationsToTimestamps(durationList2.copy())
    timestamps3 = durationsToTimestamps(durationList3.copy())
    replay = True
    while replay:
        thread = Thread(target = sampleplayer, args = (barAmount, hihat, timestamps1), ) #function1, sample1
        thread2 = Thread(target = sampleplayer, args = (barAmount, snare, timestamps2), ) #function2, sample2
        thread3 = Thread(target = sampleplayer, args = (barAmount, kick, timestamps3), ) #function2, sample2
        # start all 3 threads
        thread.start()
        thread2.start()
        thread3.start()
        thread.join()
        thread2.join()
        thread3.join()
        replay = askForReplay()

# MIDI-converter
class midiExport:
    global __MyMIDI, track, channel, volume
    def __init__(self, tempo):
            self.track    = 0
            self.channel  = 10 # channel (drum standard)
            self.volume   = 100  # volume
            self.__MyMIDI = MIDIFile(1) # one track, defaults to format 1 (tempo track is created automatically)
            self.__MyMIDI.addTempo(self.track, 0, tempo) # add tempo (bpm) to file

    def addNotes(self, durationList, midiNote): # this function adds notes one at a time, based on a durationList
        currentTime = 0 # start at position 0
        for duration in durationList:
            self.__MyMIDI.addNote(self.track, self.channel, midiNote, currentTime, .25, self.volume) # add note (track, channel, MIDInumber, time, duration, volume)
            currentTime += duration # move to next position

    def saveMidi(self, filename):
        with open(filename, "wb") as output_file: # create empty file
            self.__MyMIDI.writeFile(output_file) # write MIDIFile
            print()
            print("File saved as", filename) # let user know it's done


#----------------------------------------User-input--------------------------------------------#

# BPM
def askBPM():
    bpmFalse = True
    while True: # create loop
        bpmx = input("Bpm (default = 120):")
        if (bpmx==""): # if enter is pressed, bpm is default
            bpm=bpmDef
            break # answer recieved: stop loop
        else:
            try:
                bpm=int(bpmx) # checking whether input is integer
                break # answer recieved: stop loop
            except ValueError: #if input is not an integer replay loop
                print("False input: bpm input must be an integer (or press enter), try again...")
    return bpm

# Time signatures
def askTimeSignature():
    askSignature = [ # ask user to pick a time signature
        inquirer.List('timesignatures',
            message="Pick an irregular timesignature", # text user will see
            choices=['5/4', '7/8', '9/8'], # give 3 optrions
            ),
    ]
    answer= inquirer.prompt(askSignature) # defining answer = userinput
    signatureSplit = [float(var) for var in (answer['timesignatures']).split("/")] # casting signature text to separate floats
    signatureVar = (signatureSplit[0]/signatureSplit[1])*4 # create variable for later use when creating random beat
    return signatureVar

# Amount of bars generated
def askBarAmount():
    barAmount = int(input("How many bars should I generate? "))
    return barAmount

# Ask for replay
def askForReplay():
    askReplay = [
        inquirer.List('replay or not',
            message="Would you like to hear that again?", # ask user whether they want a replay
            choices=['yes', 'no'], # gives 2 options
        ),
    ]
    if inquirer.prompt(askReplay) == {'replay or not': 'yes'}:
        replay = True
    else:
        replay = False
    return replay

# Ask for save
def askForSave(durationList1, durationList2, durationList3):
    askSave = [
        inquirer.List('save or not',
            message="Would you like to save this beat?", # ask user whether they want to save
            choices=['yes', 'no'], # gives 2 options
        ),
    ]
    if inquirer.prompt(askSave) == {'save or not': 'yes'}:
        exporter = midiExport(bpm)
        exporter.addNotes(durationList1, 42)
        exporter.addNotes(durationList2, 38)
        exporter.addNotes(durationList3, 36)
        exporter.saveMidi(input("Under what name?(add extention .mid): "))

# Ask for restart
def askForRestart():
    askRestart = [
        inquirer.List('restart or not',
            message="What now?", # ask user whether they want a replay
            choices=['Generate new beat', 'Quit program'], # gives 2 options
        ),
    ]
    if inquirer.prompt(askRestart) == {'restart or not': 'Generate new beat'}:
        start = True
    else:
        start = False
    return start

# Samples

#----------------------------------------Program-----------------------------------------------#

print("Welcome!")
time.sleep(1.5)
start = True
while start: #start loop for beatGenerator
    print("Let’s generate some beats!")
    print()
    time.sleep(1)
    signatureVar = askTimeSignature() # userInput
    bpm = askBPM() # userInput
    barAmount = askBarAmount() # userInput
    signatureVar *= barAmount # for 2 bars, generate list with twice the sum
    print()
    print("Get ready...!")
    print()
    time.sleep(2)
    durationListHihat = beatGenerator(4, 4)
    durationListSnare = beatGenerator(4, 2)
    durationListKick = beatGenerator(4, 2)
    sampleplayers(durationListHihat, durationListSnare, durationListKick) # start playing until user stops replay
    askForSave(durationListHihat, durationListSnare, durationListKick) # filesaver
    print()
    start = askForRestart() # restart or quit?
