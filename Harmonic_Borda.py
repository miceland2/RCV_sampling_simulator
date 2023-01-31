import pandas as pd
import numpy as np
from max_tie import max_tie


def Harmonic_Borda(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    scores = pd.Series()
    
    for i in range(num_alts):
        for j in range(1, num_alts + 1):
            scores = 1 / (i + 1)
            alts[j] += scores * data[data.iloc[:, i] == float(j)].shape[0]
        
    winner = max_tie(alts)
    return (winner)