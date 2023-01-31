#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:14:21 2023

@author: miceland
"""

from Borda import Borda
from RCV import RCV
from Harmonic_Borda import Harmonic_Borda
from Copeland import Copeland
from Plurality import Plurality
import numpy as np
import pandas as pd
import os

num_alts = 10
num_voters = 100
num_profiles = 100
samples = 100

elections = pd.read_csv('elections_IC.txt', names=[i for i in range(100)])
electionsL = list(elections.iloc[0])
electionsL.insert(0, 'impartial_culture_10_100_0')
electionsL = electionsL[:len(electionsL) - 1]

### FIXME: write a function for generating an estimate rather than copy and 
### pasting the loop structure

print('========== Estimate 5 ==========')
e5 = 0

e5_bool = [False for i in range(num_profiles)]

cnt = 0
for election in electionsL:
        
    f = os.path.join('./IC', election + '.csv')
    votes = pd.read_csv(f)
    col = votes.iloc[:, 1]
    
    #alt_winner = CopelandL(num_alts, votes)                                                                                                                                   
    #alt_winner = PluralityL(num_alts, votes)
    #alt_winner = BordaL(num_alts, votes)
    #alt_winner = Harmonic_BordaL(num_alts, votes)
    alt_winner = RCV(num_alts, votes)
        
    count = np.zeros(10)
    
    for p in range(10, 11):
        for k in range(1):
            votes.iloc[:, 1] = col
            #print(votes)
            s = np.random.choice(num_voters, size=int((num_voters/10)*p), replace=False)
            svotes = votes.iloc[s]
            s_winner = None
            
            #s_winner = CopelandL(num_alts, svotes)
            #s_winner = PluralityL(num_alts, svotes)
            s_winner = Borda(num_alts, svotes)
            #s_winner = Harmonic_BordaL(num_alts, svotes)
            #s_winner = RCVL(num_alts, svotes)
    
            if (s_winner == alt_winner):
                count[p - 1] += 1
                e5 += 1
                e5_bool[cnt] = True
    cnt += 1
    """  
    for i in range(1, 11):
        print("%d0 percent sample: %.2f" %(i, count[i - 1]/100))
    """
    
str_e5 = 'E5: {}/{}'.format(e5, num_profiles)
print(str_e5)
with open('IC_Borda.txt', 'a') as f:
   f.write(str_e5)
   f.write("\n")


print('========== Estimate 4 ==========')
e4 = 0

cnt = 0
for election in electionsL:
        
    f = os.path.join('./IC', election + '.csv')
    votes = pd.read_csv(f)
    col = votes.iloc[:, 1]
    
    #alt_winner = CopelandL(num_alts, votes)                                                                                                                                   
    #alt_winner = PluralityL(num_alts, votes)
    alt_winner = Borda(num_alts, votes)
    #alt_winner = Harmonic_BordaL(num_alts, votes)
    #alt_winner = RCV(num_alts, votes)
        
    count = np.zeros(10)
    
    for p in range(1,2):
        for k in range(samples):
            votes.iloc[:, 1] = col
            #print(votes)
            s = np.random.choice(num_voters, size=int((num_voters/10)*p), replace=False)
            svotes = votes.iloc[s]
            s_winner = None
            
            #s_winner = CopelandL(num_alts, svotes)
            #s_winner = PluralityL(num_alts, svotes)
            s_winner = Borda(num_alts, svotes)
            #s_winner = Harmonic_BordaL(num_alts, svotes)
            #s_winner = RCVL(num_alts, svotes)
    
            if (s_winner == alt_winner):
                count[p - 1] += 1
                e4 += 1
    """
    for i in range(1, 11):
        print("%d0 percent sample: %.2f" %(i, count[i - 1]/100))
    """
    

str_e4 = 'E4: {}/{}'.format(e4, num_profiles * samples)
print(str_e4)
with open('IC_Borda.txt', 'a') as f:
   f.write(str_e4)
   f.write("\n")


print('========== Estimate 3 ==========')
e3 = 0

cnt = 0
for election in electionsL:
        
    f = os.path.join('./IC', election + '.csv')
    votes = pd.read_csv(f)
    col = votes.iloc[:, 1]
    
    #alt_winner = CopelandL(num_alts, votes)                                                                                                                                   
    #alt_winner = PluralityL(num_alts, votes)
    alt_winner = Borda(num_alts, votes)
    #alt_winner = Harmonic_BordaL(num_alts, votes)
    #alt_winner = RCV(num_alts, votes)
        
    count = np.zeros(10)
    
    for i in range(len(e5_bool)):
        for k in range(1, 2):
            votes.iloc[:, 1] = col
                
            
            if (e5_bool[cnt]):
                ss = np.random.choice(num_voters, size=int((num_voters/10)), replace=False)
                ssvotes = votes.iloc[s]
                ss_winner = None
                ss_winner = Borda(num_alts, ssvotes)
                
                if (ss_winner == alt_winner):
                    e3 += 1
                    
                
    cnt += 1
    """  
    for i in range(1, 11):
        print("%d0 percent sample: %.2f" %(i, count[i - 1]/100))
    """
    
str_e3 = 'E3: {}/{}'.format(e3, num_profiles * e5)
print(str_e3)
with open('IC_Borda.txt', 'a') as f:
   f.write(str_e3)
   f.write("\n")



