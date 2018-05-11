import string

from music21 import *
import os
import scipy
from music21 import midi

from MarcovChains.marcov import MarcovChainGenerator

panTadeusz = open('pan-tadeusz.txt')
marcov = MarcovChainGenerator()
for line in panTadeusz:
    for word in line.split():
        word = "".join(filter(lambda c : '' if c in string.punctuation else c, word))
        word = word.upper()
        marcov.addNext(word)

marcov.setState('TADEUSZ')
for i in range(40):
    print(marcov.getNextState(), end=' ')
