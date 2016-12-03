import pandas as pd
import numpy  as np
import matplotlib.pyplot as plot
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as sm

# Read Marihuana, CAL
MH_IL = pd.read_csv("IL_wprices_2014.csv", index_col = 'date', parse_dates =['date'])
#See scrappginng and cleaning code of how we got to these Dataset
MH_IL.rename(columns = {"MedQ" : "Price of Medium Quality"}, inplace = True)
del MH_IL['State']
del MH_IL['HighQ']
del MH_IL['HighQN']
del MH_IL['LowQ']
del MH_IL['LowQN']
# Rename columns
MH_IL.head(5)
# Plot trend of MH Prices througout 2014, (plot.0)
priceplot1= MH_IL.plot(y = "Price of Medium Quality", use_index=True)
priceplot1.set_ylabel("Daily Price of Medium Quality Marijuana")
priceplot1.set_xlabel("Month")
fig_0 =plot.gcf()
fig_0.savefig('fig_0.png')

MH_IL.to_csv('Final_ILprices.csv', index=True)
