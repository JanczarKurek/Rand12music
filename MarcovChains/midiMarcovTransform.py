from music21 import environment, midi, stream, note

from MarcovChains.marcov import MarcovChainGenerator

def transformMidi(path, firstNote, outputPath):
    mf = midi.MidiFile()
    mf.open(path)
    mf.read()
    mf.close()
    s = midi.translate.midiFileToStream(mf)
    s2 = stream.Stream()
    marcov = MarcovChainGenerator()
    marcov.setInput(lambda note_1: note_1.nameWithOctave)
    for something in s.flat:
        if isinstance(something, note.Note):
            marcov.addNext(something)

    marcov.setState(firstNote)
    for something in s.flat:
        if isinstance(something, note.Note):
            something.nameWithOctave = marcov.getNextState()
            s2.append(something)

    s2.flat.write('midi', fp=outputPath)