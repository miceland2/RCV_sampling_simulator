import numpy as np
from random import randrange

def max_tie(alts):
    """
    Randomly choose and return the index of one of the alternatives with the 
    most points
    
    """
    indexes = np.where(alts == alts.max())[0]
    ind = randrange(0, len(indexes))
    return alts.index[indexes[ind]]