"""
For this project, your task is to create a CLI that takes as input the names of 
ingredients from a user. Then, your code will fetch the recipe information from 
the CodingNomads recipe collection, and search through the text of the recipes 
to find ones that include the provided ingredients.
"""

import requests
from bs4 import BeautifulSoup
import time

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
            ingredient_list.append(ingredient)
        else:
            break

    print(f"Here is your ingredient list:")
    for item in ingredient_list:
        print(item)

    return ingredient_list

def scrape_website(URL):
    """Scrape a website

    Args:
        URL (str): URL for website to scrape
    """
    # Send a GET request to the URL
    response = requests.get(URL)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content
        html_content = response.text
        print('Scraping successful. The content has been saved to "scraped_content.html"')
        
    else:
        print('Error: Failed to retrieve the web page')
        SystemExit()

    return html_content

def save_to_file (html_content):
    """Save extracted conent into a text file.

    Args:
        html_content (html): html from website
    """
    with open ('scraped_content.html', 'w') as file:
            file.write(html_content)


# Get links for each website and then scrape each website to find matching ingredients
def get_links (URL):
    """Get links for each website and then scrape each website to find matching ingredients

    Args:
        URL (website): website with recipes
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')

    link_list = [link.get('href') for link in links]
    
    prepended_links = []
    for item in link_list:
        prepended_links.append("https://codingnomads.github.io/recipes/" + item)
    
    return(prepended_links)



def scrape_links(recipe_link_list, user_ingredient_list):
    """Scrape each link and look for ingredients on the users list

    Args:
        recipe_link_list (list): list of links to recipes
        user_ingredient_list (list): ingredients the user has

    Returns:
        list: list of links with ingredients in them
    """
    links_with_word = []
    
    for link in recipe_link_list:
        counter = 0
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        webpage_text = soup.get_text().lower()

        for item in user_ingredient_list:
            if item.lower() in webpage_text:
               counter += 1
            
        if counter == len(user_ingredient_list):
            links_with_word.append(link)

    return links_with_word


if __name__ == "__main__":
    
    # Get user ingredient list
    user_ingredient_list = get_user_ingredients() 

    # Scrape website and save html to a file, only need to do once
    html_content = scrape_website(URL)

    # Save content to an html file
    save_to_file(html_content)

    # Get all recipe links on the page
    recipe_link_list = get_links(URL) 

    # Scrape each link for ingredients on the user ingredient list
    final_link_list = scrape_links(recipe_link_list, user_ingredient_list)

    if len(final_link_list) == 0:
        print("We did not find any recipes with all of your ingredients.")

    else:
        print(f"We found {len(final_link_list)} recipes with your ingredients in them.")
        print(f"Here is the list of recipe links with your ingredients:\n ")
        time.sleep(3)
        for item in final_link_list:
            print(item)