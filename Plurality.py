import pandas as pd
import numpy as np
from max_tie import max_tie

def Plurality(num_alts, data):
    
    data = data + 1
    
    inds = [i for i in range(1, num_alts + 1)]
    
    alt_winner = None
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
        
        
    for i in inds:
        alts[i] = len(data[data.iloc[:, 0] == i])
    
    return (max_tie(alts))