from music21 import *
import os
import scipy
from music21 import midi

from MarcovChains.marcov import MarcovChainGenerator

mf = midi.MidiFile()
environment.set('musicxmlPath', '/usr/bin/musescore')
environment.set('midiPath', '/usr/bin/fluidsynth')
mf.open("Fur Elise.mid")
mf.read()
mf.close()
s = midi.translate.midiFileToStream(mf)
s2 = stream.Stream()
marcov = MarcovChainGenerator()
marcov.setInput(lambda note_1 : note_1.nameWithOctave)
for something in s.flat:
    if isinstance(something, note.Note):
        print(something)
        marcov.addNext(something)
        # s2.append(something.)
    else:
        print("Not a note nor chord===", something)

print(marcov.transitions)
marcov.setState('C4')
for something in s.flat:
    if isinstance(something, note.Note):
        something.nameWithOctave = marcov.getNextState()
        s2.append(something)

s2.flat.write('midi', fp='output2.mid')
