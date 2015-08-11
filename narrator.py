__author__ = 'Angello Maggio'

"""
Copyright (c) 2015, Angello Maggio
All rights reserved.
"""

from players import players
from random import randint
from random import choice


def narrate(counter, forwards, player_id):

    narration = "Error, no narration assigned."

    try:
        counter = int(counter)
    except ValueError:
        return 0, "Wrong input."

    player = players[player_id]

    # If the guess was right
    if forwards:

        if counter == -3:
            if player['defense'] > randint(0, 100):
                narration = player['name'] + " saves the ball on the line!"
                counter += 1
            else:
                narration = player['name'] + " couldn't clear it! Stays on the box!"

        elif counter == -2:
            if player['defense'] > randint(0, 100):
                narration = player['name'] + " defends well and sends it out."
                counter += 1
            else:
                narration = player['name'] + " couldn't stop enemy team from advancing!"

        elif counter == -1:
            if player['pass'] > randint(0, 100):
                narration = player['name'] + " sends it back to the midfield and they fight for it."
                counter += 1
            else:
                narration = player['name'] + " misses the pass and the enemy puts pressure."

        elif counter == 0:
            if player['pass'] > randint(0, 100):
                narration = player['name'] + " with a great pass fowards."
                counter += 1
            else:
                narration = player['name'] + " misses the pass and the enemy puts pressure."

        elif counter == 1:
            if player['pass'] > randint(0, 100):
                narration = player['name'] + " plays it into attacking area..."
                counter += 1
            else:
                narration = player['name'] + " couldn't handle the pressure and lost it."

        elif counter == 2:
            if player['dribbling'] > randint(0, 100):
                narration = player['name'] + " dribles through the defense and leaves it for a shot!"
                counter += 1
            else:
                narration = player['name'] + " messes up in attacking area..."

        elif counter == 3:
            if player['shot'] > randint(0, 100):
                narration = player['name'] + " shoots! Gooooooooooal for the home team!"
                counter += 1
            else:
                narration = player['name'] + " shoots! But it hits the post!"

    # If didn't guess right
    if not forwards:

        if counter == -3:
            if choice([85, 70, 60]) > randint(0, 100):
                narration = "Gooooooooooal! For the away team!"
                counter -= 1
            else:
                narration = "But the goalie saves it!"
                counter += 1

        elif counter == -2:
            if choice([90, 75, 50]) > randint(0, 100):
                narration = "It's up to the goalie!!"
                counter -= 1
            else:
                narration = "But the ball is intercepted by the home team!"
                counter += 1

        elif counter == -1:
            if choice([80, 78, 60]) > randint(0, 100):
                narration = "He goes towards the defense!"
                counter -= 1
            else:
                narration = "The home defense puts good pressure."
                counter += 1

        elif counter == 0:
            if choice([83, 76, 70]) > randint(0, 100):
                narration = "The enemy gains posession in the midfield."
                counter -= 1
            else:
                narration = "Midfielders recover it for the home team!"
                counter += 1

        elif counter == 1:
            if choice([80, 75, 70]) > randint(0, 100):
                narration = "The enemy bring it back midfield."
                counter -= 1
            else:
                narration = "The enemy can't get out of their area..."
                counter += 0

        elif counter == 2:
            if choice([90, 80, 70]) > randint(0, 100):
                narration = "Their defense was too strong"
                counter -= 1
            else:
                narration = "Enemy defenders fight to get it out!"
                counter += 0

        elif counter == 3:
            if choice([90, 80, 60]) > randint(0, 100):
                narration = "What a save by the keep!!"
                counter -= 1
            else:
                narration = "The goalie saves it but it's still in the box!"
                counter += 0

    return counter, narration