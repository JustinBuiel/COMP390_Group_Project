# COMP390 Group Project - Sean Howe, Dylan Foster, Justin Buiel - COMP 390-001

https://github.com/JustinBuiel/COMP390_Group_Project
___
libraries:
  - bs4 (Beautiful Soup)
  - requests
  - sqlite3
  - pytest
  - testfixtures
  - time

___

This project collects and filters Amazon’s product data for 6 search keywords:
  - Over Ear Headphones
  - USB Microphones
  - 1080p Webcams
  - Capture Cards
  - 8-channel Audio Mixers
  - Gaming Laptops

The User then filters by category, number of ratings, the rating itself, and the price and then stores them in a filtered file. 

___

To use the program, make sure you have python 3.11 installed and run the following commands inside the directory:

pip install requests</br>
pip install bs4

This will ensure you have the proper tools to run the program, you can then run

python amazon_product_finder.py

The program will tell you that it is crating the database and searching for each category of product. Please by patient and wait for the prompt to ask you for what you want to filter. Answer the questions using valid inputs, and then head over to the filtered data text file to find all the results.

___

Developed in Python 3.11

PyCharm 2022.3 (Community Edition)
Build #PC-223.7571.203, built on November 30, 2022
Runtime version: 17.0.5+1-b653.14 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
Windows 10 10.0
GC: G1 Young Generation, G1 Old Generation
Memory: 2048M
Cores: 20
___
Edition	Windows 10 Home Single Language
Version	21H2
Installed on	‎1/‎23/‎2022
OS build	19044.2364
Experience	Windows Feature Experience Pack 120.2212.4190.0
