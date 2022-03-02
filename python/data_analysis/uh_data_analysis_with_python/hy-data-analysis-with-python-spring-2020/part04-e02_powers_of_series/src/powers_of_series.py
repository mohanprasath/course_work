#!/usr/bin/env python3

import pandas as pd
import numpy as np

def powers_of_series(s, k):
    temp = np.arange(1, k+1)
    new_temp = s.values ** temp[:, np.newaxis]
    transposed_new_temp = np.transpose(new_temp)
    df = pd.DataFrame(transposed_new_temp, index = s.index, columns=temp)
    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    return
    
if __name__ == "__main__":
    main()
