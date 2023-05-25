"""
For this project, your task is to create a CLI that takes as input the names of 
ingredients from a user. Then, your code will fetch the recipe information from 
the CodingNomads recipe collection, and search through the text of the recipes 
to find ones that include the provided ingredients.
"""

import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.github.io/recipes/"

def get_user_ingredients():
    """Get the user list of ingredients

    Returns:
        list: ingredients
    """
    ingredient_list = []
    first_ingredient = input("Please enter your first ingredient: \n")
    ingredient_list.append(first_ingredient)

    while True:
        response = input("Would you like to enter another ingredient? Y or N \n")
        if response == "Y":
            ingredient = input("Please enter your ingredient: \n")
            ingredient_list.append(ingredient_list)
        else:
            break

    print(f"Here is your ingredient list:")
    for item in ingredient_list:
        print(item)

    return ingredient_list

user_ingredient_list = get_user_ingredients()


def scrape_website(URL):
    """Scrape a website and save the response to a local html file

    Args:
        URL (str): URL for website to scrape
    """
    # Send a GET request to the URL
    response = requests.get(URL)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text

        # Save the extracted content into a text file
        with open ('scraped_content.html', 'w') as file:
            file.write(html_content)

        print('Scraping successful. The content has been saved to "scraped_content.html"')
    else:
        print('Error: Failed to retrieve the web page')

scrape_website(URL)

