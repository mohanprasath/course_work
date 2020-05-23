#!/usr/bin/env python3

import pandas as pd

lst_cities = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']
lst_info = {'Population': [643272, 279044, 231853, 223027, 201810],
'Total area':[715.48, 528.03, 689.59, 240.35, 3817.52]}

def cities():
    df = pd.DataFrame(lst_info, index=lst_cities)
    return df
    
def main():
    print(cities())
    
if __name__ == "__main__":
    main()
