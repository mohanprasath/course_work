#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    
    SPECIAL_VALUES = ['New', 'Re']
    import pandas as pd
    import numpy as np
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/' + 'UK-top40-1964-1-2.tsv'), sep='\t')
    df.loc[df.LW.isin(SPECIAL_VALUES), 'LW'] = None
    df.loc[df.Pos.isin(SPECIAL_VALUES), 'Pos'] = None
    df.Pos = pd.to_numeric(df.Pos)
    df.LW = pd.to_numeric(df.LW)
    declining = df[df.LW < df.Pos]
    return declining

def main():
    print(special_missing_values())
    return

if __name__ == "__main__":
    main()
