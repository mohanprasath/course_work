#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():

    import pandas as pd
    import numpy as np
    import os
    
    WEEKDAY_MAP = {
    "ma": "Mon",
    "ti": "Tue",
    "ke": "Wed",
    "to": "Thu",
    "pe": "Fri",
    "la": "Sat",
    "su": "Sun"
    }

    MONTH_MAP = {
        "tammi": 1,
        "helmi": 2,
        "maalis": 3,
        "huhti": 4,
        "touko": 5,
        "kesä": 6,
        "heinä": 7,
        "elo": 8,
        "syys": 9,
        "loka": 10,
        "marras": 11,
        "joulu": 12,
    }

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = pd.read_csv(os.path.join(BASE_DIR + '/src/' + 'Helsingin_pyorailijamaarat.csv'), sep=';')
    df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)
    split_dates = df['Päivämäärä'].str.split(expand=True)
    weekday = split_dates[0].map(WEEKDAY_MAP)
    day = split_dates[1].map(int)
    month = split_dates[2].map(MONTH_MAP)
    year = split_dates[3].map(int)
    hour = split_dates[4].str.split(':', expand = True)[0].map(int)
    cols = { 'Weekday': weekday, 'Day': day, 'Month': month, 'Year': year, 'Hour': hour}
    return pd.DataFrame(cols)


def main():
    print(split_date().head(5))
    return
       
if __name__ == "__main__":
    main()
