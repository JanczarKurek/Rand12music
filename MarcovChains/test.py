import string

from music21 import *
import os
import scipy
from music21 import midi

from MarcovChains.marcov import MarcovChainGenerator

panTadeusz = open('pan-tadeusz.txt')
for line, i in zip(panTadeusz, range(20)):
    if i == 20:
        break
    for word in line.split(' '):
        if word in string.whitespace:
            pass
        else:
            print(word)