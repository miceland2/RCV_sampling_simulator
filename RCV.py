import pandas as pd
import numpy as np
from min_tie import min_tie


def RCV(num_alts, data):
    
    data = data + 1
    
    inds = [i for i in range(1, num_alts + 1)]
    alt_winner = None
    r = 0
    
    while(r < (num_alts - 1)):
        alts = pd.Series(np.zeros(num_alts - r), dtype=int, index=[i for i in range(1, num_alts - r + 1)])
        alts.index = inds
        
        for i in inds:
            alts[i] = len(data[data.iloc[:, 0] == i])
            
        
        for i in list(alts.index):
            if (alts[i] > alts.sum() - alts[i]):
                # If an alternative achieved a majority
                alt_winner = i
    
        alt_min = min_tie(alts)
        alts = alts.drop(alt_min)
        inds = alts.index
        alts.index = inds
        
        data.iloc[:, :] = data.iloc[:, :].replace(float(alt_min), np.nan)
        
        ind = pd.isna(data.iloc[:, 0])
        ind = data[ind].index
        sdata = data.loc[ind].shift(-1, axis=1)
        data.loc[ind] = sdata
        data = data[data.iloc[:, :].notnull().any(axis=1)]
        
        
        r += 1
    return(alt_winner)