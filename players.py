__author__ = 'angellomaggio'

"""
Copyright (c) 2015, Angello Maggio
All rights reserved.
"""

players = {
    'aguero': {
        'name': 'Kun Aguero',
        'status': '',
        'id': 'aguero',
        'position': 'ST',
        'shot': 82,
        'defense': 63,
        'pace': 82,
        'dribbling': 82,
        'pass': 74,
        'header': 68,
        'reflex': 0,
        'jump': 55,
        'physical': 60,
        'fitness': 100,
        'reliability': 80,
        'loyalty': 80,
        'injuries': None

    },

    'alexis': {
        'name': 'Alexis Sanchez',
        'status': '',
        'id': 'alexis',
        'position': 'RW',
        'shot': 94,
        'defense': 68,
        'pace': 95,
        'dribbling': 94,
        'pass': 90,
        'header': 85,
        'reflex': 0,
        'jump': 70,
        'physical': 80,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'bale': {
        'name': 'Gareth Bale',
        'status': '',
        'id': 'bale',
        'position': 'ST',
        'shot': 83,
        'defense': 63,
        'pace': 94,
        'dribbling': 84,
        'pass': 83,
        'header': 85,
        'reflex': 0,
        'jump': 85,
        'physical': 81,
        'fitness': 100,
        'reliability': 80,
        'loyalty': 85,
        'injuries': None

    },

    'bravo': {
        'name': 'Claudio Bravo',
        'status': '',
        'id': 'bravo',
        'position': 'GK',
        'shot': 88,
        'defense': 95,
        'pace': 75,
        'dribbling': 50,
        'pass': 90,
        'header': 85,
        'reflex': 88,
        'jump': 90,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'buffon': {
        'name': 'Gigi Buffon',
        'status': '',
        'id': 'buffon',
        'position': 'GK',
        'shot': 70,
        'defense': 94,
        'pace': 70,
        'dribbling': 50,
        'pass': 80,
        'header': 80,
        'reflex': 80,
        'jump': 80,
        'physical': 80,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 100,
        'injuries': None

    },

    'casillas': {
        'name': 'Iker Casillas',
        'status': '',
        'id': 'casillas',
        'position': 'GK',
        'shot': 80,
        'defense': 85,
        'pace': 70,
        'dribbling': 70,
        'pass': 80,
        'header': 80,
        'reflex': 85,
        'jump': 90,
        'physical': 80,
        'fitness': 100,
        'reliability': 80,
        'loyalty': 95,
        'injuries': None

    },

    'cavani': {
        'name': 'Edison Cavani',
        'status': '',
        'id': 'cavani',
        'position': '',
        'shot': 80,
        'defense': 60,
        'pace': 80,
        'dribbling': 80,
        'pass': 75,
        'header': 80,
        'reflex': 0,
        'jump': 80,
        'physical': 90,
        'fitness': 100,
        'reliability': 85,
        'loyalty': 90,
        'injuries': None

    },

    'falcao': {
        'name': 'Radamel Falcao',
        'status': '',
        'id': 'falcao',
        'position': 'ST',
        'shot': 85,
        'defense': 60,
        'pace': 70,
        'dribbling': 75,
        'pass': 75,
        'header': 0,
        'reflex': 0,
        'jump': 75,
        'physical': 80,
        'fitness': 100,
        'reliability': 70,
        'loyalty': 80,
        'injuries': None

    },

    'hazard': {
        'name': 'Eden hazard',
        'status': '',
        'id': 'hazard',
        'position': '',
        'shot': 95,
        'defense': 65,
        'pace': 80,
        'dribbling': 90,
        'pass': 80,
        'header': 80,
        'reflex': 0,
        'jump': 80,
        'physical': 80,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'ibrahimovic': {
        'name': 'Ibrahimovic',
        'status': '',
        'id': 'ibrahimovic',
        'position': 'ST',
        'shot': 95,
        'defense': 70,
        'pace': 90,
        'dribbling': 95,
        'pass': 80,
        'header': 95,
        'reflex': 0,
        'jump': 90,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'iniesta': {
        'name': 'Andres Iniesta',
        'status': '',
        'id': 'iniesta',
        'position': 'CM',
        'shot': 80,
        'defense': 85,
        'pace': 80,
        'dribbling': 80,
        'pass': 95,
        'header': 75,
        'reflex': 0,
        'jump': 70,
        'physical': 75,
        'fitness': 100,
        'reliability': 95,
        'loyalty': 100,
        'injuries': None

    },

    'james': {
        'name': 'James Rodriguez',
        'status': '',
        'id': 'james',
        'position': '',
        'shot': 85,
        'defense': 60,
        'pace': 80,
        'dribbling': 80,
        'pass': 80,
        'header': 80,
        'reflex': 0,
        'jump': 80,
        'physical': 85,
        'fitness': 100,
        'reliability': 80,
        'loyalty': 80,
        'injuries': None

    },

    'lahm': {
        'name': 'Philipp Lahm',
        'status': '',
        'id': 'lahm',
        'position': 'RB',
        'shot': 60,
        'defense': 90,
        'pace': 0,
        'dribbling': 85,
        'pass': 90,
        'header': 70,
        'reflex': 0,
        'jump': 70,
        'physical': 85,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'messi': {
        'name': 'Lionel Messi',
        'status': '',
        'id': 'messi',
        'position': '',
        'shot': 99,
        'defense': 60,
        'pace': 98,
        'dribbling': 99,
        'pass': 95,
        'header': 70,
        'reflex': 0,
        'jump': 60,
        'physical': 60,
        'fitness': 100,
        'reliability': 99,
        'loyalty': 100,
        'injuries': None

    },

    'muller': {
        'name': 'Thomas Muller',
        'status': '',
        'id': 'muller',
        'position': 'RM',
        'shot': 90,
        'defense': 70,
        'pace': 85,
        'dribbling': 80,
        'pass': 90,
        'header': 80,
        'reflex': 0,
        'jump': 80,
        'physical': 75,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'neymar': {
        'name': 'Neymar',
        'status': '',
        'id': 'neymar',
        'position': '',
        'shot': 90,
        'defense': 60,
        'pace': 90,
        'dribbling': 90,
        'pass': 80,
        'header': 80,
        'reflex': 0,
        'jump': 70,
        'physical': 70,
        'fitness': 100,
        'reliability': 85,
        'loyalty': 100,
        'injuries': None

    },

    'ozil': {
        'name': 'Mesut Ozil',
        'status': '',
        'id': 'ozil',
        'position': '',
        'shot': 80,
        'defense': 80,
        'pace': 85,
        'dribbling': 85,
        'pass': 95,
        'header': 70,
        'reflex': 0,
        'jump': 70,
        'physical': 75,
        'fitness': 100,
        'reliability': 95,
        'loyalty': 100,
        'injuries': None

    },

    'pirlo': {
        'name': 'Andrea Pirlo',
        'status': '',
        'id': 'pirlo',
        'position': '',
        'shot': 80,
        'defense': 80,
        'pace': 80,
        'dribbling': 80,
        'pass': 99,
        'header': 80,
        'reflex': 0,
        'jump': 80,
        'physical': 80,
        'fitness': 100,
        'reliability': 99,
        'loyalty': 100,
        'injuries': None

    },

    'pogba': {
        'name': 'Paul Pogba',
        'status': '',
        'id': 'pogba',
        'position': '',
        'shot': 80,
        'defense': 75,
        'pace': 80,
        'dribbling': 80,
        'pass': 80,
        'header': 75,
        'reflex': 0,
        'jump': 70,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'ramos': {
        'name': 'Sergio Ramos',
        'status': '',
        'id': 'ramos',
        'position': 'CB',
        'shot': 70,
        'defense': 95,
        'pace': 90,
        'dribbling': 80,
        'pass': 85,
        'header': 85,
        'reflex': 0,
        'jump': 90,
        'physical': 90,
        'fitness': 100,
        'reliability': 85,
        'loyalty': 90,
        'injuries': None

    },

    'robben': {
        'name': 'Robben',
        'status': '',
        'id': 'robben',
        'position': 'ST',
        'shot': 90,
        'defense': 70,
        'pace': 95,
        'dribbling': 90,
        'pass': 80,
        'header': 90,
        'reflex': 0,
        'jump': 80,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 100,
        'injuries': None

    },

    'ronaldinho': {
        'name': 'Ronaldinho',
        'status': '',
        'id': 'ronaldinho',
        'position': '',
        'shot': 90,
        'defense': 50,
        'pace': 90,
        'dribbling': 99,
        'pass': 80,
        'header': 70,
        'reflex': 0,
        'jump': 70,
        'physical': 70,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'ronaldo': {
        'name': 'Cristiano Ronaldo',
        'status': '',
        'id': 'ronaldo',
        'position': 'ST',
        'shot': 99,
        'defense': 75,
        'pace': 90,
        'dribbling': 95,
        'pass': 90,
        'header': 95,
        'reflex': 0,
        'jump': 95,
        'physical': 95,
        'fitness': 100,
        'reliability': 99,
        'loyalty': 95,
        'injuries': None

    },

    'rooney': {
        'name': 'Wayne Rooney',
        'status': '',
        'id': 'rooney',
        'position': 'ST',
        'shot': 90,
        'defense': 60,
        'pace': 85,
        'dribbling': 80,
        'pass': 80,
        'header': 85,
        'reflex': 0,
        'jump': 75,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 100,
        'injuries': None

    },

    'sterling': {
        'name': 'Raheem Sterling',
        'status': '',
        'id': 'sterling',
        'position': 'ST',
        'shot': 90,
        'defense': 60,
        'pace': 85,
        'dribbling': 80,
        'pass': 75,
        'header': 75,
        'reflex': 0,
        'jump': 70,
        'physical': 80,
        'fitness': 100,
        'reliability': 80,
        'loyalty': 70,
        'injuries': None

    },

    'suarez': {
        'name': 'Luis Suarez',
        'status': '',
        'id': 'suarez',
        'position': 'ST',
        'shot': 95,
        'defense': 60,
        'pace': 80,
        'dribbling': 80,
        'pass': 70,
        'header': 80,
        'reflex': 0,
        'jump': 80,
        'physical': 90,
        'fitness': 100,
        'reliability': 85,
        'loyalty': 80,
        'injuries': None

    },

    'vanpersie': {
        'name': 'Van Persie',
        'status': '',
        'id': 'vanpersie',
        'position': '',
        'shot': 90,
        'defense': 60,
        'pace': 80,
        'dribbling': 80,
        'pass': 75,
        'header': 85,
        'reflex': 0,
        'jump': 80,
        'physical': 85,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },

    'vidal': {
        'name': 'Arturo Vidal',
        'status': '',
        'id': 'vidal',
        'position': 'CM',
        'shot': 85,
        'defense': 80,
        'pace': 85,
        'dribbling': 80,
        'pass': 90,
        'header': 90,
        'reflex': 0,
        'jump': 90,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 100,
        'injuries': None

    },

    'xavi': {
        'name': 'Xavi Hernandez',
        'status': '',
        'id': 'xavi',
        'position': 'CM',
        'shot': 85,
        'defense': 80,
        'pace': 80,
        'dribbling': 80,
        'pass': 90,
        'header': 75,
        'reflex': 0,
        'jump': 70,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 100,
        'injuries': None

    },

    'yayatoure': {
        'name': 'Yaya Toure',
        'status': '',
        'id': 'yayatoure',
        'position': 'CDM',
        'shot': 75,
        'defense': 90,
        'pace': 80,
        'dribbling': 80,
        'pass': 90,
        'header': 90,
        'reflex': 0,
        'jump': 90,
        'physical': 90,
        'fitness': 100,
        'reliability': 90,
        'loyalty': 90,
        'injuries': None

    },


    }