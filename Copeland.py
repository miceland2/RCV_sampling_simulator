import math
import pandas as pd
import numpy as np
from max_tie import max_tie

def Copeland(num_alts, data):
    
    inds = [i for i in range(1, num_alts + 1)]
    
    data = data + 1
    
    alts = pd.Series(np.zeros(num_alts), dtype=int, index=[i for i in range(1, num_alts + 1)])
    alts.index = inds
    
    alt_mat = np.zeros((num_alts, num_alts))
    
    for k in range(data.index.size):
    
        d_test = data.iloc[k]
                
        ranked = []
        cnt = 1
        for i in d_test:
            if (not(math.isnan(i))):
                ranked.append(i)
            if (math.isnan(i)):
                break
            else:
                for j in d_test[cnt:]:
                    if (math.isnan(j)):
                        break
                    alt_mat[int(i) - 1][int(j) - 1] += 1
            cnt+= 1
                
    for i in range(num_alts):
        for j in range(num_alts):
            if (alt_mat[i][j] > alt_mat[j][i]):
                alts[i + 1] += 1
            elif ((alt_mat[i][j] == alt_mat[j][i]) and (i != j)):
                alts[i + 1] += 0.5
                
    
                                
    winner = max_tie(alts)
    return(winner)