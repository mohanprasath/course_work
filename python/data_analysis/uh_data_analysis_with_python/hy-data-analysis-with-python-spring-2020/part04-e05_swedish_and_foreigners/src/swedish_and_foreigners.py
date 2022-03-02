#!/usr/bin/env python3

import pandas as pd
import os

def swedish_and_foreigners():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/', 'municipal.tsv'), sep='\t', index_col='Region 2018')
    df = df['Akaa':'Äänekoski']
    swedish = df.columns[2]
    foreigners = df.columns[3]
    df = df[(df[swedish] > 5.0) & (df[foreigners] > 5.0)]
    return df[df.columns[[0, 2, 3]]]

def main():
    print(swedish_and_foreigners())
    return

if __name__ == "__main__":
    main()
