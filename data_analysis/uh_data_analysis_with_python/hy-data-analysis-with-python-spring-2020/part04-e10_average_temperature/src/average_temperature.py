#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    import pandas as pd
    import numpy as np
    import os
    # from pandas_profiling import ProfileReport
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    wh = pd.read_csv(os.path.join(BASE_DIR + '/src/' + 'kumpula-weather-2017.csv'))
    # wh2 = wh.drop(["Year", "m", "d"], axis=1)  # taking averages over these is not very interesting
    wh[wh['m']==7]['Air temperature (degC)']
    return wh[wh['m']==7]['Air temperature (degC)'].mean()

def main():
    print("Average temperature in July: ", str(average_temperature()))
    return

if __name__ == "__main__":
    main()
