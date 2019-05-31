
import random

input_melody = [[1, 1, 120], [2, 2, 120], [3, 3, 120], [4, 4, 120], [5, 5, 120]]
layer1 = input_melody.copy()

def shuffle(list_):
	random.shuffle(list_)

def reverse(list_):
	list_.reverse()

def melody_transform(input_melody):
	pitch = []
	duration = []
	for note in input_melody:
		pitch.append(note[0])
		duration.append(note[1])
	shuffle(pitch)
	reverse(duration)
	print(pitch)
	for i in range(0, len(input_melody)):
		layer1.append([pitch[i], duration[i], 120])

print("input:  {}".format(input_melody))
melody_transform(input_melody)
print("layer1: {}".format(layer1))
