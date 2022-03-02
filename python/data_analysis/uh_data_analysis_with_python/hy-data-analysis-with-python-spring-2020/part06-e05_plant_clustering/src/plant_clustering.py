#!/usr/bin/env python3

import scipy
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics
from sklearn.cluster import KMeans


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    iris=load_iris()
    # X = iris.data[:, :2]
    # y = iris.target
    # print(X, y)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.8)
    model = KMeans(n_clusters=3, n_jobs = 12, random_state=0)
    model.fit(iris.data)
    centers = model.cluster_centers_
    # print(centers)
    permutation = find_permutation(3, iris.target, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    acc = metrics.accuracy_score(iris.target, new_labels)
    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
