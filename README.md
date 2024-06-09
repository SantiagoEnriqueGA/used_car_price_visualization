# Used Car Data Scraping and Analysis

## Overview

This project involves scraping data from Cars.com using Python scripts and analyzing the data for insights. The main scripts are `carsDotComScrape.py` for scraping data related to the Lexus GX 460 model and `carsFileCleaning.py` for cleaning the scraped data. Additionally, data visualization and machine learning modeling are performed in a Jupyter Notebook (`GX460_Vis.ipynb`).

## Files

1. **carsDotComScrape.py.py**:
   - This script contains the `CarsDotComScraper` class, which is responsible for scraping data from Cars.com listings for a given search. It uses BeautifulSoup and requests libraries to parse HTML content, extract vehicle details, and store the data in CSV format (`output_DATE.csv`).

2. **carsFileCleaning.py**:
   - This script contains the `CarsDotComCleaner` class, which cleans the scraped data from Cars.com. It reads the data from a CSV file, performs cleaning operations such as removing rows with missing or irrelevant information, extracting year, make, and model details, formatting numerical data, and saving the cleaned data in a new CSV file (`output_DATE_cleaned.csv`).

3. **GX460_scrape.py**:
   - This script calls the carsDotComScrape and carsFileCleaning from the above files. It scrapes and cleans data for all new and used GX460s on Cars.com

4. **carsVis.ipynb**:
   - This Jupyter Notebook loads the cleaned data from `output_DATE_cleaned.csv` and performs data visualization using matplotlib and seaborn libraries. It includes scatter plots with regression lines, joint plots with regression analysis, and machine learning models like Linear Regression, Ridge Regression, and Random Forest Regression to predict car prices based on various features.

5. **output_DATE.csv**:
   - This file contains the raw data scraped from Cars.com listings before cleaning.

6. **output_DATE_cleaned.csv**:
   - This file contains the cleaned and formatted data ready for analysis and visualization.

## Usage

1. **Scraping and Cleaning Data**:
   - Edit `GX460_scrape.py` to modify the URL with desired filters for scraping data related to the Lexus GX 460 model.
   - Run `GX460_scrape.py` to extract data and store it in `output_DATE.csv`.

2. **Visualizing Data**:
   - Open and run `GX460_Vis.ipynb` in a Jupyter Notebook environment to visualize the cleaned data and perform analysis.

## Example Plots
**See carsVis.ipynb for more**

![alt text](https://raw.githubusercontent.com/SantiagoEnriqueGA/used_car_price_visualization/main/carsDotCom/plots/Violin%20and%20Box%20plots%20for%20'Year'%20vs%20'Price'.png)


![alt text](https://raw.githubusercontent.com/SantiagoEnriqueGA/used_car_price_visualization/main/carsDotCom/plots/Car%20Price%20vs%20Miles%20Driven%20(Color%20Coded%20by%20Year).png)


![alt text](https://raw.githubusercontent.com/SantiagoEnriqueGA/used_car_price_visualization/main/carsDotCom/plots/Polynomial%20Car%20Price%20vs%20Miles%20Driven.png)


## Dependencies

- Python 3.x
- pandas
- requests
- BeautifulSoup (bs4)
- matplotlib
- seaborn
- scikit-learn
