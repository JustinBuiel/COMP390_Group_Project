import db_utils
from UI_Funcs import *
from web_scraper import scraper

"""Group members:
    Justin Buiel
    Dylan Foster
    Sean Howe"""

category_dict = {
    "Over Ear Headphones": 0,
    "USB Microphones": 1,
    "1080p Webcams": 2,
    "Capture Cards": 3,
    "8-channel Audio Mixers": 4,
    "Gaming Laptops": 5
}


def main():
    # db_connection, db_cursor = db_utils.set_up_database()
    # scraper(category_dict, db_cursor)
    # db_connection.commit()
    # print("commit")
     user_Interface()
    # db_utils.shut_down_data_base(db_connection)


if __name__ == '__main__':
    # print_hi('name')

    main()
