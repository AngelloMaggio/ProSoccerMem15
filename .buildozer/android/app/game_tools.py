"""
Copyright (c) 2015, Angello Maggio
All rights reserved.
"""

from glob import glob
from os.path import dirname, join, basename


def best_ratio(nb,width,height):
    row = 1
    correct_ratio = 1.
    min_err = None
    nbparrow = nb/row
    if nb % row != 0:
        nbparrow += 1
    x = float(width)/nbparrow
    y = float(height)/row
    ratio = x/y
    min_err = abs(ratio-correct_ratio)
    while ratio < correct_ratio:
        row += 1
        nbparrow = nb/row
        if nb % row != 0:
            nbparrow += 1
        x = float(width)/nbparrow
        y = float(height)/row
        ratio = x/y
        if abs(ratio-correct_ratio)> min_err:
            row -= 1
        min_err = abs(ratio-correct_ratio)
    return row


def load_data():
    sounds = {}
    icons = []
    for s in glob(join(dirname(__file__), "sounds", '*.wav')):
        name=basename(s[:-4]).split("_")[0]
        if sounds.has_key(name):
            sounds[name].append(s)
        else:
            sounds[name]=[s]
    for i in glob(join(dirname(__file__), "icons", '*.png')):
        icons.append(i)
    return sounds, icons