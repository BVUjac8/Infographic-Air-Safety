# Julia Cuellar
# DSC 640
# Infographic

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Will use in Infographic
def read_file():
    air = pd.read_csv('air-safety.csv')
    print("Display data with null:\n", air.isnull())
    print("Display counts of null from data:\n", air.isnull().sum())
    print('Data:\n', air)
    line = air['airline']
    fat_1 = air['fatalities_00_14']
    fat_2 = air['fatalities_85_99']
    plt.bar(line, fat_1, color='y')
    plt.bar(line, fat_2, bottom=fat_1, color='m')
    plt.xlabel('airline')
    plt.xticks(rotation=30, ha='right')
    plt.xticks(size=5)
    plt.legend(['fatalities_00_14', 'fatalities_85_99'])
    plt.title('Airline Fatalities', font='Tempus Sans ITC', fontsize=15)
    plt.grid()
    plt.show()


# Will use in Infographic
def read_file2():
    fin = pd.read_csv('Financials_Full_Data_data.csv')
    print("Display data with null:\n", fin.isnull())
    print("Display counts of null from data:\n", fin.isnull().sum())
    print('Data:\n', fin)
    fin.plot(x="Year", y=["Total Operating Expense", "Total Operating Revenue"], color='ym')
    plt.title('Airline Operating Expense & Revenue', font='Tempus Sans ITC', fontsize=15)
    plt.grid()
    plt.show()


# Will use in Infographic
def read_file3():
    safe = pd.read_csv('Safety Record of U.S. Air Carriers.csv')
    print("Display data with null:\n", safe.isnull())
    print("Display counts of null from data:\n", safe.isnull().sum())
    print('Data:\n', safe)


# Will use in Infographic
def read_file4():
    seat = pd.read_csv('Seat.csv')
    print("Display data with null:\n", seat.isnull())
    print("Display counts of null from data:\n", seat.isnull().sum())
    print('Data:\n', seat)


if __name__ == "__main__":
    read_file()
    read_file2()
    read_file3()
    read_file4()