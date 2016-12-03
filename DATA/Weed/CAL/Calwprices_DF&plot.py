import pandas as pd
import numpy  as np
import matplotlib.pyplot as plot
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as sm

MH_Cal = pd.read_csv("California_wprices_2014.csv", index_col = 'Date', parse_dates =['Date'])
#See scrappginng and cleaning code of how we got to these Dataset
MH_Cal.rename(columns = {"MedQ" : "Price of Medium Quality"}, inplace = True)
del MH_Cal['State']
del MH_Cal['HighQ']
del MH_Cal['HighQN']
del MH_Cal['LowQ']
del MH_Cal['LowQN']
# Rename columns
MH_Cal.head(5)
# Plot trend of MH Prices througout 2014, (plot.0)
priceplot1= MH_Cal.plot(y = "Price of Medium Quality", use_index=True)
priceplot1.set_ylabel("Daily Price of Medium Quality Marijuana")
priceplot1.set_xlabel("Month")
fig_0 =plot.gcf()
fig_0.savefig('fig_0.png')

MH_Cal.to_csv('Final_Californiaprices.csv', index=True)
