'''IN PROGRESS Contains functions used to make the UI of the project'''

'''Makes use of below functions to create how the UI looks and works'''

def user_Interface():
    introduction()
    follow_up_questions()


'''Prints the product category message and takes the users input'''

def introduction():
    print(" 1. Over Ear Headphones \n " "2. USB Microphones \n ""3. 1080p Webcams \n ""4. Capture Cards \n ""5. 8-channel Audio Mixers \n"" 6. Gaming Laptops \n")
    uI_num = input("Choose one of the Product Categories: \n")
    if not uI_num.isdigit():
        print("Please enter a valid value \n")
        introduction()
        print("\n")
    uI_num = int(uI_num)
    if uI_num != 1 and uI_num != 2 and uI_num != 3 and uI_num != 4 and uI_num != 5 and uI_num != 6:
        print("Please enter a valid value \n")
        introduction()
        print("\n")
    else:
        follow_up_questions()
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


'''Asks the user to enter a star review'''


def stars_Target():
    star_review = input("Enter a target star review (ex. '4.5'): ")
    reals_review = 0
    if star_review.isdigit():
        reals_review = int(star_review)
    elif "." in star_review:
        choice_dot = star_review
        choice_dot_remove = choice_dot.replace(".","")
        if choice_dot_remove.isdigit():
            reals_review = float(star_review)
    else:
        print("Please enter a valid value")
        stars_Target()
    if reals_review < 0.0 or reals_review > 9.9:
         print("Please enter a valid value \n")
         stars_Target()


'''Asks the user to enter an equality operator to sort the star reviews'''


def stars_Equality():
    star_equality_op = input("Choose an equality operator (>, <, >=, <=, =): ")
    if star_equality_op != '>' and star_equality_op != '<' and star_equality_op != '>=' and star_equality_op != '<=' and star_equality_op != '=':
        print("Please enter a valid value")
        stars_Equality()
        print("\n")
    print("\n")

'''Asks the user for their desired number of reviews'''


def reviews_Target():
    num_of_reviews = input("Enter a target number of reviews (ex. '1000'): ")
    if not num_of_reviews.isdigit():
        print("\n")
        print("Please enter a valid value \n")
        reviews_Target()
        print("\n")
    else:
        num_of_reviews = int(num_of_reviews)
    if num_of_reviews < 0 or num_of_reviews > 100000:
        print("Please enter a valid value")
        reviews_Target()
        print("\n")
    print("\n")


'''Asks the user to enter an equality operator to sort their number of reviews'''


def reviews_Equality():
    review_num_op = input("Choose an equality operator (>, <, >=, <=, =): ")
    if review_num_op != '>' and review_num_op != '<' and review_num_op != '>=' and review_num_op != '<=' and review_num_op != '=':
        print("Please enter a valid value")
        reviews_Equality()
        print("\n")
    print("\n")


'''Asks the user for their desired price'''


def price_Target():
    target_price = input("Enter a target price (ex. '59.99'): ")
    realp_review = 0
    if target_price.isdigit():
        realp_review = int(target_price)
    elif "." in target_price:
        choice_dot = target_price
        choice_dot_remove = choice_dot.replace(".","")
        if choice_dot_remove.isdigit():
            realp_review = float(target_price)
    else:
        print("Please enter a valid value")
        price_Target()
    if realp_review < 0.0 or realp_review > 100000.0:
         print("Please enter a valid value \n")
         price_Target()


'''Asks the user to enter an equality operator to sort their price'''


def price_Equality():
    price_op = input("Choose an equality operator (>, <, >=, <=, =): ")
    if price_op != '>' and price_op != '<' and price_op != '>=' and price_op != '<=' and price_op != '=':
        print("Please enter a valid value")
        price_Equality()
        print("\n")
    print("\n")


'''Asks the user if they would like to repeat the process and repeats if they say yes, asks them to type again if 
    they give an answer that is not yes or no, and ends the program if the user types no'''


def repeat_project_answer():
    yes_or_no = input("Would you like to execute another query? (yes/no): ")
    if yes_or_no == 'yes':
        print("\n")
        user_Interface()
        print("\n")
    elif yes_or_no == 'no':
        exit()
    else:
        print("Please type 'yes' or 'no' ")
        print("\n")
        repeat_project_answer()
