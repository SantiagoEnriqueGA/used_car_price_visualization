# ------------------------------------------------------------------------------------
# SEGA97
# Gets Cars.com link from user and extract info from listings to csv output
# appends to csv after each page
# ------------------------------------------------------------------------------------

# Import necessary libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date

# Set Desired Filters and set the number of pages to scrape.
# URL of first page and number of total pages
firstURL = 'https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=lexus&maximum_distance=all&mileage_max=&models[]=lexus-gx_460&monthly_payment=&page=1&page_size=100&sort=year&stock_type=used&year_max=&year_min=2014&zip=75208'
numPages = 15

# Initialize the URLs list with the firstURL
URLs = [firstURL]

# Loop through the range of numPages (from 2 to numPages+1) to create additional URLs
for page in range(2, numPages+1):
    # Construct the URL for each page and append it to the URLs list
    pageURL = firstURL.replace('page=1', f'page={page}')
    URLs.append(pageURL)

# Iterate through each URL (page)
for URL in URLs:
    # Making a GET request
    r = requests.get(URL)

    # Create a BeautifulSoup object to parse HTML content
    soup = bs(r.content, 'html.parser')

    # Parse the HTML content to extract vehicle details
    html_soup = bs(r.text, 'html.parser')
    content_list = html_soup.find_all('div', attrs={'class': 'vehicle-details'})

    # Extract specific information like title, mileage, price, and deal info from HTML
    title_info = []
    for item in content_list:
        title_info.append(item.find_all('a', attrs={'class': 'vehicle-card-link js-gallery-click-link'}))
    mile_info = []
    for item in content_list:
        mile_info.append(item.find_all('div', attrs={'class':'mileage'}))
    price_info = []
    for item in content_list:
        price_info.append(item.find_all('div', attrs={'class':'price-section price-section-vehicle-card'}))
    deal_info = []
    for item in content_list:
        deal_info.append(item.find_all('button', attrs={'data-qa':'vehicle-badging'}))

    # Define functions to extract data from the parsed HTML and add it to lists
    def get_names(title_info):
        names = []
        for item in title_info:
            if(len(item) ==0):
                names.append('None')
            for i in item:
                names.append(i.find_all("h2", attrs = {"class" : "title"})[0].text.strip())
        return names
    def get_miles(mile_info):
        miles = []
        for item in mile_info:
            if(len(item) ==0):
                miles.append('None')
            for i in item:
                miles.append(i.text)
        return miles
    def get_price(price_info):
        price = []
        for item in price_info:
            if(len(item) ==0):
                item.append(0)
            for i in item:
                price.append(i.find_all("span", attrs = {"class" : "primary-price"})[0].text.strip())
        return price
    def get_deal(deal_info):
        deal = []
        for item in deal_info:
            if len(item) == 0:
                deal.append('None')
            for i in item:
                spans = i.find_all("span", attrs={"data-qa": "price-badge-text"})
                if spans:  # Check if spans list is not empty
                    temp = spans[0].text.strip()
                    temp = temp.split(" Deal")[0]  # Keep only text before " Deal"
                    deal.append(temp)
                else:
                    deal.append('None')  # If no matching span found, append 'None'
        return deal


    # Call the functions to extract data and store the results in lists
    car_names = get_names(title_info)
    car_miles = get_miles(mile_info)
    car_price = get_price(price_info)
    car_deal = get_deal(deal_info)


    # Create a DataFrame using Pandas to organize the extracted data
    carDf = pd.DataFrame(
        {'name': car_names,
        'miles': car_miles,
        'price': car_price,
        'deal': car_deal
        })


    # Print the DataFrame (optional for debugging purposes)
    # print(carDf)

    # Append the data from the DataFrame to a CSV file named 'output.csv'
    today = date.today()
    todayDate = today.strftime("%b-%d-%Y")
    carDf.to_csv('carsDotCom/output_'+todayDate+'.csv', mode='a', index=False, header=False)

print('CSV Written to: carsDotCom/output_'+todayDate+'.csv')
