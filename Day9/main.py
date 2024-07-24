# # Day 9 - Dictionaries
# # Estructure -> {Key: Value, Key: Value, ...}
# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
#                           "Function": "A piece of code that you can easily call over and over again.", 
#                           "Loop": "The action of doing something over and over again."}

# # List[position]
# # Dictionaries["Key]

# # print(programming_dictionary["Bug"])
# # Adding new items to dictionary.
# programming_dictionary["Alexander"] = "That's my name bruda!"

# # Creating and empty dictionary.
# empty_dic = {}

# # Wipe dictionary
# # programming_dictionary = {}

# # Edit an item in a dictionary.
# programming_dictionary["Bug"] = "A moth in your computer."

# # Loop through a dictionary.
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# print(programming_dictionary)

# # Exercise - Grading Program
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# print(student_grades)

# # Nested dictionaries
# # Nesting
# capitals = {"France": "Paris", 
#             "Germany": "Berlin"}

# # Nesting a list in a Dictionary
# trvel_log = {"France": ["Paris", "Lille", "Dijon"], 
#              "Germany": ["Berlin", "Hamburg", "Stuttgart"],
#              }

# # Nesting Dictionary in a Dictionary
# travel_log_v2 = {
#                 "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12}, 
#                  "Germany": {"cities_visited": ["Andernach", "Ilmenau", "Miessenheim", "Berlin", "Frankfurt"], "total_visits": 5}
#                  }

# # Nesting a Dictionary in a List
# travel_log_v3 = [
#     {
#         "country": "France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     }, 
#     {
#         "country": "Germany", 
#         "cities_visited": ["Andernach", "Ilmenau", "Miessenheim", "Berlin", "Frankfurt"], 
#         "total_visits": 5
#     }, 
# ]

# # Exercise - Dictionary in a List
# country = input() # Add country name
# visits = int(input()) # Number of visits
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# def add_new_country(name, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = name
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)

# add_new_country(country, visits, list_of_cities)

# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

# Exercise - The Secret Auction Program
import os
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    bidder_name = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bid:
            highest_bid = bidding_record[bidder]
            bidder_name = bidder
    
    print(f"The winner is {bidder_name} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    
    if input("Are there any other bidders? Type 'yes' or 'no'.\n") == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    else:
        os.system('cls')
        print(logo)
