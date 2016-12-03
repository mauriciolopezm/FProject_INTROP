import pandas as pd
import numpy  as np
import matplotlib.pyplot as plot
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as sm

#Read Crime data, SF
C_SF = pd.read_csv("Raw_SF_crime_2014.csv", index_col = 'Date', parse_dates = ['Date'])
C_SF.head(5)
# Data shows that for each date of year 2014, there are multiple entries of crimes, we want to group by dates count the total number of incidents and count only specific types of crime, mainly homicides and drug related incidents.
# Dropping variables that wont be used
del C_SF['DayOfWeek']
del C_SF['PdDistrict']
del C_SF['Resolution']
del C_SF['Address']
C_SF.head(5)
# Before merging we will create a df grouping by date and counting Inc Numb  (total crime incidents per day) and total count of homicides and drug related crimes (total specific type of incidents per day)
# Boolean columns on type of crimes:

# Boolean column homicides, we define "homicide" as the  subcategories of crimes labeled as assault that mention homicide in the description column
C_SF['H'] = ((C_SF['Descript'] == "ATTEMPTED HOMICIDE WITH A GUN") | (C_SF['Descript'] == "ATTEMPTED HOMICIDE WITH A KNIFE") | (C_SF['Descript'] == "ATTEMPTED HOMICIDE WITH BODILY FORCE") | (C_SF['Descript'] == "ATTEMPTED HOMICIDE WITH A DANGEROUS WEAPON"))
C_SF.H = C_SF.H.astype(int) # transforming bool to 1/0
C_SF[C_SF['H']==True].head(50)

#Boolean column on drug related crimes, we define drug related crimes as the category labeled "DRUG/NARCOTIC", this a broader pool of crimes than "homicides", we expect higher count per day across 2014
C_SF['D'] = (C_SF['Category'] == "DRUG/NARCOTIC")
C_SF.D = C_SF.D.astype(int) # transforming bool to 1/0
C_SF[C_SF['D']==True].head(50)
C_SF.head(50)
C_SF[(C_SF['D']==True) & (C_SF['H']==True)].head(50)
# this shows an empty df, this means H and D are mutually exclusive, no crime is labeled both as homicide and drug/related crime, this makes it difficult to know which homicides are related to drug related crime

# We can now drop category column
del C_SF['Category']

# Groupin by date(index) counting total crimes and specific type crimes, plotting each type of crime per day throughout 2014
#Total crimes per day
C_SF_TC= C_SF.groupby([C_SF.index])[['IncidntNum']].count()
priceplot2_1= C_SF_TC.plot(y = "IncidntNum", use_index=True)
priceplot2_1.set_ylabel("Total crimes per day")
priceplot2_1.set_xlabel("Month")
fig_2_1=plot.gcf()
fig_2_1.savefig('fig_2_1.png')
#Total homicides per day
C_SF_TH= C_SF.groupby([C_SF.index])[['H']].sum()
priceplot2_2= C_SF_TH.plot(y = "H", use_index=True)
priceplot2_2.set_ylabel("Total homicides per day")
priceplot2_2.set_xlabel("Month")
fig_2_2 =plot.gcf()
fig_2_2.savefig('fig_2_2.png')
# Total drug related crimes per day
C_SF_TD= C_SF.groupby([C_SF.index])[['D']].sum()
priceplot2_3= C_SF_TD.plot(y ="D", use_index=True)
priceplot2_3.set_ylabel("Total drug related crimes per day")
priceplot2_3.set_xlabel("Month")
fig_2_3 =plot.gcf()
fig_2_3.savefig('fig_2_3.png')


# Merging all counts for each crime type
C_SF_merge= C_SF_TC.join(C_SF_TH).join(C_SF_TD)
#C_SF_merge.sort_values(by =[C_SF.index])
C_SF_merge.head(50)
C_SF_merge.rename(columns = {'IncidntNum' : "Total crimes per day", "H" : "Total homicides per day", "D" : "Total drug related crimes per day" }, inplace = True)
# Rename columns
C_SF_merge.head(5)
C_SF_merge.to_csv('Final_SF_crime.csv', index=True)

# Plotting different  types of crime (frequency per day) throughout 2014
# Total crimes per day (all types)
C_SF_merge.plot()
plot.figure()
ax = C_SF_merge.plot(secondary_y=['Total homicides per day', 'Total drug related crimes per day'])
ax.set_ylabel('Total crimes per day')
ax.right_ax.set_ylabel('Homicides and drug relatd crimes per day')
fig_2_4 =plot.gcf()
fig_2_4.savefig('fig_2_4.png')
