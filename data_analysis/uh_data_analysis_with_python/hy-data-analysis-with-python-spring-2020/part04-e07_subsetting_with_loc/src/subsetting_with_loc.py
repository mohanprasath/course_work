#!/usr/bin/env python3

import pandas as pd
import os

def subsetting_with_loc():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/', 'municipal.tsv'), sep='\t', index_col='Region 2018')
    df = df['Akaa':'Äänekoski']
    df = df.loc[:,[ "Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    return df

def main():
    print(subsetting_with_loc())
    return

if __name__ == "__main__":
    main()
