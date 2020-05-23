#!/usr/bin/env python3

import pandas as pd

def below_zero():
    import pandas as pd
    import numpy as np
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    wh = pd.read_csv(os.path.join(BASE_DIR + '/src/' + 'kumpula-weather-2017.csv'))
    return wh[wh['Air temperature (degC)']<0]['Year'].count()

def main():
    print("Number of days below zero: ", str(below_zero()))
    return
    
if __name__ == "__main__":
    main()
