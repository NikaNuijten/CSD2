import simpleaudio as sa
import time

sampleBiem = sa.WaveObject.from_wave_file("audioFiles/BIEM.wav")

bpm = 120
playbackTimes = [4, 1, 0.5, 1, 1.5]
numPlaybackTimes = len(playbackTimes) #len = length/size/oid

print("Bpm =", bpm)

#play loop "times" times
times = 4
while(times>0):
    print()
    times -= 1
    #print values to controll with a time delay
    for foo in playbackTimes:
        print("BIEM")
        sampleBiemPlay = sampleBiem.play()
        time.sleep(foo/(bpm/60))
    #time.sleep(1)
    print()
print("Done")
