import requests
from bs4 import BeautifulSoup
from db_utils import *
import sqlite3

HEADERS_FOR_GET_REQ = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
     'Accept-Language': 'en-US, en;q=0.5'}
)


def scraper(category_dict: dict, db_cursor):
    for item, key in category_dict.items():
        search_url = create_target_URL(item)
        search_results = find_search_results(search_url, key, db_cursor)


def create_target_URL(keywords: str):
    query_terms = keywords.replace(' ', '+')
    base_amazon_search_url = 'https://www.amazon.com/s?k='
    search_url = f'{base_amazon_search_url}{query_terms}'
    return search_url


def find_search_results(search_url: str, key: int, db_cursor):
    listing_counter = 0
    listing_limit = 10
    url_results_page_param = 1
    while listing_counter < listing_limit:
        print("loop", listing_counter, listing_limit)
        results_url_param = f'&page={url_results_page_param}'
        search_page_url = f'{search_url}{results_url_param}'
        response = requests.get(search_page_url, headers=HEADERS_FOR_GET_REQ)
        print(response.status_code)
        soup_format = BeautifulSoup(response.content, 'html.parser')
        search_results = soup_format.find_all('div',
                                              {'class': 's-result-item', 'data-component-type': 's-search-result'})
        listing_counter = extracting_search_results(search_results, listing_counter, listing_limit, url_results_page_param, key,
                                                    db_cursor)
        url_results_page_param += 1


def extract_product_name(listing_block):
    product_name = listing_block.h2.text
    return product_name


def extract_product_rating(listing_block):
    try:
        rating_info = listing_block.find('i', {'class': 'a-icon'}).text
        return rating_info
    except AttributeError:
        return None


def extract_num_ratings(listing_block):
    try:
        num_ratings = listing_block.find('span', {'class': 'a-size-base s-underline-text'}).text
        return num_ratings
    except AttributeError:
        return None


def extract_product_price(listing_block):
    try:
        price_integer = listing_block.find('span', {'class': 'a-price-whole'}).text
        price_decimal = listing_block.find('span', {'class': 'a-price-fraction'}).text
        return price_integer + price_decimal
    except AttributeError:
        return None


def extract_product_URL(listing_block):
    try:
        product_url_segment = listing_block.h2.a['href']
        complete_product_url = 'https://amazon.com' + product_url_segment
        return complete_product_url
    except AttributeError:
        return None


def extracting_search_results(search_results: list, listing_counter: int, listing_limit: int,
                              url_results_page_param: int, key: int, db_cursor):
    for listing in search_results:
        listing_counter += 1
        if listing_counter > listing_limit:
            print("break", listing_limit, listing_counter)
            break
        db_table_row_data = [None, None, None, None, None]
        db_table_row_data[0] = extract_product_name(listing)
        db_table_row_data[1] = extract_product_rating(listing)
        db_table_row_data[2] = extract_num_ratings(listing)
        db_table_row_data[3] = extract_product_price(listing)
        db_table_row_data[4] = extract_product_URL(listing)
        put_data_in_tables(tuple(db_table_row_data), db_cursor, key)
        print("extracted")
    return listing_counter
