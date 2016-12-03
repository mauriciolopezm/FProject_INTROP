import pandas as pd
import numpy  as np # for those extra mathematical functions.
import matplotlib as plot

# opening up the file which has all the states and different years and parsing the date
weedprices_df = pd.read_csv("weedprices.csv", parse_dates = ['date'])
weedprices_df.head(2)
#only getting the california state prices
california = weedprices_df[weedprices_df.State=="California"]
#grouping by dates to see if there are any repeated dates or not - checked this through checking unique values also
california.groupby(['date']).size()
# parsing out the year column seperately so that it can be used as a filter
california['year'] = pd.DatetimeIndex(california_df['date']).year
#getting only values for 2014 year for the california data set
california_df = california[(california["year"] == 2014) & (california["State"] == "California")]
california_df.count() # checking the data.
# dropping the index column
california_df.drop(california_df.columns[[0]], axis=1)
california_df.count()
# output the dataframe into csv
california_df.to_csv('California_wprices_2014.csv', index=False)
