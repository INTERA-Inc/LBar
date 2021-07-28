#Creating Date vs. Pressure graphs for LBar Semi-Annual Reporting Deliverables
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdate
from matplotlib.dates import DateFormatter
import os

df0 = pd.read_excel(r"LBar_AppB_Data_Updated_7.15.2021.xlsx")
#gwe = pd.read_excel(r"LBar_GWE_transcribed.xlsx")

#df = pd.concat([df0, gwe])

#select relevant columns for subsetted dataframe
df = df0[['StationName','SampleDate_D','LongName','Value']]

#convert Sample_Date_D columns to pd.to_datetime() objects
#df['SampleDate_D'], gwe['SampleDate_D'] = pd.to_datetime(df['SampleDate_D']), pd.to_datetime(gwe['SampleDate_D'])
df['SampleDate_D'] = pd.to_datetime(df['SampleDate_D'])

#subset dataframe for 'Original Data'
#df = df[df['QCSampleType'] == 'Original data']

#export updated dataframe to .csv in working directory
df.to_csv(r"LBar_semiannual_workingDataframe.csv", index=False)

os.mkdir("AppendixB_Figures")

#subset dataframes based on analyte for reporting
boron = df[df['LongName'] == 'Boron']
chloride = df[df['LongName'] == 'Chloride']
fluoride = df[df['LongName'] == 'Fluoride']
iron = df[df['LongName'] == 'Iron']
manganese = df[df['LongName'] == 'Manganese']
radium = df[df['LongName'] == 'Radium']
sulfate = df[df['LongName'] == 'Sulfate']
tds = df[df['LongName'] == 'Total Dissolved Solids']
uranium = df[df['LongName'] == 'Uranium']
uranium_below = uranium[uranium['StationName'].isin(['MW-1','MW-2', 'MW-5'])]
waterlevel = df[df['LongName'] == 'Groundwater Elevation']

#create a function to graph the individual dataframes
def grapher1(dataframe,analyte,y0,y1, limitvalue, text_y,y_axis_label,hline_text):
    fig = plt.figure(figsize=(8,6), dpi=600)         #resolution-dpi changed to '600'
    ax = fig.add_subplot(111)
    ax.axis([13845,19000,y0,y1])
    sns.lineplot(data=dataframe, x='SampleDate_D', y='Value',hue= 'StationName', style = 'StationName', ci=None, marker = 'o')
    ax.grid()
    limit = limitvalue
    ax.axhline(y=limit, color='red', linestyle='--', alpha=0.75)
    #ax.set_title("Time Series: " + analyte + "\n JJ No. 1/L-Bar Mine \n Stage1 Investigation Report", fontweight='bold')
    ax.set_ylabel(y_axis_label, weight='bold', fontsize=12)
    ax.set_xlabel("Date", weight='bold', fontsize=12)
    ax.text(13880,text_y, hline_text)
    locator = mdate.YearLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(DateFormatter('%b-%Y'))
    plt.xticks(rotation=45)
    ax.legend(['MW-1','MW-2','MW-3','MW-4','MW-5'],loc='best')
    plt.tight_layout()
    plt.savefig("AppendixB_Figures/LBar_" + analyte + "_AppB_Graph.png")
    
#Call grapher1() for each parameter-dataframe
grapher1(boron,"Boron",0,0.8,0.75, 0.76,"Boron, Dissolved (mg/L)",'0.75 - NMWQCC Standard')
grapher1(chloride,"Chloride",0,30,30,29,"Chloride (mg/L)","250 - NMWQCC Standard (not shown)")
grapher1(fluoride, "Fluoride",0.5,2.5,1.6,1.62, "Fluoride (mg/L)", "1.6 - NMWQCC Standard")
grapher1(iron, "Iron", 0, 0.5,0.5,0.48,"Iron, Dissolved (mg/L)","1.0 - NMWQCC Standard (not shown)" )
grapher1(manganese, "Manganese", 0,0.25, 0.20, 0.205,"Manganese, Dissolved (mg/L)","0.2 - NMWQCC Standard")
grapher1(sulfate, "Sulfate", 0,1200, 600, 625,'Sulfate (mg/L)', "600 - NMWQCC Standard")
grapher1(tds,"Total Dissolved Solids",400,2000,1000,1050,"Total Dissolved Solids (mg/L)", "1000 - NMWQCC Standard")
grapher1(uranium,"Uranium",0,0.8,0.03, 0.035, "Uranium, Dissolved (mg/L)", "0.03 - NMWQCC Standard")
grapher1(uranium_below,"Uranium (Wells Below Standard)",0,0.04, 0.03, 0.031, "Uranium, Dissolved (mg/L)", "0.03 - NMWQCC Standard")
grapher1(waterlevel, "Groundwater Elevation",5940, 5970,5970,5970,"Groundwater Elevation (ft AMSL)", " ")
grapher1(radium,"Radium-226 + Radium-228",0,14,14,13.6,"Ra-226 + Ra-228 (pCi/L)", "30 - NMWQCC Standard (not shown)" )
