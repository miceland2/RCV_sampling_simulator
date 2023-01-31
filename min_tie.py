import numpy as np
from random import randrange

def min_tie(alts):
    """
    Randomly choose and return the index of one of the alternatives with the 
    least points
    
    """
    indexes = np.where(alts == alts.min())[0]
    ind = randrange(0, len(indexes))
    return alts.index[indexes[ind]]