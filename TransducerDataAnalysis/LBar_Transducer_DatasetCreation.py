#LBar: Transducer dataset combination and concatenation

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

mw3a = pd.read_excel(r"20804187_MW-3 2021-03-31 08_03_57 -0600.xlsx", header=1)
mw3b = pd.read_excel(r"20804187_MW-3 2021-06-17 13_45_23 -0600.xlsx", header=1)
mw4a = pd.read_excel(r"20820260_MW-4 2021-03-31 07_45_36 -0600.xlsx", header=1)
mw4b = pd.read_excel(r"20820260_MW-4 2021-06-17 13_23_07 -0600.xlsx", header=1)

#here are the 3 old MW3 transducer datasets (already aggregated for daily mean())
mw3_a = pd.read_csv(r"S:\AUS\L-Bar\Mine\NMED\Stage 2 Abatement\GW Monitoring\2020 Sampling\Transducer Data\Exports\HOBO-Export_4-16thru7-22.csv", header=1)
mw3_b = pd.read_csv(r"S:\AUS\L-Bar\Mine\NMED\Stage 2 Abatement\GW Monitoring\2020 Sampling\Transducer Data\Exports\HOBO-Export_7-30thru8-27.csv", header=1)
mw3_c = pd.read_csv(r"S:\AUS\L-Bar\Mine\NMED\Stage 2 Abatement\GW Monitoring\2020 Sampling\Transducer Data\Exports\HOBO-Export_8-27thru10-07.csv", header=1)

mw3_ML = pd.read_excel(r"ManualWL.xlsx", sheet_name='MW3')
mw4_ML = pd.read_excel(r"ManualWL.xlsx", sheet_name='MW4')

#combine the two mw3 dataframe formats, 
#rename and subset columns, then combine again
mw3_1 = pd.concat([mw3a, mw3b])
mw3_2 = pd.concat([mw3_a, mw3_b, mw3_c])

mw3_2.columns = ['#','Date', 'Diff Press','Abs Press','Water Level','EndFile','Bar Press']
mw3_2 = mw3_2[['Date','Abs Press','Bar Press','Diff Press']]

mw3_1a = mw3_1[['Date Time, GMT -0600', 'Abs Press, psi','Baro Press, psi','Diff Press, psi',]]
mw3_1a.columns = ['Date','Abs Press','Bar Press','Diff Press']
mw3_1a = mw3_1a.set_index(['Date'])
mw3_re = mw3_1a.resample('D').mean()
mw3_re = mw3_re.reset_index()
mw3_re['Station'] = 'MW3'

mw3_all = pd.concat([mw3_2, mw3_re])
mw3_all['Station'] = 'MW3'

# define variables from Ashley's workbook
MW3initialDTW = 417.57
MW3datumElev = 6367.39
DiffPress1 = mw3_all.iloc[4,3]
WL_constant = 2.31

mw3_all['Delta Press'] = (DiffPress1 - mw3_all['Diff Press']).astype(float).round(10)
mw3_all['Delta WL'] = (mw3_all['Delta Press']*WL_constant).astype(float).round(8)
mw3_all['DTW'] = (MW3initialDTW + mw3_all['Delta WL']).astype(float).round(8)
mw3_all['Water Elevation'] = (MW3datumElev - mw3_all['DTW']).astype(float).round(8)

#export the update mw3_all dataframe to .csv, review
mw3_all.to_csv("mw3_all.csv", index=False)


#mw4_all
mw4_1 = pd.concat([mw4a, mw4b])
#mw4_2 = pd.concat([mw4_a, mw4_b, mw4_c])

mw4_1.columns = ['#','Date', 'Diff Press','Abs Press','Water Level','EndFile','Bar Press']
mw4_a = mw4_1[['Date','Abs Press','Bar Press','Diff Press']]

#mw3_1a = mw3_1[['Date Time, GMT -0600', 'Abs Press, psi','Baro Press, psi','Diff Press, psi',]]
#mw3_1a.columns = ['Date','Abs Press','Bar Press','Diff Press']
mw4_b = mw4_a.set_index(['Date'])
mw4_c = mw4_b.resample('D').mean()
mw4_c = mw4_c.reset_index()
mw4_c['Station'] = 'MW4'
mw4_all = mw4_c[5:]

# define variables from Ashley's workbook
MW4initialDTW = -384.64
MW4datumElev = 6334.39

DiffPress2 = mw4_all.iloc[4,3]
WL_constant = 2.31

mw4_all['Delta Press'] = (DiffPress2 - mw4_all['Diff Press']).astype(float).round(10)

mw4_all['Delta WL'] = (mw4_all['Delta Press']*WL_constant).astype(float).round(8)

mw4_all['DTW'] = (MW4initialDTW + mw4_all['Delta WL']).astype(float).round(8)

mw4_all['Water Elevation'] = (MW4datumElev + mw4_all['DTW']).astype(float).round(8)

mw4_all.to_csv("mw4_all.csv", index=False)
