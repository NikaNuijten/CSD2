import random

inputMelody = [[1, 1, 120], [2, 2, 120], [3, 3, 120], [4, 4, 120]]
layer1 = []
#inputMelodyCopy = []

def copyList(list):
    listcopy = []
    for note in list:
        listcopy.append(note)
    return listcopy

def shuffleTransform(list): # Randomly shuffles the note or duration values
    random.shuffle(list)
    return list

def invertTransform(list):
    list.reverse()
    return list

def getNotes(list, noteList): # Outputs a list of midi note values from the list
    for note in list:
        noteList.append(note[0])
        note.pop(0)
    #return noteList

def getDurations(list, durationList): # Outputs a list of duration values from the list
    for note in list:
        durationList.append(note[0])
        note.pop(0)
    #return durationList

def combineMelody(list, noteList, durationList): # Combines the note and durationvalues
    for note in list:
        note.insert(0, durationList[0])
        durationList.pop(0)
        note.insert(0, noteList[0])
        noteList.pop(0)
    return list

def melodyTransform():
    inputNotes = []
    inputDurations = []
    layer1.append(inputMelody)
    getNotes(inputMelodyCopy, inputNotes)
    getDurations(inputMelodyCopy, inputDurations)
    print("inputMelodyCopy na getNotes&durations=", inputMelodyCopy)
    print("inputMelody na getNotes&durations=", inputMelody)
    inputNotes = shuffleTransform(inputNotes)
    inputDurations = shuffleTransform(inputDurations)
    combineMelody(inputMelodyCopy, inputNotes, inputDurations)
    print("inputMelodyCopy na combine=", inputMelodyCopy)
    print("inputMelody na combine=", inputMelody)
    layer1.append(inputMelodyCopy)
    return layer1

inputMelodyCopy = copyList(inputMelody)
print("inputMelodyCopy=", inputMelodyCopy)
print("inputMelody=", inputMelody)
melodyTransform()
print("inputMelodyCopy na functie=", inputMelodyCopy)
print("inputMelody na functie=", inputMelody)

#print("layer1End", layer1)
