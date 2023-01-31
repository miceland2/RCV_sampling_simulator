#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:19:47 2022

@author: miceland
"""
import pandas as pd
import mapel


num_alts = 10
num_voters = 100
size = 100

experiment = mapel.prepare_experiment(instance_type='ordinal')

"""
experiment.add_family(culture_id='impartial_culture', size=size,
                              color='green',
                              marker='o', label='IC')


experiment.add_family(culture_id='conitzer', size=size,
                               color='orange', marker='o',
                               label='Conitzer SP')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.1},
                               color='blue', marker='o')


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.2},
                               color='blue', marker='o')


experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.3},
                               color='blue', marker='o')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.4},
                               color='blue', marker='o')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.5},
                               color='blue', marker='o')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.6},
                               color='blue', marker='o')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.7},
                               color='blue', marker='o')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.8},
                               color='blue', marker='o')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 0.9},
                               color='blue', marker='o')

experiment.add_family(culture_id='mallows', size=size,
                               params={'phi': 1.0},
                               color='blue', marker='o',
                               label='Mallows')

experiment.add_family(culture_id='group-separable', size=size,
                                params={'tree': 'balanced'},
                                color='red', marker='o',
                                label='GS')

experiment.add_family(culture_id='walsh', size=size,
                      color='brown', marker='o',
                      label='Walsh')

experiment.add_family(culture_id='single-crossing', size=size,
                      color='navy', marker='o',
                      label='SC')

experiment.add_family(culture_id='euclidean', size=size,
                      params={'dim': 1, 'space': 'uniform'},
                      color='turquoise', marker='o',
                      num_voters=100, label='Unif 1D')
"""
experiment.add_family(culture_id='euclidean', size=size,
                               params={'dim': 5, 'space': 'uniform'},
                               color='purple', marker='o',
                               num_voters=101, label='Unif 5D')

"""
"""


# Generate 100 csv files

for key in experiment.elections.keys():
    data = experiment.elections[key].votes
    df = pd.DataFrame(data)
    df.to_csv(key + ".csv", index=False)

"""
df = pd.DataFrame(experiment.coordinates)
df.to_csv('coordinates.csv')
experiment.compute_distances(distance_id='emd-positionwise')
experiment.embed(algorithm='mds')
"""


### export coordinates and elction names

with open('elections_U5.txt', 'a') as f:
    for e in experiment.elections.keys():
        f.write(str(e) + ",")
        
"""
experiment.print_map()


k = num_elections (for each model) = 100?

do 0.1-1.0 sample for each of them

100 voters, copeute averages in data file (opacities)

"""





