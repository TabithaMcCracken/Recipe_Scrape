# Recipe Finder

This script allows a user to input ingredients they have on hand and returns recipes from a specific website (`https://codingnomads.github.io/recipes/`) that contain those ingredients.

## Features

1. Prompt user for ingredients they have.
2. Scrape the provided website for recipe links.
3. Check each recipe page for the user-provided ingredients.
4. Display a list of recipe links that have all of the provided ingredients.

## Installation and How to Run

### Prerequisites

Ensure you have Python and the requests, time and BeautifulSoup libraries installed.

```bash
pip install requests
```

```bash
pip install time
```

```bash
pip install BeautifulSoup
```

### How to Run 

To run the script, execute the following command:

```bash
python Recipe_Scrape.py
```


Replace `<name_of_script>` with the name you've saved the script as.

## Instructions

1. When prompted, enter the first ingredient you have on hand.
2. You'll be asked if you want to enter another ingredient. If you do, type `Y` and then input the next ingredient. If not, type `N`.
3. After you've finished inputting all your ingredients, the script will search the website for recipes that contain all of the ingredients you provided.
4. Wait for the script to finish processing. The script will then display a list of recipes that match your criteria. If no recipes are found, you'll be informed accordingly.

## Dependencies

This script requires the following Python libraries:

- `requests`
- `time`
- `BeautifulSoup` from `bs4`

Please ensure you have these installed before running the script.

## Important Notes

- The script specifically looks for recipes on `https://codingnomads.github.io/recipes/`. It may not work correctly with other websites.
- The search is case-insensitive, so "SUGAR" and "sugar" will be treated the same.
- The script checks for the presence of ALL input ingredients in a recipe. If a recipe contains some but not all the ingredients, it won't be returned.

## Feedback and Contribution

For any feedback or contributions to this script, please open a pull request or raise an issue in this repository.



