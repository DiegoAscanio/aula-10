import pdb
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

cidades = ['D', 'M', 'G', 'J', 'P']

distancias = np.array(
    [[0,467,340,327,358],
     [467,0,497,677,843],
     [340,497,0,454,762],
     [327,677,454,0,441],
     [358,843,762,441,0]]
)

MST = minimum_spanning_tree(distancias)
print(MST)
print(MST.sum())
