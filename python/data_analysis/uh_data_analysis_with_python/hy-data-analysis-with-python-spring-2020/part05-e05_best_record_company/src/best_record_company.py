#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    gdp_df = df.groupby('Publisher').sum()
    top_ = gdp_df.sort_values('WoC', ascending=False).index[0]
    final_df = df.loc[df['Publisher']==top_, :]
    return final_df

def main():
    print(best_record_company().head(30))
    return
    

if __name__ == "__main__":
    main()
