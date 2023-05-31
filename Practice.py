import requests
from bs4 import BeautifulSoup

URL = "https://codingnomads.github.io/recipes/recipes/3-honeycomb-cookies.html"

ingredient_list = ['milk', 'sugar', 'salt']

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
webpage_text = soup.get_text().lower()

print(webpage_text)

counter = 0

for item in ingredient_list:
    if item.lower() in webpage_text:
        counter += 1
        print(f"This item is in the recipe: {item}")
        print(f"This is how many items are found in this recipe page: {counter}")

if counter == len(ingredient_list):
    print("All the items were found in this recipe.")
else:
    print("Not all of the items were found in this recipe.")