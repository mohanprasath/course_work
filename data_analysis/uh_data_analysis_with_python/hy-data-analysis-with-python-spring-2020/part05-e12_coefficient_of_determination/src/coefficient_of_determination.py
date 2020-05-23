#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression


def find_score(X, y):
    return LinearRegression(fit_intercept=True).fit(X, y).score(X, y)

def coefficient_of_determination():
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')
    X = df.loc[:, 'X1':'X5']
    y = df.loc[:, 'Y']
    score_all = find_score(X, y)
    num_of_features = X.shape[1]
    single_feature_scores = [find_score(X.iloc[:, [i]], y) for i in range(0, num_of_features)]
    return [score_all] + single_feature_scores

def main():
    for idx, coef in enumerate(coefficient_of_determination()):
        idx = str(idx) if idx else ''
        print("R2-score with feature(s) X{} is: {}".format(idx, coef))

if __name__ == "__main__":
    main()
