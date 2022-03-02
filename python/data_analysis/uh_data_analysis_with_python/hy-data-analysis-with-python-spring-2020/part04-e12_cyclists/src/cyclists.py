#!/usr/bin/env python3

import pandas as pd

def cyclists():
    import pandas as pd
    import numpy as np
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/' + 'Helsingin_pyorailijamaarat.csv'), sep=';')
    return df.dropna(how='all', axis=0).dropna(how='all', axis=1)

def main():
    cyclists()
    return
    
if __name__ == "__main__":
    main()
