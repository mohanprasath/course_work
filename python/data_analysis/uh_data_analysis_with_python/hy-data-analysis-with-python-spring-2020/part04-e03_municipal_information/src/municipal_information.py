#!/usr/bin/env python3

import pandas as pd
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    # df = pd.read_csv(os.path.join(BASE_DIR, 'municipal.tsv'), sep='\t')
    file_path = os.path.join(os.path.dirname(sys.argv[0]), "..", "src", 'municipal.tsv')
    df = pd.read_csv(file_path, sep='\t')
    print("Shape: %s, %s" % df.shape)
    print('Columns:')
    for column in df.columns:
        print(column)

if __name__ == "__main__":
    main()
