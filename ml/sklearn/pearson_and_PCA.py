'''
This is an example of finding the Pearson correlation coefficient as well as Principal Component Analysis (PCA).
PCA transforms the data to align with the axes (mean of 0) without loss of information.

Inspired by the "Unsupervised Learning" course on Datacamp.com
Author: Alex Nakagawa
'''

import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.decomposition import PCA

# Assign the 0th column of grains: width
width = df[:,0]

# Assign the 1st column of grains: length
length = df[:,1]

plt.scatter(width, length)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width, length)
print(correlation)


# Create PCA instance: model
model = PCA()
pca_features = model.fit_transform(df)

xs = pca_features[:,0]
ys = pca_features[:,1]

# Scatter plot xs vs ys
plt.scatter(xs, ys)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation after PCA
correlation, pvalue = pearsonr(xs, ys)
print(correlation)