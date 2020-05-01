import requests
from bs4 import BeautifulSoup

def prep_soup(url):

    # get page data
    page = requests.get(url)

    # gets html content of page in parsable format
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup




def scrape(soup):

    # find the recipe title
    title = scrape_title(soup)

    # find the ingredient information
    ingredients = scrape_ingredients(soup)

    # find the instructions
    instructions = scrape_instructions(soup)

    # find the tags
    tags = scrape_tags(soup)

    # return full info as dictionary
    full_recipe_info = {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions,
        "tags": tags
    }

    return full_recipe_info


def scrape_title(soup):

    # find the recipe title
    title = soup.find(class_="recipe-title").get_text().replace('\n', '').strip(' ')

    return title


def scrape_ingredients(soup):

    # find list items for ingredients list
    ingredients_list = soup.find('ul', class_="recipe-ingredients").find_all('li')


    # load each ingredient into list
    ingredients = []
    for item in ingredients_list:

        # separate out quantity, ingredient name, ingredient details
        quantity = item.find(class_="quantity").get_text().replace('\n', '').strip(' ')
        ingredient = item.find(class_="ingredient-name").get_text().replace('\n', '').strip(' ').split(',')
        ingredient_name = ingredient[0]
        ingredient_details = ''.join(ingredient[1:]) if len(ingredient) > 1 else ''


        ingredients.append([quantity, ingredient_name, ingredient_details])

    return ingredients


def scrape_instructions(soup):

    # parses recipe steps to get just the text from list items and puts the instructions in a list
    instructions = [item.get_text().strip(' ')  for item in soup.find(class_="recipe-steps").find_all('li')]

    return instructions



def scrape_tags(soup):

    # get recipe tags
    tags = [item.get_text().strip(' ') for item in soup.find(class_='tags-nutrition-container').find_all('a')] if soup.find(class_='tags-nutrition-container') is not None else []

    return tags










