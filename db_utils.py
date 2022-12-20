"""
This module contains all sql interactions with the database
the supporting functions are all private including insertions into tables for security
"""

import sqlite3


def _get_table_names():
    """ This private function returns the category names for use when creating and interacting with the tables """

    table_names = ['Over_Ear_Headphones', 'USB_microphones', 'Webcams', 'Capture_Cards',
                   'Audio_Mixers', 'Gaming_Laptops']
    return table_names


def _make_tables(db_cursor, db_connection, table_name):
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
        db_connection.commit()
    except sqlite3.Error as create_error:
        print(f'A database table creation error has occurred: {create_error}')


def put_data_in_tables(product_tuple, db_cursor, table_num):
    """ This private function takes the entry data, database cursor object and a table name
        as it's parameters in order to insert the product data into the correct table """
    product_name, rating, num_ratings, price, product_url = product_tuple
    table_names = _get_table_names()
    table_name = table_names[table_num]
    try:
        db_cursor.execute(f'''INSERT INTO {table_name} VALUES(?, ?, ?, ?, ?)''',
                          (product_name,
                           rating,
                           num_ratings,
                           price,
                           product_url))
    except sqlite3.Error as insert_error:
        print(f'A database insert error has occurred: {insert_error}')


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
            _make_tables(db_cursor, db_connection, table_name)
        print('Successfully created all tables')
    except sqlite3.Error as db_error:
        print(f'A database error has occurred: {db_error}')
    finally:
        return db_connection, db_cursor


def filter_data(table_num, stars, stars_eq, reviews, reviews_eq, price, price_eq, db_cursor):
    table_names = _get_table_names()
    table_name = table_names[table_num]
    sql = f'''SELECT * FROM {table_name} where rating {stars_eq} {stars} AND num_ratings {reviews_eq} {reviews} AND price {price_eq} {price}'''
    print(sql + '\n')
    try:
        response = db_cursor.execute(sql)
    except sqlite3.Error as query_error:
        print(f'A database error has occurred: {query_error}')
    with open('filtered_data.txt', 'a') as fileIO:
        fileIO.write(table_name + ' results: \n\n')
        for row in response:
            print(row)
            write_to_file(row, fileIO)
        fileIO.write('\n')


def write_to_file(row, fileIO):
    fileIO.write('Product: ' + str(row[0]) + '\n')
    fileIO.write('Rating: ' + str(row[1]) + '/5\n')
    fileIO.write('Number of Reviews: ' + str(row[2]) + '\n')
    fileIO.write('Price: ' + str(row[3]) + '\n')
    fileIO.write('URL: ' + str(row[4]) + '\n')
    fileIO.write('\n')


def shut_down_data_base(db_connection):
    """ This function actually populates the database tables and disconnects from the database """

    db_connection.commit()
    db_connection.close()
