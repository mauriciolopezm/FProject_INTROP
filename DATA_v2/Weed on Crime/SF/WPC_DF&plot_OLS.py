import pandas as pd
import numpy  as np
import matplotlib.pyplot as plot
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as sm

#Weed DF SF
MH_CAL= pd.read_csv('Final_Californiaprices.csv', index_col='Date')
MH_CAL.head()
#Crime DF SF
C_SF_merge= pd.read_csv('Final_SF_crime.csv', index_col='date')
C_SF_merge.head()

# Merge with California weed prices
WPC_SF_merge = MH_Cal.join(C_SF_merge)
WPC_SF_merge.head()
WPC_SF_merge.columns
WPC_SF_merge.to_csv('SF_WPC_final.csv', index=True) # This is our main data frame for SF!!

# PLOTS AND REGRESSION ANALYSIS SF
#Plots weed price vs types of crime
WPC_SF_merge = MH_Cal.join(C_SF_merge)
WPC_SF_merge_AUX1 = WPC_SF_merge # AUX DF TO PLOT TOTAL CRIMES AND WEED PRICES THROUGHOUT 2014
del WPC_SF_merge_AUX1['Total homicides per day']
del WPC_SF_merge_AUX1['MedQN']
# actual plot
WPC_SF_merge_AUX1.plot()
plot.figure()
ax = WPC_SF_merge_AUX1.plot(secondary_y=['Total drug related crimes per day', 'Total crimes per day'])
ax.set_ylabel('Weed prices')
ax.right_ax.set_ylabel('Drug relatd crimes per day')
fig_3_0 =plot.gcf()
fig_3_0.savefig('fig_3_0.png')

WPC_SF_merge = MH_Cal.join(C_SF_merge)
WPC_SF_merge_AUX2 = WPC_SF_merge # AUX DF TO PLOT TOTAL CRIMES AND WEED PRICES THROUGHOUT 2014
del WPC_SF_merge_AUX2['Total crimes per day']
del WPC_SF_merge_AUX2['Total homicides per day']
del WPC_SF_merge_AUX2['MedQN']
# actual plot
WPC_SF_merge_AUX2.plot()
plot.figure()
ax = WPC_SF_merge_AUX2.plot(secondary_y=['Total drug related crimes per day'])
ax.set_ylabel('Weed prices')
ax.right_ax.set_ylabel('Total drug related crimes per day')
fig_3_01 =plot.gcf()
fig_3_01.savefig('fig_3_01.png')

WPC_SF_merge = MH_Cal.join(C_SF_merge)
WPC_SF_merge_AUX4 = WPC_SF_merge # AUX DF TO PLOT TOTAL CRIMES AND WEED PRICES THROUGHOUT 2014
del WPC_SF_merge_AUX4['Total crimes per day']
del WPC_SF_merge_AUX4['Total drug related crimes per day']
del WPC_SF_merge_AUX4['MedQN']
# actual plot
WPC_SF_merge_AUX4.plot()
plot.figure()
ax = WPC_SF_merge_AUX4.plot(secondary_y=['Total homicides per day'])
ax.set_ylabel('Weed prices')
ax.right_ax.set_ylabel('Total homicides per day')
fig_3_02 =plot.gcf()
fig_3_02.savefig('fig_3_02.png')

# Weedprice vs total crime per day
WPC_SF_merge = MH_Cal.join(C_SF_merge)
fig, ax = plot.subplots()
sns.regplot(data = WPC_SF_merge, x = "Total crimes per day", y = "Price of Medium Quality", ax = ax)
ax.set(xlabel='Total crimes per day', ylabel='Price of Medium Quality ($)')
fig_3_1 = plot.gcf()
fig_3_1.savefig('fig_3_1.png')
# Weedprice vs drug related crime per day
fig, ax = plot.subplots()
sns.regplot(data = WPC_SF_merge, x = "Total drug related crimes per day", y = "Price of Medium Quality", ax = ax)
ax.set(xlabel='Total drug related crimes per day', ylabel='Price of Medium Quality ($)')
fig_3_2 = plot.gcf()
fig_3_2.savefig('fig_3_2.png')
# Weedprice vs homicide crimes per day
fig, ax = plot.subplots()
sns.regplot(data = WPC_SF_merge, x = "Total homicides per day", y = "Price of Medium Quality", ax = ax)
ax.set(xlabel='Total homicides per day', ylabel='Price of Medium Quality ($)')
fig_3_3 = plot.gcf()
fig_3_3.savefig('fig_3_3.png')

#OLS REGRESSION ANALYSIS, remember here we are using our main df, WPC_SF_merge
WPC_SF_reg= WPC_SF_merge
WPC_SF_reg.rename(columns = {"Price of Medium Quality" : "PMedQ", "Total homicides per day" : "TH", "Total drug related crimes per day" : "TDC", "Total crimes per day" : "TC"  }, inplace = True)
#Weedprice vs total crime per day
model = sm.ols(formula = 'TC ~ PMedQ', data = WPC_SF_reg).fit()
model.summary()
#Weedprice vs total drug related crime per day
model = sm.ols(formula = 'TDC ~ PMedQ', data = WPC_SF_reg).fit()
model.summary()
#Weedprice vs total drug homicides per day
model = sm.ols(formula = 'TH ~ PMedQ', data = WPC_SF_reg).fit()
model.summary()
