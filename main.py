"""
This is the main driver of the program. It makes calls to the other functions in other modules.
"""

import db_utils
from UI_Funcs import user_Interface
from web_scraper import scraper

category_dict = {
    "Over Ear Headphones": 0,
    "USB Microphones": 1,
    "1080p Webcams": 2,
    "Capture Cards": 3,
    "8-channel Audio Mixers": 4,
    "Gaming Laptops": 5
}


def main():
    """This is the main function, it is called when the program is run.
    This module calls other functions that do the heavy lifting"""
    db_connection, db_cursor = db_utils.set_up_database()
    scraper(category_dict, db_cursor)
    db_connection.commit()
    print("Database population complete.")
    with open('filtered_data.txt', 'w'):
        pass
    user_Interface(db_cursor)
    db_utils.shut_down_data_base(db_connection)


if __name__ == '__main__':
    main()
