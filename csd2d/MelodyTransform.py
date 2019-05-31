import random

inputMelody = [[1, 1, 120], [2, 2, 120], [3, 3, 120], [4, 4, 120]]
layer1 = []
function = []
inputPitches = []
inputDurations = []
newPitches = []
newDurations = []

def shuffleTransform(list): # Randomly shuffles the note or duration values
    random.shuffle(list)
    return list

def invertTransform(list): # Inverts the note or duration values
    list.reverse()
    return list


def transform(list):
    transformations = ["shuffle", "invert"]
    newList = []
    function = random.choice(transformations)
    if function == "shuffle":
        newList = shuffleTransform(list)
    else:
        newList = invertTransform(list)
    return newList

def melodyTransform():
    layer1 = inputMelody.copy()
    for note in inputMelody:
        inputPitches.append(note[0])
        inputDurations.append(note[1])
    length = 20
    repeat = length/len(inputPitches)
    while repeat > 0:
        newList = transform(inputPitches)
        for pitch in inputPitches:
            newPitches.append(pitch)
        newList = transform(inputDurations)
        for duration in inputDurations:
            newDurations.append(duration)
        repeat -= 1
    for i in range(0, length-len(inputPitches)):
        layer1.append([newPitches[i], newDurations[i], 120])
    return layer1


#melodyTransform()
layer1 = melodyTransform()
print(layer1)


#print("layer1End", layer1)
