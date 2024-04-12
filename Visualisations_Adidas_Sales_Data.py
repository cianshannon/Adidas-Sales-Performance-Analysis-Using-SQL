#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

inpPath = r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Cleaned_Adidas_Sales_Data.csv"
inpDf = pd.read_csv(r"C:\Users\ciana\OneDrive\Documents\DCU\Final Year\MT412 - Professional Business Analytics\Cleaned_Adidas_Sales_Data.csv")


# In[3]:


# Convert 'InvoiceDate' to datetime to facilitate time-based aggregation
inpDf['InvoiceDate'] = pd.to_datetime(inpDf['InvoiceDate'])


# In[5]:


# Aggregate total sales over time by month
monthly_sales = inpDf.groupby(inpDf['InvoiceDate'].dt.to_period('M'))['TotalSales'].sum()


# In[7]:


# Calculate total sales by product category
sales_by_category = inpDf.groupby('ProductCategory')['TotalSales'].sum()


# In[9]:


# Aggregate total sales by region
sales_by_region = inpDf.groupby('Region')['TotalSales'].sum()


# In[10]:


# Plot Size 
plt.figure(figsize=(15, 10))


# In[11]:


# Plot 1: Total Sales Over Time (Line Chart)
plt.subplot(2, 2, 1)
monthly_sales.plot(kind='line', marker='o', color='b', title='Total Sales Over Time')
plt.ylabel('Total Sales ($)')
plt.xlabel('Month')


# In[12]:


# Plot 2: Total Sales by Product Category (Pie Chart)
plt.subplot(2, 2, 2)
sales_by_category.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Sales by Product Category')
plt.ylabel('') 


# In[13]:


# Plot 3: Sales Trends Over Time (Line Chart)
plt.subplot(2, 2, 3)
monthly_sales.plot(kind='line', marker='x', color='g', title='Sales Trends Over Time')
plt.ylabel('Sales ($)')
plt.xlabel('Month')


# In[14]:


# Plot 4: Total Sales by Region (Bar Chart)
plt.subplot(2, 2, 4)
sales_by_region.plot(kind='bar', color='orange', title='Total Sales by Region')
plt.ylabel('Total Sales ($)')
plt.xlabel('Region')


# In[ ]:




