import pandas as pd
import numpy  as np
import matplotlib.pyplot as plot
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as sm

#Weed DF CHI
MH_IL= pd.read_csv('Final_ILprices.csv', index_col='date')
MH_IL.head()
#Crime DF CHI
C_CHI_merge= pd.read_csv('Final_CHI_crime.csv', index_col='Number')
C_CHI_merge.head()

# Merge with IL weed prices
WPC_CHI_merge = MH_IL.join(C_CHI_merge)
WPC_CHI_merge.head()
WPC_CHI_merge.columns
WPC_CHI_merge.to_csv('CHI_WPC_final.csv', index=True) # This is our main data frame for CHI!!

# PLOTS AND REGRESSION ANALYSIS CHI
#Plots weed price vs types of crime
WPC_CHI_merge = MH_IL.join(C_CHI_merge)
WPC_CHI_merge_AUX1 = WPC_CHI_merge # AUX DF TO PLOT TOTAL CRIMES AND WEED PRICES THROUGHOUT 2014
del WPC_CHI_merge_AUX1['Total homicides per day']
del WPC_CHI_merge_AUX1['MedQN']
# actual plot
WPC_CHI_merge_AUX1.plot()
plot.figure()
ax = WPC_CHI_merge_AUX1.plot(secondary_y=['Total drug related crimes per day', 'Total crimes per day'])
ax.set_ylabel('Weed prices')
ax.right_ax.set_ylabel('Drug relatd crimes per day')
fig_3_0 =plot.gcf()
fig_3_0.savefig('fig_3_0_CHI.png')

WPC_CHI_merge = MH_IL.join(C_CHI_merge)
WPC_CHI_merge_AUX2 = WPC_CHI_merge # AUX DF TO PLOT TOTAL CRIMES AND WEED PRICES THROUGHOUT 2014
del WPC_CHI_merge_AUX2['Total crimes per day']
del WPC_CHI_merge_AUX2['Total homicides per day']
del WPC_CHI_merge_AUX2['MedQN']
# actual plot
WPC_CHI_merge_AUX2.plot()
plot.figure()
ax = WPC_CHI_merge_AUX2.plot(secondary_y=['Total drug related crimes per day'])
ax.set_ylabel('Weed prices')
ax.right_ax.set_ylabel('Total drug related crimes per day')
fig_3_01 =plot.gcf()
fig_3_01.savefig('fig_3_01_CHI.png')

WPC_CHI_merge = MH_IL.join(C_CHI_merge)
WPC_CHI_merge_AUX4 = WPC_CHI_merge # AUX DF TO PLOT TOTAL CRIMES AND WEED PRICES THROUGHOUT 2014
del WPC_CHI_merge_AUX4['Total crimes per day']
del WPC_CHI_merge_AUX4['Total drug related crimes per day']
del WPC_CHI_merge_AUX4['MedQN']
# actual plot
WPC_CHI_merge_AUX4.plot()
plot.figure()
ax = WPC_CHI_merge_AUX4.plot(secondary_y=['Total homicides per day'])
ax.set_ylabel('Weed prices')
ax.right_ax.set_ylabel('Total homicides per day')
fig_3_02 =plot.gcf()
fig_3_02.savefig('fig_3_02_CHI.png')

# Weedprice vs total crime per day
WPC_CHI_merge = MH_IL.join(C_CHI_merge)
fig, ax = plot.subplots()
sns.regplot(data = WPC_CHI_merge, x = "Total crimes per day", y = "Price of Medium Quality", ax = ax)
ax.set(xlabel='Total crimes per day', ylabel='Price of Medium Quality ($)')
fig_3_1 = plot.gcf()
fig_3_1.savefig('fig_3_1_CHI.png')
# Weedprice vs drug related crime per day
fig, ax = plot.subplots()
sns.regplot(data = WPC_CHI_merge, x = "Total drug related crimes per day", y = "Price of Medium Quality", ax = ax)
ax.set(xlabel='Total drug related crimes per day', ylabel='Price of Medium Quality ($)')
fig_3_2 = plot.gcf()
fig_3_2.savefig('fig_3_2_CHI.png')
# Weedprice vs homicide crimes per day
fig, ax = plot.subplots()
sns.regplot(data = WPC_CHI_merge, x = "Total homicides per day", y = "Price of Medium Quality", ax = ax)
ax.set(xlabel='Total homicides per day', ylabel='Price of Medium Quality ($)')
fig_3_3 = plot.gcf()
fig_3_3.savefig('fig_3_3_CHI.png')

#OLS REGRESSION ANALYSIS, remember here we are using our main df, WPC_CHI_merge

WPC_CHI_reg= WPC_CHI_merge
WPC_CHI_reg.rename(columns = {"Price of Medium Quality" : "PMedQ", "Total homicides per day" : "TH", "Total drug related crimes per day" : "TDC", "Total crimes per day" : "TC"  }, inplace = True)
#Weedprice vs total crime per day
model = sm.ols(formula = 'TC ~ PMedQ', data = WPC_CHI_reg).fit()
model.summary()
#Weedprice vs total drug related crime per day
model = sm.ols(formula = 'TDC ~ PMedQ', data = WPC_CHI_reg).fit()
model.summary()
#Weedprice vs total drug homicides per day
model = sm.ols(formula = 'TH ~ PMedQ', data = WPC_CHI_reg).fit()
model.summary()
