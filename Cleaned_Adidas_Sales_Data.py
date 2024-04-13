#!/usr/bin/env python
# coding: utf-8

# Data Cleaning Documentation for Adidas Sales Data

## Introduction
#This Jupyter Notebook documents the data cleaning process for the Adidas Sales Data used in a Sales Performance Analysis. The aim is to prepare the data for analysis, ensuring it is clean and formatted correctly.

import pandas as pd

inpPath = r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Adidas_Sales_Data.csv"
inpDf = pd.read_csv(r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Adidas_Sales_Data.csv")

#Display the first few rows of the dataset and summary information
inpDf.info()
inpDf.describe()

## Data Cleaning ##

### Rename Columns

# Rename columns to remove spaces and make names more concise
inpDf.columns = ['Retailer', 'RetailerID', 'InvoiceDate', 'Region', 'StateName', 'City',
                'GenderType', 'ProductCategory', 'PricePerUnit', 'UnitsSold',
                'TotalSales', 'OperatingProfit', 'OperatingMargin', 'SalesMethod']

### Check for Duplicates ###

# Check for duplicates
duplicate_rows = inpDf.duplicated().sum()
duplicate_rows

### Handle Zero Sales ###

# Assuming zero sales are valid, no action is needed; otherwise, we could filter them out

inpDf = inpDf[inpDf['TotalSales'] > 0]

### Analyse and Treat Outliers ###

price_99th = inpDf['PricePerUnit'].quantile(0.99)
sales_99th = inpDf['TotalSales'].quantile(0.99)

inpDf['PricePerUnit'] = inpDf['PricePerUnit'].clip(upper=price_99th)
inpDf['TotalSales'] = inpDf['TotalSales'].clip(upper=sales_99th)

#The primary reason why I capped values at the 99th percentile is to reduce the impact of extreme values that can skew the analysis. These extreme values might be due to data entry errors, unusual transactions, or other anomalies.

# Display the cleaned data structure
inpDf.info()
inpDf.describe()

# Only four entries were removed after the cleaning process.

## Exporting the Cleaned Data ##

# Define the output path for the cleaned CSV file
outPath = r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Cleaned_Adidas_Sales_Data.csv"

# Export the cleaned DataFrame to a CSV file
inpDf.to_csv(outPath, index=False)





