'''
This is an example of cross tabulation tables created from clustering.

Inspired from the "Unsupervised Learning" course on Datacamp.com
Author: Alex Nakagawa
'''

# Import pandas
import pandas as pd

# Fit the pipeline to samples (samples is an array)
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({'labels':labels, 'species':species})

# Create crosstab: ct
ct = pd.crosstab(df['labels'],df['species'])

# Display ct
print(ct)
