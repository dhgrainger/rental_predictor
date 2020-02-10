# Import libraries
import pandas as pd
import numpy as np
import datetime

# Import listings csv
data = pd.read_csv('listings.csv')

# Drop uneeded columns
data = data.drop(['host_name','neighbourhood_group'], axis=1)

# Make object variables categorical
cols = ['neighbourhood','room_type']
for col in cols:
    data[col] = data[col].astype('category')

# Change last review to date type
data.last_review = pd.to_datetime(data.last_review)

# Make a column to know what day the data was downloaded - probably a better way to track this
data['date_of_data_download'] = datetime.date.today()
data.date_of_data_download = pd.to_datetime(data.date_of_data_download)

# Make a column to track days since last review
data['days_since_last_review'] = data.date_of_data_download - data.last_review

# Export cleaned dataframe to csv
data.to_csv('listings_cleaned.csv',index=False)
