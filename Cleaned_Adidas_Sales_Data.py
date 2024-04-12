#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Data Cleaning Documentation for Adidas Sales Data

## Introduction
#This Jupyter Notebook documents the data cleaning process for the Adidas Sales Data used in a Sales Performance Analysis. The aim is to prepare the data for analysis, ensuring it is clean and formatted correctly.


# In[2]:


import pandas as pd

inpPath = r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Adidas_Sales_Data.csv"
inpDf = pd.read_csv(r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Adidas_Sales_Data.csv")



# In[3]:


#Display the first few rows of the dataset and summary information
inpDf.info()
inpDf.describe()


# In[4]:


## Data Cleaning ##


# In[5]:


### Rename Columns

# Rename columns to remove spaces and make names more concise
inpDf.columns = ['Retailer', 'RetailerID', 'InvoiceDate', 'Region', 'StateName', 'City',
                'GenderType', 'ProductCategory', 'PricePerUnit', 'UnitsSold',
                'TotalSales', 'OperatingProfit', 'OperatingMargin', 'SalesMethod']


# In[6]:


### Check for Duplicates ###


# In[7]:


# Check for duplicates
duplicate_rows = inpDf.duplicated().sum()
duplicate_rows


# In[8]:


### Handle Zero Sales ###


# In[9]:


# Assuming zero sales are valid, no action is needed; otherwise, we could filter them out

inpDf = inpDf[inpDf['TotalSales'] > 0]


# In[10]:


### Analyse and Treat Outliers ###

price_99th = inpDf['PricePerUnit'].quantile(0.99)
sales_99th = inpDf['TotalSales'].quantile(0.99)


# In[11]:


inpDf['PricePerUnit'] = inpDf['PricePerUnit'].clip(upper=price_99th)
inpDf['TotalSales'] = inpDf['TotalSales'].clip(upper=sales_99th)

#The primary reason why I capped values at the 99th percentile is to reduce the impact of extreme values that can skew the analysis. These extreme values might be due to data entry errors, unusual transactions, or other anomalies.


# In[12]:


# Display the cleaned data structure
inpDf.info()
inpDf.describe()


# In[13]:


# Only four entries were removed after the cleaning process.


# In[14]:


## Exporting the Cleaned Data ##

# Define the output path for the cleaned CSV file
outPath = r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Cleaned_Adidas_Sales_Data.csv"

# Export the cleaned DataFrame to a CSV file
inpDf.to_csv(outPath, index=False)


# In[ ]:




