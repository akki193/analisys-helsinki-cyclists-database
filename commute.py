#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def bicycle_timeseries():
    file = "Helsingin_pyorailijamaarat.csv"
    data = pd.read_csv(file, sep=";")
    data = data.dropna(how="all", axis=0).dropna(how="all", axis=1)

    wd_hashmap = {"ma": "Mon", 
                  "ti": "Tue", 
                  "ke": "Wed", 
                  "to": "Thu", 
                  "pe": "Fri", 
                  "la": "Sat", 
                  "su": "Sun"}
    
    m_hashmap = {"tammi": 1,
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
                 "joulu": 12}
    
    col = data["Päivämäärä"].str.split(expand=True)
    col.columns = ["Weekday", "Day", "Month", "Year", "Time"]
    col["Weekday"] = col["Weekday"].replace(wd_hashmap)
    col["Month"] = col["Month"].replace(m_hashmap)
    col = col.astype(str)
    

    


    data["Date"] = pd.to_datetime(col["Year"]+"-"+
                                  col["Month"]+"-"+
                                  col["Day"]+" "+
                                  col["Time"])
    data["Weekday"] = col["Weekday"]
    data = data.set_index("Date")
    data = data.drop("Päivämäärä", axis=1)

    return data

def commute():
    data = bicycle_timeseries()
    res_data = data["2017-08-01":"2017-08-31"]
    wd_to_nums = dict(zip(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], [1,2,3,4,5,6,7]))
    groups = res_data.groupby("Weekday").sum()
    groups.index = groups.index.map(wd_to_nums)
    groups = groups.sort_index()
    
    return groups
    
def main():
    df = commute()
    plt.plot(df)
    plt.show()


if __name__ == "__main__":
    main()
