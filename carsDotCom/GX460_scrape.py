from carsDotComScrape import CarsDotComScraper
from carsFileCleaning import CarsDotComCleaner
from datetime import date 

# # Define the URL to scrape data from Cars.com
first_url = 'https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=lexus&maximum_distance=all&mileage_max=&models[]=lexus-gx_460&monthly_payment=&page=1&page_size=100&sort=year&stock_type=all&year_max=&year_min=2014&zip=75208'
# Instantiate a CarsDotComScraper object with the first URL
scraper = CarsDotComScraper(first_url)
# Call the scrape_data method to scrape data from Cars.com
scraper.scrape_data()

# Generate the input path for the cleaned data using today's date
input_path = "carsDotCom/data/output_" + date.today().strftime("%b-%d-%Y")
output_path = input_path
# Instantiate a CarsDotComCleaner object with the input path
cleaner = CarsDotComCleaner(input_path)
# Call the clean_data method to clean the scraped data
cleaned_data = cleaner.clean_data()
# Call the save_cleaned_data method to save the cleaned data to a new CSV file
cleaner.save_cleaned_data(cleaned_data, output_path)
