#!/usr/bin/env python3

import pandas as pd
import os

def municipalities_of_finland():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/', 'municipal.tsv'), sep='\t', index_col='Region 2018')
    return df['Akaa':'Äänekoski']
    
def main():
    print(municipalities_of_finland())
    return 
    
if __name__ == "__main__":
    main()
