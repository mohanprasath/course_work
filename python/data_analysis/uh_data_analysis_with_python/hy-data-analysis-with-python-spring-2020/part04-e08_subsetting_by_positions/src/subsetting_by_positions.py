#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    import pandas as pd
    import numpy as np
    import os
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/' + 'UK-top40-1964-1-2.tsv'), sep='\t') #, index_col='Pos') #, header=True)
    return df.iloc[1:11, 2:4]

def main():
    subsetting_by_positions()
    return

if __name__ == "__main__":
    main()
