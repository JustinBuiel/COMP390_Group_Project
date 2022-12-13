# for Sean: when you finish getting all the items for a category
# make a call like db_utils.insertion_loop(dict, db_connection, db_cursor, table_num)
# where dict is a dictionary with unimportant keys and a list or tuple with the 5 data points
# for each product and table_num is 0 for headphones, 1 for microphones and so on.
# you can do this in here or in main, but you will need both db_connection and db_cursor

import requests
from bs4 import BeautifulSoup
from db_utils import *
import sqlite3

HEADERS_FOR_GET_REQ = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
     'Accept-Language': 'en-US, en;q=0.5'}
)

# Over Ear Headphones - 0
# USB Microphones - 1
# 1080p Webcams - 2
# Capture Cards - 3
# 8-channel Audio Mixers - 4
# Gaming Laptops - 5

def scraper():
    search_url = create_target_URL()
    search_results = find_search_results(search_url)

def create_target_URL(keywords: str):
    query_terms = keywords.replace(' ', '+')
    base_amazon_search_url = 'https://www.amazon.com/s?k='
    search_url = f'{base_amazon_search_url}{query_terms}'
    return search_url

def find_search_results(search_url: str):
    listing_counter = 0
    listing_limit = 300
    url_results_page_param = 1
    while listing_counter < listing_limit:
        search_results = gathering_search_results(search_url , url_results_page_param)


def gathering_search_results(search_url:str, url_results_page_param:int):
    results_url_param = f'&page={url_results_page_param}'
    search_page_url = f'{search_url}{results_url_param}'
    response = requests.get(search_page_url, headers=HEADERS_FOR_GET_REQ)
    soup_format = BeautifulSoup(response.content, 'html.parser')
    search_results = soup_format.find_all('div',
                                          {'class': 's-result-item', 'data-component-type': 's-search-result'})
    return search_results

def extracting_search_results(search_results):

# listing_counter = 0
# listing_limit = 300
# url_results_page_param = 1
# while listing_counter < listing_limit:
#     results_url_param = f'&page={url_results_page_param}'
#     search_page_url = f'{search_url}{results_url_param}'
#     response = requests.get(search_page_url, headers=HEADERS_FOR_GET_REQ)
#     soup_format = BeautifulSoup(response.content, 'html.parser')
#     search_results = soup_format.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
#     for listing in search_results:
#         listing_counter ++
#         if listing_counter > listing_limit:
#            break
#     db_table_row_data = [null, null, null, null, null]
#     listing_data[0] = extract_product_name()
#     listing_data[1] = extract_product_rating()
#     listing_data[2] = extract_num_ratings()
#     listing_data[3] = extract_product_price()
#     listing_data[4] = extract_product_URL()
#     insert_values_into_db_table(db_cursor, 'table_name', tuple(listing_data))
#     url_results_page_param ++
