# Used Car Data Scraping and Analysis

## Overview

This project involves scraping data from Cars.com using a Python script (`carsDotComScrape.py`), cleaning the scraped data using another Python script (`carsFileCleaning.py`), and visualizing the cleaned data using a Jupyter Notebook (`carsVis.ipynb`). Additionally, it includes the creation and evaluation of machine learning models to predict car prices based on various features.

## Files

1. **carsDotComScrape.py**: This script extracts information from Cars.com listings based on specified filters such as make, model, year range, and location. It uses the BeautifulSoup library to parse HTML content, extracts vehicle details like title, mileage, price, and deal information, and stores the data in CSV format (`output_DATE.csv`).

2. **carsFileCleaning.py**: After scraping the data, this script cleans the CSV file by removing rows with missing or irrelevant information, extracting year, make, and model details from the title, formatting numerical data like miles and price, and storing the cleaned data in a new CSV file (`output_DATE_cleaned.csv`).

3. **carsVis.ipynb**: This Jupyter Notebook loads the cleaned data from `output_DATE_cleaned.csv`, performs data visualization using matplotlib and seaborn libraries, including scatter plots with regression lines, joint plots with regression analysis, and linear regression models to analyze the relationship between mileage and price. It also includes polynomial regression analysis.

4. **output_DATE.csv**: The raw data scraped from Cars.com listings before cleaning.

5. **output_DATE_cleaned.csv**: The cleaned and formatted data ready for analysis and visualization.

## Usage

1. **Scraping Data**:
   - Edit `carsDotComScrape.py` to modify the URL with desired filters.
   - Run `carsDotComScrape.py` to extract data and store it in `output_DATE.csv`.

2. **Cleaning Data**:
   - Run `carsFileCleaning.py` to clean the scraped data and store it in `output_DATE_cleaned.csv`.

3. **Visualizing Data**:
   - Open and run `carsVis.ipynb` in a Jupyter Notebook environment to visualize the cleaned data and perform analysis.

4. **Modeling**:
   - The Jupyter Notebook (`carsVis.ipynb`) includes machine learning models like Linear Regression, Ridge Regression, and Random Forest Regression to predict car prices based on features like mileage, year, stock status, and sub-model.

## Dependencies

- Python 3.x
- pandas
- requests
- BeautifulSoup (bs4)
- matplotlib
- seaborn
- scikit-learn

