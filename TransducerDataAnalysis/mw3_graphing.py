#Creating Date vs. Pressure graphs for LBar Semi-Annual Reporting Deliverables

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

months = mdates.MonthLocator()  # every month

#'mw3_all.csv' was created through combinating, wrangling data from HoboWare Transducer exports
mw3_all = pd.read_csv(r"mw3_all.csv")
mw3_all['Date'] = pd.to_datetime(mw3_all['Date'])

#'mw3_ML' is manual water elevation data from field sampling
mw3_ML = pd.read_excel(r"ManualWL.xlsx", sheet_name='MW3')

#creating scatter plot for plot: "Date" vs "Water Elevation"
#sns.scatterplot()  add the manual waterlevel data array as another series
sns.scatterplot(x=mw3_all['Date'][5:], y=mw3_all['Water Elevation'][5:], data=mw3_all, label='OnSet Data Logger')
sns.scatterplot(x=mw3_ML['Date'], y=mw3_ML['Manual DTW'], data=mw3_all, markers = 'X',label='Manual WLs')
plt.title("Figure 6: MW-3 Average Daily Differential Pressure")
plt.xlabel("Date")
plt.ylabel("Groundwater Elevation (ft amsl)")
plt.xticks(rotation=45)
myFmt = mdates.DateFormatter('%b-%Y')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()
plt.grid()
plt.savefig("MW3_Transducer_WaterLevel_Graph.png")


#creating scatterplot for "Date" vs "Differential Pressure"
sns.scatterplot(x=mw3_all['Date'][5:], y=mw3_all['Diff Press'][5:], data=mw3_all, label='OnSet Diff. Pressure')
#sns.lineplot(x=mw3_all['Date'][5:], y=mw3_all['Diff Press'][5:], data=mw3_all, label='OnSet Diff. Pressure')
#sns.scatterplot(x=mw4_ML['Date'], y=mw4_ML['Water Level'], data=mw4_ML, markers = 'X',label='Manual WLs')
plt.title("Figure 7: MW-3 Average Daily Differential Pressure")
plt.xlabel("Date")
plt.ylabel("Differential Pressure (psi)")
plt.xticks(rotation=45)
myFmt = mdates.DateFormatter('%b-%Y')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()
plt.grid()
plt.tight_layout()
#plt.savefig("MW3_Transducer_DiffPress_Graph.png")