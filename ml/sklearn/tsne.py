'''
This is an example of using t-SNE to visualize the distances and number of clusters in your
dataset for classification.

Inspired by the "Unsupervised Learning" course on Datacamp.com
Author: Alex Nakagawa
'''

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE

# samples is a 2-D array of sample values

# Try different learning rates between 5-200
model = TSNE(learning_rate=100)
transformed = model.fit_transform(samples)

# Taking the index 0 and 1 features and plotting them against each other
xs=transformed[:,0]
ys=transformed[:,1]

plt.scatter(xs,ys, c=species)
plt.show()
