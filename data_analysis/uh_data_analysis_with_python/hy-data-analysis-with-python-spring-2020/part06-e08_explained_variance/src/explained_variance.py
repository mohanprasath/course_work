#!/usr/bin/env python3
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import math
from sklearn.decomposition import PCA

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    print(df.head())
    variance = df.var(axis=0)
    print(variance)
    pca = PCA()
    pca.fit(df)
    explained_variance = pca.explained_variance_
    print(explained_variance)
    return variance, explained_variance

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    print("The variances are:", " ".join([f"{x:.3f}" for x in v]))
    print("The explained variances after PCA are:", " ".join([f"{x:.3f}" for x in ev]))
    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()

if __name__ == "__main__":
    main()
