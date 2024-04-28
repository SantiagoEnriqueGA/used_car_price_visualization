
import pandas as pd

# Define the path to the CSV file containing the car data
path = 'carsDotCom/output_Apr-27-2024'

# Read the data from the CSV file into a pandas DataFrame named 'cars'
# Specify column names as "Title", "Miles", "Price", and "Deal"
cars = pd.read_csv(path+'.csv',  
                   names=["Title", "Miles", "Price", "Deal"])

# Drop if no title
cars = cars.dropna(subset=['Title'])

# Extract the year, make, and model information from the 'Title' column
cars['Year']=cars['Title'].str.split(' ').str[0]
cars['Make']=cars['Title'].str.split(' ').str[1]
cars['Model']=cars['Title'].str.split(' ').str[2:].str.join(" ")

# Remove the last 4 characters from the 'Miles' column to remove ' miles'
cars['Miles']=cars['Miles'].str[:-4]

# Replace "Not Priced" with 0, remove the dollar sign from 'Price'
cars['Price']=cars['Price'].replace("Not Priced",0)
cars['Price']=cars['Price'].str[1:]

# Extract only the first two words from the 'Deal' column
cars['Deal']=cars['Deal'].replace('"', '')
cars['Deal']=cars['Deal'].str.split(' ').str[:2].str.join(" ")


# Convert 'Year' to integer type, remove commas from 'Price' and 'Miles'
cars['Year'] = cars['Year'].fillna(0).astype(int)

# Remove commas from 'Price' and 'Miles' and convert to integer
cars['Price']=cars['Price'].str.replace(',', '')
cars['Miles']=cars['Miles'].str.replace(',', '')

# Drop rows with NaN values in 'Price', fill NaN values in 'Miles' with 0, and convert to integer
cars = cars.dropna(subset=['Price'])
cars['Price']=cars['Price'].astype(int)
cars['Miles']=cars['Miles'].fillna(0).astype(int)

# Write the cleaned data back to a new CSV file with 'cleaned' appended to the original file name
cars.to_csv(path+'_cleaned.csv', mode='a', index=False, header=True)


