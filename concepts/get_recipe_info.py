import requests
from bs4 import BeautifulSoup

# set url
#url = "https://cooking.nytimes.com/recipes/1019944-vegan-broccoli-soup-with-cashew-cream"
url = 'https://cooking.nytimes.com/recipes/1017310-butter-stewed-radishes'


# get page data
page = requests.get(url)

# gets html content of page in parsable format
soup = BeautifulSoup(page.content, 'html.parser')


# find the recipe title
title = soup.find(class_="recipe-title").get_text().replace('\n', '').strip(' ')
#print(title)


# parses recipe steps to get just the text from list items and puts the instructions in a list
instructions = [item.get_text().strip(' ')  for item in soup.find(class_="recipe-steps").find_all('li')]

# for step in steps:
#     print(step)


# find list items for ingredients list
ingredients_list = soup.find('ul', class_="recipe-ingredients").find_all('li')

#print(ingredients_list)

ingredients = []
for item in ingredients_list:
    quantity = item.find(class_="quantity").get_text().replace('\n', '').strip(' ')
    ingredient = item.find(class_="ingredient-name").get_text().replace('\n', '').strip(' ').split(',')
    ingredient_name = ingredient[0]
    ingredient_details = ingredient[1:] if len(ingredient) > 1 else ''


    ingredients.append([[quantity], [ingredient_name], [ingredient_details]])

# for ingredient in ingredients:
#     print(ingredient[0], ingredient[1])

# get recipe tags
tags = [item.get_text().strip(' ') for item in soup.find(class_='tags-nutrition-container').find_all('a')]
#print(tags)

my_recipe = {
    "title": title,
    "ingredients": ingredients,
    "instructions": instructions,
    "tags": tags
}

print(my_recipe)















