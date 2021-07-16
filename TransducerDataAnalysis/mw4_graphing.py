#Creating Date vs. Pressure graphs for LBar Semi-Annual Reporting Deliverables

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

months = mdates.MonthLocator()  # every month

mw4_all = pd.read_csv(r"mw4_all.csv")
mw4_all['Date'] = pd.to_datetime(mw4_all['Date'])

mw4_ML = pd.read_excel(r"ManualWL.xlsx", sheet_name='MW4')

#Creating graph 1:
#sns.scatterplot()  add the manual waterlevel data array as another series
sns.scatterplot(x=mw4_all['Date'][5:], y=mw4_all['Water Elevation'][5:], data=mw4_all, label='OnSet Data Logger')
sns.scatterplot(x=mw4_ML['Date'], y=mw4_ML['Water Level'], data=mw4_ML, markers = 'X',label='Manual WLs')
plt.title("Figure 7: MW-4 Average #### Pressure")
plt.xlabel("Date")
plt.ylabel("Groundwater Elevation (ft amsl)")
plt.xticks(rotation=45)
myFmt = mdates.DateFormatter('%b-%Y')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()
plt.grid()
plt.savefig("MW4_Transducer_####_Graph.png")

#Creating graph3:
#sns.scatterplot()  add the manual waterlevel data array as another series
sns.scatterplot(x=mw4_all['Date'][5:], y=mw4_all['Diff Press'][5:], data=mw4_all, label='OnSet Diff. Pressure')
#sns.lineplot(x=mw4_all['Date'][5:], y=mw4_all['Diff Press'][5:], data=mw4_all, label='OnSet Diff. Pressure')
#sns.scatterplot(x=mw4_ML['Date'], y=mw4_ML['Water Level'], data=mw4_ML, markers = 'X',label='Manual WLs')
plt.title("Figure 7: MW-4 Average Daily Differential Pressure")
plt.xlabel("Date")
plt.ylabel("Differential Pressure (psi)")
plt.xticks(rotation=45)
myFmt = mdates.DateFormatter('%b-%Y')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("MW4_Transducer_DiffPress_Graph.png")