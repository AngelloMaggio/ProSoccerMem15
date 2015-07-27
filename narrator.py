__author__ = 'Angello Maggio'

"""
Copyright (c) 2015, Angello Maggio
All rights reserved.
"""


def narrate(counter, forwards):

    try:
        counter = int(counter)
    except ValueError:
        return 0, "Wrong input."

    if forwards:
        if counter == -3:
            narration = "What a save by the goalie!"
        if counter == -2:
            narration = "The defense kicks it out."
        if counter == -1:
            narration = "The DM sends it back to the midfield and they fight for it."
        if counter == 0:
            narration = "They manage to move it fowards."
        if counter == 1:
            narration = "It's him versus the defense!"
        if counter == 2:
            narration = "Alone against the goalie!!"
        if counter == 3:
            narration = "Gooooooooooal! For the home team!"
        counter += 1

    if not forwards:
        if counter == -3:
            narration = "Gooooooooooal! For the away team!"
        if counter == -2:
            narration = "It's up to the goalie!!"
        if counter == -1:
            narration = "He goes towards the defense!"
        if counter == 0:
            narration = "The enemy gains posession in the midfield."
        if counter == 1:
            narration = "The enemy bring it back midfield."
        if counter == 2:
            narration = "Their defense was too strong"
        if counter == 3:
            narration = "What a save by the keep!!"
        counter -= 1

    return counter, narration