import pandas as pd
import numpy  as np
import matplotlib.pyplot as plot
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as sm

# Chicago crime data
#Read Crime data, CHI
C_CHI = pd.read_csv("CHI_Crime_2014.csv", index_col = 'Number', parse_dates = ['Number'])
C_CHI.head(5)
C_CHI.columns
C_CHI.rename(columns = {"Case" : "IncidntNum", "Type" : "Descript"}, inplace = True)

# Data shows that for each date of year 2014, there are multiple entries of crimes, we want to group by dates count the total number of incidents and count only specific types of crime, mainly homicides and drug related incidents.
# Before merging we will create a df grouping by date and counting Inc Numb  (total crime incidents per day) and total count of homicides and drug related crimes (total specific type of incidents per day)
# Boolean columns on type of crimes:
# Boolean column homicides, we define "homicide" as the  subcategories of crimes labeled as assault that mention homicide in the description column
C_CHI['H'] = ((C_CHI['Descript'] == "HOMICIDE"))
C_CHI.H = C_CHI.H.astype(int) # transforming bool to 1/0

#Boolean column on drug related crimes, we define drug related crimes as the category labeled "DRUG/NARCOTIC", this a broader pool of crimes than "homicides", we expect higher count per day across 2014
C_CHI['D'] = (C_CHI['Descript'] == "NARCOTICS")
C_CHI.D = C_CHI.D.astype(int) # transforming bool to 1/0
C_CHI.head(50)

# We can now drop category column
del C_CHI['Descript']

# Groupin by date(index) counting total crimes and specific type crimes, plotting each type of crime per day throughout 2014
#Total crimes per day
C_CHI_TC= C_CHI.groupby([C_CHI.index])[['IncidntNum']].count()
priceplot2_1= C_CHI_TC.plot(y = "IncidntNum", use_index=True)
priceplot2_1.set_ylabel("Total crimes per day")
priceplot2_1.set_xlabel("Month")
fig_2_1=plot.gcf()
fig_2_1.savefig('fig_2_1_CHI.png')
#Total homicides per day
C_CHI_TH= C_CHI.groupby([C_CHI.index])[['H']].sum()
priceplot2_2= C_CHI_TH.plot(y = "H", use_index=True)
priceplot2_2.set_ylabel("Total homicides per day")
priceplot2_2.set_xlabel("Month")
fig_2_2 =plot.gcf()
fig_2_2.savefig('fig_2_2_CHI.png')
# Total drug related crimes per day
C_CHI_TD= C_CHI.groupby([C_CHI.index])[['D']].sum()
priceplot2_3= C_CHI_TD.plot(y ="D", use_index=True)
priceplot2_3.set_ylabel("Total drug related crimes per day")
priceplot2_3.set_xlabel("Month")
fig_2_3 =plot.gcf()
fig_2_3.savefig('fig_2_3_CHI.png')

# Merging all counts for each crime type
C_CHI_merge= C_CHI_TC.join(C_CHI_TH).join(C_CHI_TD)
C_CHI_merge.head(50)
C_CHI_merge.rename(columns = {"IncidntNum" : "Total crimes per day", "H" : "Total homicides per day", "D" : "Total drug related crimes per day" }, inplace = True)
# Rename columns and save to file
C_CHI_merge.to_csv('Final_CHI_crime.csv', index=True)

#This is the final merge for Chicago crime
# Plotting different  types of crime (frequency per day) throughout 2014
# Total crimes per day (all types)
C_CHI_merge.plot()
plot.figure()
ax = C_CHI_merge.plot(secondary_y=['Total homicides per day', 'Total drug related crimes per day'])
ax.set_ylabel('Total crimes per day')
ax.right_ax.set_ylabel('Homicides and drug relatd crimes per day')
fig_2_4 =plot.gcf()
fig_2_4.savefig('fig_2_4_CHI.png')
