#!/usr/bin/env python3

import pandas as pd

def top_bands():
    uk_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    bands_df = pd.read_csv("src/bands.tsv", sep="\t")
    print(uk_df.head())
    print(bands_df.head())
    bands_df['Band'] = bands_df['Band'].str.upper()
    merged = pd.merge(bands_df, uk_df, left_on='Band', right_on='Artist')
    return merged

def main():
    top_bands()
    return

if __name__ == "__main__":
    main()
