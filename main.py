import db_utils
from UI_Funcs import *

"""Group members:
    Justin Buiel
    Dylan Foster
    Sean Howe"""


def main():
    db_connection, db_cursor = db_utils.set_up_database()
    # web scraper call
    # ui call
    db_utils.shut_down_data_base(db_connection)


if __name__ == '__main__':
    main()


# Dylan Testing of User Interface
#    user_Interface()

