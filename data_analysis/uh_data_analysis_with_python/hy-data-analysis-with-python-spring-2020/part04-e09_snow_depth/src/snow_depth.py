#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    import pandas as pd
    import numpy as np
    import os
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    wh = pd.read_csv(os.path.join(BASE_DIR + '/src/' + 'kumpula-weather-2017.csv'))
    wh2 = wh.drop(["Year", "m", "d"], axis=1)  # taking averages over these is not very interesting
    return wh.describe()['Snow depth (cm)']['max']

def main():
    print("Max snow depth: ", str(snow_depth()))
    return

if __name__ == "__main__":
    main()
