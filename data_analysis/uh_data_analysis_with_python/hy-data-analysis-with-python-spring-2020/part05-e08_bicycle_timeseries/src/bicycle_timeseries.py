#!/usr/bin/env python3

import pandas as pd


def clean_df(df):
   
    df2 = df.copy()
    date_column = df2[["Päivämäärä"]]
   # date_column.dropna(how="any",inplace = True)
    dates = date_column["Päivämäärä"].str.split(expand = True)
    dates.rename(columns = {
                0 : "Weekday",
                1 : "Day",
                2 : "Month",
                3 : "Year",
                4 : "Hour"
    },inplace = True)

    dates.Month = dates.Month.map({"tammi":"1","helmi":2,"maalis":3,
                                        "huhti":4,"touko":5,"kesä":6, "heinä":7,
                                        "elo":8,"syys":9,"loka":10,
                                        "marras":11,"joulu":12
                        })

    dates.dropna(how="any")
    dates.drop(["Weekday"],axis = 1,inplace = True)
    print(type(dates.Day[1]),type(dates.Month[1]),type(dates.Year[1]),type(dates.Hour[1]))

    dates.Month = dates.Month.astype(str)
    return dates

def bicycle_timeseries():

    main_df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    main_df = main_df.dropna(how="all",axis=0)
  
    df_dates = clean_df(main_df)
   
    df_dates['NEW'] = df_dates["Year"] +"-"+df_dates["Month"] +"-" + df_dates["Day"] + " " + df_dates["Hour"]
  
    df_dates["test"]= pd.to_datetime(df_dates['NEW'],format='%Y%m%d', errors='ignore')
    df_dates["NEW"] = df_dates["test"].apply(lambda a : pd.Timestamp(a))#.astype(str) #+ " " + df_dates["Hour"]

  
    df_dates.drop(["Day","Month","Year","Hour","test"],axis=1,inplace = True)
    main_df.drop(["Päivämäärä","Unnamed: 21"],axis=1,inplace = True)
    main_df["DatetimeIndex"] = df_dates
    
    main_df.set_index(["DatetimeIndex"],inplace = True)
    print((main_df.head()))
  
   
    return main_df

def main():
    bicycle_timeseries()
    return None

if __name__ == "__main__":
    main()
