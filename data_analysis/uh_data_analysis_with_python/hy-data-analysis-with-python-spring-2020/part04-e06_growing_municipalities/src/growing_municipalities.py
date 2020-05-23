#!/usr/bin/env python3

import pandas as pd
import os

def growing_municipalities(df):
    print(df.columns)
    pop_growth = df.columns[1]
    print(pop_growth)
    numerator = df[df[pop_growth] > 0].shape[0]
    denominator = df.shape[0]
    return float(numerator/denominator)

def main():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/', 'municipal.tsv'), sep='\t', index_col='Region 2018')
    df = df['Akaa':'Äänekoski']
    print("Proportion of growing municipalities: {:.1f}%".format(growing_municipalities(df)*100))

if __name__ == "__main__":
    main()
