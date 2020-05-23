#!/usr/bin/env python3

import scipy.stats
import numpy as np
import os
import sys

def load2():
    """This loads the data from the internet. Does not work well on the TMC server."""
    import seaborn as sns
    return sns.load_dataset('iris').drop('species', axis=1).values

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    iris_data = load()
    sepal_length = iris_data[:, 0]
    petal_length = iris_data[:, 2]
    corr = scipy.stats.pearsonr(sepal_length, petal_length)[0]
    return corr

def correlations():
    iris_data = load()
    return np.corrcoef(iris_data, rowvar=False)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
