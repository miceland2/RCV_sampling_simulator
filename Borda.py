import pandas as pd
import numpy as np
from max_tie import max_tie


def Borda(num_alts, votes):
    
    votes = votes + 1
    
    inds = [i for i in range(1, num_alts + 1)]
    
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    scores = pd.Series()
    
    for i in range(num_alts):
        for j in range(1, num_alts + 1):
            scores = votes.shape[1] - (i + 1)
            alts[j] += scores * votes[votes.iloc[:, i] == float(j)].shape[0]
        
    winner = max_tie(alts)
    return (winner)