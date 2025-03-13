import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_price(url):
    """
    Crawls the given URL, extracts the price from the HTML content, and returns it.

    Args:
        url (str): The URL to crawl.

    Returns:
        str: The price of the property.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    price = soup.find('span', class_='house-price d-flex flex-row flex-md-column flex-lg-row align-items-lg-center ng-star-inserted').text 
    price = int(re.findall('[0-9]+', price.replace('.', ''))[0])
    return price

def create_data_frame(filename):
    """
    Reads the addresses from the given file and creates a pandas DataFrame.

    Args:
        filename (str): The name of the file containing the addresses.

    Returns:
        pandas.DataFrame: A DataFrame containing the addresses and prices.
    """
    with open(filename, 'r') as file:
        addresses = file.readlines()
    
    df = (pd.DataFrame(addresses, columns=['Address'])
          .drop_duplicates()
          .reset_index(drop=True))

    price_lst = [get_price(address) for address in df['Address']]
    df['Price'] = price_lst
    return df
    

if __name__ == '__main__':
    url = 'https://www.boliga.dk/adresse/soendervangen-1-8700-horsens-531389064'
    price = get_price(url)
    print(price)