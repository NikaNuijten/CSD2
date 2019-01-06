import simpleaudio as sa
import time
import random

# load 2 audiofiles into a list
sampleBiem = sa.WaveObject.from_wave_file("audioFiles/BIEM.wav")
sampleBell = sa.WaveObject.from_wave_file("audioFiles/Bell.wav")
samples = [sampleBiem, sampleBell]

# set bpm
bpmFalse = True
while True: # create loop
    bpmx = input("Bpm (default = 120):")
    if (bpmx==""): # if enter is pressed, bpm is default 120
        bpm=120
        break # answer recieved: stop loop
    else:
        try:
            bpm=int(bpmx) # checking whether input is integer
            break # answer recieved: stop loop
        except ValueError: #if input is not an integer replay loop
            print("False input: bpm input must be an integer (or press enter), try again...")

# replay amount
replays = int(input("Amount of replays:"))

# create a list to hold the timestamps
timestamps = []

# durationsToTimestamps16th Function
inputDurations = input("Insert note durations (use ,):")
durationList = [float(x) for x in inputDurations.split(",")] # durations to floats

durationList = [0] + durationList
timestampList =[] #create empty timestampsList

times = len(durationList)
while(times>2):
    times -= 1
    durationList[1] = durationList[1]*4 + durationList[0]
    timestampList.append(durationList[1])
    durationList.pop(0)


# transform the sixteenthTimestamps to a timestamps list with time values
for timestamp in timestampList:
  timestamps.append(timestamp * 15/bpm)

#replays
timestampsCopy = timestamps.copy() #copy timestamps list
times = replays
while(times>0):
    times -= 1
    #timestampsNew = timestamps.copy()
    timestampsNew = [x+2 for x in timestampsCopy]
    timestampsCopy = timestampsNew.copy()
    timestamps.extend(timestampsNew) #extend timestamps to timestamps

# retrieve first timestamp
# NOTE: pop(0) returns and removes the element at index 0
timestamp = timestamps.pop(0)
# retrieve the startime: current time
startTime = time.time()
keepPlaying = True
# play the sequence
while keepPlaying:
  # retrieve current time
  currentTime = time.time()
  # check if the timestamp's time is passed
  if(currentTime - startTime >= timestamp):
    # pick random sample
    sampleRand = random.choice(samples)
    print(sampleRand)
    # play sample
    sampleRandPlay = sampleRand.play()

    # if there are timestamps left in the timestamps list
    if timestamps:
      # retrieve the next timestamp
      timestamp = timestamps.pop(0)
    else:
      # list is empty, stop loop
      keepPlaying = False
  else:
    # wait for a very short moment
    time.sleep(0.001)
#make sure last sample isn't cut off
time.sleep(1)
print("done")
