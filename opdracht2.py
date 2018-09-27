import simpleaudio as sa
import time

bpm=120

replays = (int(input("Amount of replays:")))+1

notelist = input("Insert note durations (use ,):")
playbackTimes = [float(x) for x in notelist.split(",")] # converts string to separate floats
numPlaybackTimes = len(playbackTimes) # len = length/size/oid

sampleBiem = sa.WaveObject.from_wave_file("audioFiles/BIEM.wav")

print()

# play loop "times" times
times = replays
while(times>0):
    times -= 1
    # print values to controll with a time delay
    for foo in playbackTimes:
        print("BIEM")
        sampleBiemPlay = sampleBiem.play()
        time.sleep(foo/(bpm/60))
    print()
time.sleep(1)
print("Done")
