
'''IN PROGRESS Contains functions used to make the UI of the project'''


'''Makes use of below functions to create how the UI looks and works'''
def user_Interface():
    introduction()
    follow_up_questions()

'''Prints the product category message and takes the users input'''
def introduction():
    UI_num = input("Choose a Product Category: \n"
          " 1. Over Ear Headphones \n "
          "2. USB Microphones \n "
          "3. 1080p Webcams \n "
          "4. Capture Cards \n "
          "5. 8-channel Audio Mixers \n"
          " 6. Gaming Laptops \n")
    # if UI_num != '1' or '2' or '3' or '4' or '5' or '6':
    #     print("Please enter a valid value")
    print("\n")


'''Contains the rest of the questions asked to the user and takes their answer to give them the end result'''
def follow_up_questions():
    stars_Target()
    print("\n")
    stars_Equality()
    print("\n")
    reviews_Target()
    print("\n")
    reviews_Equality()
    print("\n")
    price_Target()
    print("\n")
    price_Equality()
    print("\n")
    repeat_project_answer()
    print("\n")

'''Asks the user to enter a star review'''
def stars_Target():
    star_review = input("Enter a target star review (ex. '4.5'): ")
    # if star_review < 0.0 or star_review > 9.9:
    #     print("Please enter a valid value")

'''Asks the user to enter an equality operator to sort the star reviews'''
def stars_Equality():
    star_equality_op = input("Choose an equality operator (>, <, >=, <=, =): ")
    # if star_equality_op != '>' or '<' or '>=' or '<=' or '=':
    #     print("Please enter a valid value")
    #     stars_Equality()
    # print("\n")

'''Asks the user for their desired number of reviews'''
def reviews_Target():
    num_of_reviews = input("Enter a target number of reviews (ex. '1000'): ")
    # if num_of_reviews < 0 or num_of_reviews > 1000:
    #     print("Please enter a valid value")

'''Asks the user to enter an equality operator to sort their number of reviews'''
def reviews_Equality():
    review_num_op = input("Choose an equality operator (>, <, >=, <=, =): ")
    # if review_num_op != '>' or '<' or '>=' or '<=' or '=':
    #     print("Please enter a valid value")
    #     reviews_Equality()
    # print("\n")

'''Asks the user for their desired price'''
def price_Target():
    target_price = input("Enter a target price (ex. '59.99'): ")
    # if target_price < 0.0 or target_price > 1000:
    #     print("Please enter a valid value")

'''Asks the user to enter an equality operator to sort their price'''
def price_Equality():
    price_op = input("Choose an equality operator (>, <, >=, <=, =): ")
    # if price_op != '>' or '<' or '>=' or '<=' or '=':
    #     print("Please enter a valid value")
    #     price_Equality()
    # print("\n")

'''Asks the user if they would like to repeat the process and repeats if they say yes, asks them to type again if 
    they give an answer that is not yes or no, and ends the program if the user types no'''
def repeat_project_answer():
    yes_or_no = input("Would you like to execute another query? (yes/no): ")
    if yes_or_no == 'yes':
        print("\n")
        user_Interface()
        print("\n")
    elif yes_or_no == 'no':
        return 0
    else:
        print("Please type 'yes' or 'no' ")
        print("\n")
        repeat_project_answer()

