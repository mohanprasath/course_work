#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep="\t")
    X = df.loc[:, ['X1', 'X2']]
    # print(X)
    y = df.iloc[:, -1]
    lab_len = len(set(y))
    
    # print(y)
    # print(df.head())
    results = []
    for eps_value in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=eps_value)
        model.fit(X)
        outliers = 0
        clusters_num = len(set(model.labels_))
        # finding outliers
        if -1 in model.labels_:
            clusters_num -= 1
            outliers = list(model.labels_).count(-1)
        permutation = find_permutation(clusters_num, y, model.labels_)
        new_labels = pd.DataFrame([permutation[label] for label in model.labels_]).iloc[:, 0]
        non_outliers_mask = model.labels_ == -1

        if lab_len != clusters_num:
            score = None
        else:
            score = accuracy_score(y[~non_outliers_mask], new_labels[~non_outliers_mask])

        results.append([eps_value, score, clusters_num, outliers])

    return pd.DataFrame(results, columns=['eps', 'Score', 'Clusters', 'Outliers'], dtype=float)

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
