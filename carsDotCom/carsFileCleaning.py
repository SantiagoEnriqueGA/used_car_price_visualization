import pandas as pd

class CarsDotComCleaner:
    """A class for cleaning data extracted from Cars.com."""

    def __init__(self, input_path):
        """
        Initialize the cleaner with the input CSV file path.
        
        Args:
            input_path (str): The path to the input CSV file.
        """
        self.input_path = input_path

    def clean_data(self):
        """
        Clean the data from the input CSV file.
        
        Returns:
            pd.DataFrame: Cleaned DataFrame containing car data.
        """
        # Read the data from the CSV file into a pandas DataFrame named 'cars'
        # Specify column names as "Title", "Miles", "Price", and "Deal"
        cars = pd.read_csv(self.input_path + '.csv', names=["Title", "Miles", "Price", "Deal", "Stock"])

        # Drop if no title
        cars = cars.dropna(subset=['Title'])
        cars = cars[~cars['Title'].str.contains('None')]

        # Extract the year, make, and model information from the 'Title' column
        cars['Year'] = cars['Title'].str.split(' ').str[0]
        cars['Make'] = cars['Title'].str.split(' ').str[1]
        cars['Model'] = cars['Title'].str.split(' ').str[2:].str.join(" ")

        # Extract sub-model info
        cars['Sub_Model'] = cars['Model'].str.lower().apply(lambda x: 'Luxury' if 'luxury' in x else ('Premium' if 'premium' in x else 'Base'))

        # Remove the last 4 characters from the 'Miles' column to remove ' miles'
        cars['Miles'] = cars['Miles'].str[:-4]

        # Replace "Not Priced" with 0, remove the dollar sign from 'Price'
        cars['Price'] = cars['Price'].replace("Not Priced", 0)
        cars['Price'] = cars['Price'].str[1:]

        # Extract only the first two words from the 'Deal' column
        cars['Deal'] = cars['Deal'].replace('"', '')
        cars['Deal'] = cars['Deal'].str.split(' ').str[:2].str.join(" ")

        # Convert 'Year' to integer type
        cars['Year'] = cars['Year'].fillna(0).astype(int)

        # Remove commas from 'Price' and 'Miles' and convert to integer
        cars['Price'] = cars['Price'].str.replace(',', '')
        cars['Miles'] = cars['Miles'].str.replace(',', '')

        # Drop rows with NaN values in 'Price', 'Miles' and convert to integers
        cars = cars.dropna(subset=['Price'])
        cars = cars.dropna(subset=['Miles'])
        cars['Price'] = cars['Price'].astype(int)
        cars['Miles'] = cars['Miles'].replace('', '0').astype(int)

        return cars

    def save_cleaned_data(self, cleaned_data, output_path):
        """
        Save the cleaned data to a new CSV file.
        
        Args:
            cleaned_data (pd.DataFrame): The cleaned DataFrame containing car data.
            output_path (str): The path to save the cleaned CSV file.
        """
        # Write the cleaned data back to a new CSV file with 'cleaned' appended to the original file name
        cleaned_data.to_csv(output_path + '_cleaned.csv', mode='w', index=False, header=True)

# Example Usage
# input_path = 'carsDotCom/data/output_May-05-2024'
# output_path = 'carsDotCom/data/output_May-05-2024'
# cleaner = CarsDotComCleaner(input_path)
# cleaned_data = cleaner.clean_data()
# cleaner.save_cleaned_data(cleaned_data, output_path)
