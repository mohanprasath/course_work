#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    ids = index=list("abc")
    return (pd.Series(L1, index=ids), pd.Series(L2, index=ids))
    
def modify_series(s1, s2):
    s1['d'] = s2['b']
    s2 = s2.drop("b")
    return (s1, s2)
    
def main():
    s1, s2  = create_series([1, 2, 3], [4, 5, 6])
    s1_modified, s2_modified = modify_series(s1, s2)
    print(s1_modified + s2_modified)
    
if __name__ == "__main__":
    main()
