"""
Contains functions used to make the UI of the project
"""

import db_utils


def user_Interface(db_cursor):
    """Makes use of below functions to create how the UI looks and works"""
    introduction(db_cursor)


def is_nums(user_input: str):
    """Checks if the input only contains digits"""
    if user_input.isdigit():
        return True
    else:
        return False


def has_dot(usr_input: str):
    """Checks if the number has a dot in it"""
    if usr_input.find('.') != -1:
        return True
    else:
        return False


def introduction(db_cursor):
    """Prints the product category message and takes the users input"""
    print('\n0. Over Ear Headphones\n''1. USB Microphones\n''2. 1080p Webcams\n''3. Capture Cards\n''4. 8-channel Audio Mixers\n''5. Gaming Laptops \n')
    uI_num = input('Choose one of the Product Categories: ')
    if is_nums(uI_num) is False:
        print('Please enter a valid value \n')
        introduction(db_cursor)
    uI_num = int(uI_num)
    if uI_num != 0 and uI_num != 1 and uI_num != 2 and uI_num != 3 and uI_num != 4 and uI_num != 5:
        print('Please enter a valid value \n')
        introduction(db_cursor)
    else:
        print()
        follow_up_questions(uI_num, db_cursor)


def follow_up_questions(table_num, db_cursor):
    """Contains the rest of the questions posed to the user and takes their answer to give them the end result"""
    stars = stars_Target()
    stars_eq = stars_Equality()
    print()
    reviews = reviews_Target()
    reviews_eq = reviews_Equality()
    print()
    price = price_Target()
    price_eq = price_Equality()
    print()
    db_utils.filter_data(table_num, stars, stars_eq, reviews, reviews_eq, price, price_eq, db_cursor)
    print()
    yes_or_No(db_cursor)


def stars_Target():
    """Asks the user to enter a star review"""
    star_review = input('Enter a target star review (ex. \'4.5\'): ')
    reals_review = 0
    if is_nums(star_review) is True:
        reals_review = int(star_review)
    else:
        dot_removed = star_review.replace('.', '')
        if is_nums(dot_removed):
            reals_review = float(star_review)
        else:
            reals_review = 5.1
    if reals_review < 0.0 or reals_review > 5.0:
        print('Please enter a valid value \n')
        stars_Target()
    return reals_review


def stars_Equality():
    """Asks the user to enter an equality operator to sort the star reviews"""
    star_equality_op = input('Choose an equality operator (>, <, >=, <=, =): ')
    if star_equality_op != '>' and star_equality_op != '<' and star_equality_op != '>=' and star_equality_op != '<=' and star_equality_op != '=':
        print('Please enter a valid value')
        stars_Equality()
    return star_equality_op


def reviews_Target():
    """Asks the user for their desired number of reviews"""
    num_of_reviews = input('Enter a target number of reviews (ex. 1000): ')
    if is_nums(num_of_reviews) is False:
        print('Please enter a valid value \n')
        reviews_Target()
    else:
        num_of_reviews = int(num_of_reviews)
    if num_of_reviews < 0 or num_of_reviews > 100000:
        print('Please enter a valid value')
        reviews_Target()
        return None
    return num_of_reviews


def reviews_Equality():
    """Asks the user to enter an equality operator to sort their number of reviews"""
    review_num_op = input('Choose an equality operator (>, <, >=, <=, =): ')
    if review_num_op != '>' and review_num_op != '<' and review_num_op != '>=' and review_num_op != '<=' and review_num_op != '=':
        print('Please enter a valid value')
        reviews_Equality()
    else:
        return review_num_op


def price_Target():
    """Asks the user for their desired price"""
    target_price = input('Enter a target price (ex. \'59.99\'): ')
    realp_review = 0
    if is_nums(target_price) is True:
        realp_review = int(target_price)
    else:
        choice_dot_remove = target_price.replace('.', '')
        if is_nums(choice_dot_remove) is True:
            realp_review = float(target_price)
        else:
            realp_review = 11111111.0
    if realp_review < 0.0 or realp_review > 100000.0:
        print('Please enter a valid value \n')
        price_Target()
    return realp_review


def price_Equality():
    """Asks the user to enter an equality operator to sort their price"""
    price_op = input('Choose an equality operator (>, <, >=, <=, =): ')
    if price_op != '>' and price_op != '<' and price_op != '>=' and price_op != '<=' and price_op != '=':
        print('Please enter a valid value')
        price_Equality()
    else:
        return price_op


def yes_or_No(db_cursor):
    """Asks the user if they would like to repeat the process and repeats if they say yes, asks them to type again if
    they give an answer that is not yes or no, and ends the program if the user types no"""
    repeat_OR_not = input('Would you like to execute another query? (yes/no): ')
    if repeat_OR_not == 'yes':
        user_Interface(db_cursor)
        return repeat_OR_not
    elif repeat_OR_not == 'no':
        exit()
    else:
        print('Please type \'yes\' or \'no\'\n')
        yes_or_No(db_cursor)
