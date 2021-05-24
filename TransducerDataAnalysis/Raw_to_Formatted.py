**Import .xlsx file, concatenate datasets from two stations (MW3, MW4), qa-check, export new file**

#Import packages
import pandas as pd
import seaborn as sns
import numpy as np
import glob


#Load and create the two station/well transducer datasets, dataframes
##*You will be prompted to enter the file pathway & extension for the MW-3/MW-4 datasets*
#Two Wells w/ hobo's: MW-3, MW-4
#load each dataset per well, then add column 'station' == 'MW-3' or 'MW-4'

print("example file path: S\AUS\....Transducer Data\Exports\20804187_MW-3 2021-03-31 08_03_57 -0600.xlsx")
      
MW3_df = pd.read_excel(input(str("Enter MW-3 transducer data path, file, extension: ")), sheet_name="DATA", header=1)
MW3_df = MW3_df.resample('d', on ='Date Time, GMT -0600').mean().reset_index()
MW3_df['station'] = 'MW-3'

MW4_df = pd.read_excel(input(str("Enter MW-4 transducer data path, file, extension: ")), sheet_name="DATA", header=1)
MW4_df = MW4_df.resample('d', on ='Date Time, GMT -0600').mean().reset_index()
MW4_df['station'] = 'MW-4'


#Concatenate the two dataframes vertically: MW3_df, MW4_df
##*Run check to see if dataframes concatenated correctly
##inspect the new dataframe 
#concatenate the two above dataframes

df_concat = pd.concat([MW3_df, MW4_df])
print("concat dataframe shape: " + str(df_concat.shape))

#Concatenation QA check
if len(df_concat) == (len(MW3_df) + len(MW4_df)):
    print("New dataframe shape concatenated vertically OK")
else:
    print("Check previous code; dataframe shape incorrect")
    
#inspect new dataframe
df_concat.head()

#Function to format and build a new dataframe "df"

def formatting():
    
    datetime = pd.to_datetime(pd.Series(df_concat['Date Time, GMT -0600']).rename('datetime'), format = '%YYYY-%mm-%dd %HH:%mm')
    station = pd.Series(df_concat['station']).rename('station')
    AbsPress = pd.Series(df_concat['Abs Press, psi']).rename('Abs Press')
    BaroPress = pd.Series(df_concat['Baro Press, psi']).rename('Baro Press')
    DiffPress = pd.Series(df_concat['Diff Press, psi']).rename('Diff Press')
    
    data = {'datetime': datetime,
           'station': station,
           'Abs Press': AbsPress,
           'Baro Press': BaroPress,
           'Diff Press': DiffPress}
    
    df = pd.DataFrame(data)
    return df

df = formatting()

print(df.head())
print("  ")
print(df.dtypes)


#Describe dataframe (stats), check for null-values

df.describe()
print(df.isna().sum())

#Export the concatenated dataframe as .xlsx to filepath
def export():
    df.to_excel(input(str("Enter the export file path and extension: ")), index=False)

export()