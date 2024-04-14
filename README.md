# A Sales Performance Analysis on Adidas using SQL

## Project Overview 

This project focuses on analysing the Adidas sales database to identify key insights to help improve sales performance and operational efficiency. 
The dataset was acquired from Kaggle 'https://www.kaggle.com/datasets/vishwas199728/adidas-sales-data' and was then cleaned using Juypter Notebook followed by analysis through SQL queries using pgAdmin4. Finally, some visualisations were created using matplotlib.pyplot on python to visualise the SQL queries.

## Contents

`Cleaned_Adidas_Sales_Data.ipynb`: cleaned python file.

`Adidas_Sales_Data.sql`: SQL queries file.

`Adidas_Sales_Data.csv` The raw CSV file containing the database acquired from Kaggle.

`Visualisations_Adidas_Sales_Data.py`: python visualising file showcasing a range of different plot types using `matplotlib.pyplot`.

## Dataset Cleaning

The `Adidas_Sales_Data.csv` was cleaned as mentioned using Python through Juypter Notebook. Below is the step-by-step cleaning process:

- The file was imported to Juypter using pandas.
- I renamed the columns to remove space and make words more concise.
- Checked for duplicates but none were found.
- Removed/made sure there were no 0 or negative values in the TotalSales column.
- Capped values at the 99th percentile to remove any computational errors while still providing a fair assessment of the database.

## SQL Setup

A database `Adidas_Sales_Data` was created on pgAdmin 4 to conduct the SQL queries.

## SQL Table

Below is the code for the SQL Table `Sales`

```
CREATE SEQUENCE sales_id_seq START WITH 1;

CREATE TABLE Sales (
    SalesID INT PRIMARY KEY DEFAULT nextval('sales_id_seq'),
    Retailer VARCHAR(255),
    RetailerID INT,
    InvoiceDate DATE,
    Region VARCHAR(255),
    StateName VARCHAR(255),
    City VARCHAR(255),
    GenderType VARCHAR(50),
    ProductCategory VARCHAR(255),
    PricePerUnit NUMERIC,
    UnitsSold INT,
    TotalSales NUMERIC,
    OperatingProfit NUMERIC,
    OperatingMargin NUMERIC,
    SalesMethod VARCHAR(100)
);
```

I created a sequence `sales_id_seq` in order to import the data from the CSV file after creating a new column 'SalesID' to include a 'PRIMARY KEY'.

## Data Engineering for Visualisations

- Converted `InvoiceDate` to datetime to facilitate time-based aggregation.
- Aggregated total sales over time by month.
- Calculated total sales by product category.
- Aggregated total sales by region.
- Different types of plots are used such as line chart, pie chart, and bar chart.

## How to Use

Before running the scripts, make sure you have the following installed:
- Python 3
- pandas library for Python
- PostgreSQL
- pgAdmin 4 or another SQL client that can run SQL scripts
- matplotlib.pyplot for Python

Clone or download the files and run the scripts on their respective programs.

## Queries

Conducted queries to find generic information about the sales data such as Total Sales, Total Profit, and Average Price Per Unit.

Other analyses included Sale Trends Over Time, Top Performing Regions, Sales Performance by Retailers, Profitability Analysis etc.

## Findings

These queries provide beneficial information for Adidas stakeholders looking to see how sales in the company are performing. With these queries, the Top-Selling Product Category has been identified, the Top-Selling Region, and the Top-Selling Retailer. More descriptive information such as Product Profitability, Sale Trends, and Gender Preferences are detailed too, aiding Adidas in future decisions
