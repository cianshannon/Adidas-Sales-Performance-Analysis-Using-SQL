Create Database Adidas_Sales_Data

/* Create a sequence to implement SalesId into the table as a PRIMARY KEY. This will start at 1 and continue down all the rows of the dataset*/
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

COPY Sales(Retailer, RetailerID, InvoiceDate, Region, StateName, City, GenderType, ProductCategory, PricePerUnit, UnitsSold, TotalSales, OperatingProfit, OperatingMargin, SalesMethod)
FROM 'C:\\Users\\Public\\Public Doc4SQL\\Cleaned_Adidas_Sales_Data.csv'
DELIMITER ','
CSV HEADER;

-- SQL Queries --

/* 1. Calculate Total Sales */
SELECT SUM(TotalSales) AS Total_Sales FROM Sales;

/* 2. Calculate Total Profit */
SELECT SUM(OperatingProfit) AS Total_Profit FROM Sales;

/* 3. Calculate Average Price per Unit */
SELECT AVG(PricePerUnit) AS Average_Price_Per_Unit FROM Sales;

/* 4. Calculate Total Units Sold */
SELECT SUM(UnitsSold) AS Total_Units_Sold FROM Sales;

/* 5. Total Sales by Product Category */
SELECT ProductCategory, SUM(TotalSales) AS Total_Sales
FROM Sales
GROUP BY ProductCategory
ORDER BY Total_Sales DESC;
/* This query looks to see which product category has the most sales. In this case, Street Footwear has the most sales. */

/* 6. Sale Trends Over Time */
SELECT DATE_TRUNC('month', InvoiceDate) AS Month, SUM(TotalSales) AS Total_Sales
FROM Sales
GROUP BY Month
ORDER BY Month;
/* This query looks at the total sales of each month */

/* 7. Top Performing Region */
SELECT Region, SUM(TotalSales) AS Total_Sales
FROM Sales
GROUP BY Region
ORDER BY Total_Sales DESC;
/* Utilising this query we can see which region had the most sales. The query show that the West had the most sales. */

/* 8. Sales Performance by Retailer */
SELECT Retailer, SUM(TotalSales) AS Total_Sales
FROM Sales
GROUP BY Retailer
ORDER BY Total_Sales DESC;
/* This query looks to identify which retailer sees the most sales. West Gear has the most sales. */

/* 9. Profitability Analysis */
SELECT ProductCategory, AVG(OperatingMargin) AS Avg_Operating_Margin
FROM Sales
GROUP BY ProductCategory
ORDER BY Avg_Operating_Margin DESC;
/* A profitability Analysis query seeks to see the profitability margins of each product category. Street Footwear is the most profitable product category. */

/* 10. Units Sold by Product Category and Gender Type */
SELECT ProductCategory, GenderType, SUM(UnitsSold) AS Total_Units_Sold
FROM Sales
GROUP BY ProductCategory, GenderType
ORDER BY ProductCategory, GenderType;
