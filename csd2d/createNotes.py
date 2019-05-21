import music21 as m21

# a list with some custom notes, using a custom structure:
# [pitch, quarter_note_length, velocity]
custom_notes = [[60, 1, 100], [62, 2, 80], [64, 1, 60], [60, 4, 100]]

def create_notes(input_notes):
    """
    Transforms a list of notes to m21 notes.

    Parameters:
    input_notes - a list of notes, each note defined as a list:
                  [pitch, quarter_note_length, velocity]

    Returns:
    A list of m21 notes.
    """

    # instantiate new list
    notes =[]
    for n in input_notes:
        # create m21 note
        note = m21.note.Note()
        # to work with midi note values --> create a pitch object with
        # midi parameter and assign this pitch object to note.pitch
        note.pitch = m21.pitch.Pitch(midi=n[0])
        # set notelength and velocity
        note.quarterLength=n[1]
        note.volume.velocity = n[2]
        # add note to m21 notes list
        notes.append(note)

    return notes



def notes_to_stream(notes):
    """
    Creates a m21 stream adds the m21 notes in the passed list and returns the
    stream.

    Parameters:
    notes: - A list of m21 notes.

    Returns:
    A m21 stream.
    """
    # instantiate treble clef
    clef = m21.clef.TrebleClef()
    # number --> number of flats (negative) or sharps (positive)
    key_signature = m21.key.KeySignature(-2)

    # instantiate stream
    stream = m21.stream.Stream()
    stream.clef = clef
    stream.timeSignature = m21.meter.TimeSignature('2/4')
    stream.keySignature = key_signature
    # add notes

    stream.append(notes)

    return stream


# call functions
notes = create_notes(custom_notes)

stream = notes_to_stream(notes)
stream.show()
