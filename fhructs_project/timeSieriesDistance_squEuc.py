import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram


data = np.array([
    [1, 2, 3, 4, 3, 2, 1, 0],
    [4, 3, 2, 1, 0, 1, 2, 3],
    [0, 1, 2, 3, 4, 3, 2, 1],
    [3, 4, 3, 2, 2, 1, 1, 0],
    [2, 2, 1, 0, 0, 1, 2, 3]
])

distances = pdist(data, metric='sqeuclidean')
dist_matrix = squareform(distances)
Z = linkage(dist_matrix, method='single')

dendrogram(Z)
plt.show()

