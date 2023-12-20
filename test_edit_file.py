# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:01:28 2023

@author: storm
"""

import pandas as pd

dataset = pd.read_csv("data/bolig02.csv")

# Assuming your DataFrame is named dataset and the date column is named "date"
dataset['date'] = pd.to_datetime(dataset['date'], format='%Y-%m-%d %H:%M:%S')

# Extracting year, month, day, hour, and minute into separate columns
dataset['year'] = dataset['date'].dt.year
dataset['month'] = dataset['date'].dt.month
dataset['day'] = dataset['date'].dt.day
dataset['hour'] = dataset['date'].dt.hour
dataset['minute'] = dataset['date'].dt.minute


dataset = dataset[['year', 'month','day','hour','minute','temperature','humidity']]































# Optionally, you can drop the original "date" column if you don't need it anymore
# dataset = dataset.drop('date', axis=1)

# Display the resulting DataFrame

# dataset = pd.read_csv("data/bolig02.csv")

# # Assuming your DataFrame is named dataset and the date column is named "date"
# dataset['date'] = pd.to_datetime(dataset['date'], format='%Y-%m-%d %H:%M:%S')

# # Extracting year, month, day, hour, and minute into separate columns
# year = dataset['date'].dt.year
# month = dataset['date'].dt.month
# day = dataset['date'].dt.day
# hour = dataset['date'].dt.hour
# minute = dataset['date'].dt.minute

# temperature = dataset['temperature']
# humidity = dataset['humidity']

# #dataset = dataset[['year', 'month','day','hour','minute','temperature','humidity']]