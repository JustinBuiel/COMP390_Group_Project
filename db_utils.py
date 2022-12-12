"""
This module contains all sql interactions with the database
the supporting functions are all private including insertions into tables for security
"""

import sqlite3


def _get_table_names():
    """ This private function returns the category names for use when creating and interacting with the tables """

    table_names = ['Over_Ear_Headphones', 'USB_microphones', '1080p_Webcams', 'Capture_Cards',
                   '8-channel_Audio_Mixers', 'Gaming_Laptops']
    return table_names


def _make_tables(db_cursor, table_name):
    """ This private function takes the database cursor object and a table name as it's
        parameters in order to create the 6 categories' tables. The tables are also cleared
        out so old data doesn't affect results """
    try:
        db_cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}(
                            product_name TEXT,
                            rating REAL,
                            num_ratings INTEGER,
                            price REAL,
                            product_url TEXT);''')
        db_cursor.execute(f'''DELETE FROM {table_name}''')
    except sqlite3.Error as create_error:
        print(f'A database error has occurred: {create_error}')


def _put_data_in_tables(category_tuple, db_connection, db_cursor, table_name):
    """ This private function takes the entry data, database cursor object and a table name
        as it's parameters in order to insert the product data into the correct table """
    product_name, rating, num_ratings, price, product_url = category_tuple
    try:
        db_cursor.execute(f'''INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?)''',
                          (product_name,
                           rating,
                           num_ratings,
                           price,
                           product_url))
        db_connection.commit()
    except sqlite3.Error as insert_error:
        print(f'A database error has occurred: {insert_error}')


def set_up_database():
    """ This function sets up our database and then creates the tables. The function
        returns the important connection and cursor objects for use throughout the program """
    db_connection = None
    try:
        # initialize the database and its important connection/cursor objects
        db_name = 'amazon_products.db'
        db_connection = sqlite3.connect(db_name)
        db_cursor = db_connection.cursor()
        print('Successfully connected to database')
        # create the tables by passing a table to the _make_tables function
        table_names = _get_table_names()
        for table_name in table_names:
            _make_tables(db_cursor, table_name)
        print('Successfully created all tables')
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')
    finally:
        return db_connection, db_cursor


def insertion_loop(category_dict: dict, db_connection, db_cursor, table_num: int):
    """ This function accepts a dictionary, the database connection and cursor and a table_num
    int in order to loop through the dictionary of products captured by the web scraper
    and insert said data into the correct tables """
    table_names = _get_table_names()
    for k, v in category_dict.items():
        _put_data_in_tables(v, db_connection, table_names[table_num])


def shut_down_data_base(db_connection):
    """ This function actually populates the database tables and disconnects from the database """

    db_connection.commit()
    db_connection.close()
