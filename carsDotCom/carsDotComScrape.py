# Import necessary libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date

# Define a class for scraping Cars.com data
class CarsDotComScraper:
    """
    A class to scrape data from cars.com website.

    Attributes:
        first_url (str): The URL of the first page to scrape.
        num_pages (int): The number of pages for pagination.
        urls (list): List of URLs for all pages.
        today_date (str): The current date for naming the output file.
    """

    def __init__(self, first_url):
        """
        Initialize the scraper with the first URL provided.
        
        Args:
            first_url (str): The URL of the first page to scrape.
        """
    
        # Initialize the scraper with the first URL provided
        self.first_url = first_url
        # Get the number of pages for pagination
        self.num_pages = self.return_num_pages()
        # Generate a list of URLs for all pages
        self.urls = self.generate_urls()
        # Get the current date for naming the output file
        self.today_date = date.today().strftime("%b-%d-%Y")

    # Method to get the number of pages by inspecting the last page URL
    def return_num_pages(self):
        """
        Get the number of pages for pagination by inspecting the last page URL.
        
        Returns:
            int: The number of pages.
        """
        page_number = 1000  # A large number to ensure we get redirected to the last page
        new_url = self.first_url.replace("page=1", f"page={page_number}")
        response = requests.get(new_url, allow_redirects=False)
        redirected_url = response.headers['Location']
        last_page_number = int(redirected_url.split('page=')[-1].split('&')[0])
        return last_page_number

    # Method to generate URLs for all pages based on the first URL and number of pages
    def generate_urls(self):
        """
        Generate a list of URLs for all pages based on the first URL and number of pages.
        
        Returns:
            list: List of URLs for all pages.
        """
        urls = [self.first_url]
        for page in range(2, self.num_pages + 1):
            page_url = self.first_url.replace('page=1', f'page={page}')
            urls.append(page_url)
        return urls

    # Method to scrape data from all generated URLs
    def scrape_data(self):
        """
        Scrape data from all generated URLs and save it to a CSV file.
        """
        print(f"Scraping data from {self.num_pages} pages.")
        for url in self.urls:
            r = requests.get(url)
            soup = bs(r.content, 'html.parser')
            html_soup = bs(r.text, 'html.parser')
            content_list = html_soup.find_all('div', attrs={'class': 'vehicle-details'})
            title_info = [item.find_all('a', attrs={'class': 'vehicle-card-link js-gallery-click-link'}) for item in content_list]
            mile_info = [item.find_all('div', attrs={'class':'mileage'}) for item in content_list]
            price_info = [item.find_all('div', attrs={'class':'price-section price-section-vehicle-card'}) for item in content_list]
            deal_info = [item.find_all('button', attrs={'data-qa':'vehicle-badging'}) for item in content_list]
            stock_info = [item.find_all('p', attrs={'class':'stock-type'}) for item in content_list]

            # Extract data using helper methods
            car_names = self.get_names(title_info)
            car_miles = self.get_miles(mile_info)
            car_price = self.get_price(price_info)
            car_deal = self.get_deal(deal_info)
            car_stock = self.get_stock(stock_info)

            # Create a DataFrame and save data to CSV
            car_df = pd.DataFrame({
                'name': car_names,
                'miles': car_miles,
                'price': car_price,
                'deal': car_deal,
                'stock': car_stock
            })
            car_df.to_csv(f'carsDotCom/data/output_{self.today_date}.csv', mode='a', index=False, header=False)

        print(f'CSV Written to: carsDotCom/data/output_{self.today_date}.csv')

    # Static method to extract car names from title_info
    @staticmethod
    def get_names(title_info):
        """
        Static method to extract car names from title_info.
        
        Args:
            title_info (list): List of title information.
            
        Returns:
            list: List of car names.
        """
        names = []
        for item in title_info:
            if len(item) == 0:
                names.append('None')
            for i in item:
                names.append(i.find_all("h2", attrs={"class": "title"})[0].text.strip())
        return names

    # Static method to extract car miles from mile_info
    @staticmethod
    def get_miles(mile_info):
        """
        Static method to extract car names from title_info.
        
        Args:
            title_info (list): List of title information.
            
        Returns:
            list: List of car names.
        """
        miles = []
        for item in mile_info:
            if len(item) == 0:
                miles.append('None')
            for i in item:
                miles.append(i.text)
        return miles

    # Static method to extract car prices from price_info
    @staticmethod
    def get_price(price_info):
        """
        Static method to extract car names from title_info.
        
        Args:
            title_info (list): List of title information.
            
        Returns:
            list: List of car names.
        """
        price = []
        for item in price_info:
            if len(item) == 0:
                item.append(0)
            for i in item:
                price.append(i.find_all("span", attrs={"class": "primary-price"})[0].text.strip())
        return price

    # Static method to extract car deal information from deal_info
    @staticmethod
    def get_deal(deal_info):
        """
        Static method to extract car names from title_info.
        
        Args:
            title_info (list): List of title information.
            
        Returns:
            list: List of car names.
        """
        deal = []
        for item in deal_info:
            if len(item) == 0:
                deal.append('None')
            for i in item:
                spans = i.find_all("span", attrs={"data-qa": "price-badge-text"})
                if spans:
                    temp = spans[0].text.strip()
                    temp = temp.split(" Deal")[0]
                    deal.append(temp)
                else:
                    deal.append('None')
        return deal

    # Static method to extract car stock information from stock_info
    @staticmethod
    def get_stock(stock_info):
        """
        Static method to extract car names from title_info.
        
        Args:
            title_info (list): List of title information.
            
        Returns:
            list: List of car names.
        """
        stock = []
        for item in stock_info:
            if len(item) == 0:
                stock.append('None')
            else:
                stock.append(item[0].text.strip())
        return stock

# Example Usage
# first_url = 'https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=lexus&maximum_distance=all&mileage_max=&models[]=lexus-gx_460&monthly_payment=&page=1&page_size=100&sort=year&stock_type=all&year_max=&year_min=2014&zip=75208'
# scraper = CarsDotComScraper(first_url)
# scraper.scrape_data()
