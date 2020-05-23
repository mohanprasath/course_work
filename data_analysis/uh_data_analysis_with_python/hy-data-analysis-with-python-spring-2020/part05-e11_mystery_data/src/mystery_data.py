#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv('src/mystery_data.tsv', sep="\t")
    fit = LinearRegression(fit_intercept=False).fit(df.iloc[:,0:5], df.loc[:, 'Y'])
    return fit.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    
if __name__ == "__main__":
    main()
