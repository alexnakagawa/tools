'''
This is an example of a dendrogram plot showing the hierarchical structure of clustering.

Inspired from the "Unsupervised Learning" course on Datacamp.com
Author: Alex Nakagawa
'''

# Import normalize
from sklearn.preprocessing import normalize

# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, 'complete')

# Plot the dendrogram
dendrogram(mergings, labels=companies, leaf_rotation=90, leaf_font_size=6)
plt.show()
