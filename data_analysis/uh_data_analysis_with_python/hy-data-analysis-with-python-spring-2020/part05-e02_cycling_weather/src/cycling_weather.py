#!/usr/bin/env python3

import pandas as pd

def split_date(df):
    days = {"ma": "Monday", "ti": "Tuesday", "ke": "Wednesday", "to": "Thuday", "pe": "Friday", "la": "Satday", "su": "Sunday"}
    months = {"tammi": 1, "helmi": 2, "maalis": 3, "huhti": 4, "touko": 5, "kesä": 6,
    "heinä": 7, "elo": 8, "syys": 9, "loka": 10, "marras": 11, "joulu": 12,}

    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]

    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]

    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})
    return d

def cycling_weather():
    # file 1
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(how='all') # remove rows with only missing values
    df = df.dropna(how='all', axis='columns') # remove columns with only missing values
    split_df = split_date(df)
    df = df.drop(columns="Päivämäärä")
    pyo_df = pd.concat([split_df, df], axis=1)
    # file 2
    wea_df = pd.read_csv("src/kumpula-weather-2017.csv", sep=",")
    wea_df = wea_df.rename(columns = {'m': 'Month', 'd': 'Day'}, index=str)
    # merging
    merged_df = pd.merge(pyo_df, wea_df)
    merged_df = merged_df.drop(["Time zone", "Time"], axis=1)
    return merged_df

def main():
    df = cycling_weather()
    return

if __name__ == "__main__":
    main()
