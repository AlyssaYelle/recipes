'''
playing around with beautiful soup to get web recipe info into a nice format for storing in db
'''


import requests
from bs4 import BeautifulSoup

# set url
url = "https://cooking.nytimes.com/recipes/1017582-zucchini-flan"

# get page data
page = requests.get(url)

# gets html content of page in parsable format
soup = BeautifulSoup(page.content, 'html.parser')




# find the recipe title
title = soup.find(class_="recipe-title").get_text().replace('\n', '').strip(' ')

print('\ntitle:\n')
print(title)



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

print('\ningredients:\n')
print(ingredients)



# parses recipe steps to get just the text from list items and puts the instructions in a list
instructions = [item.get_text().strip(' ')  for item in soup.find(class_="recipe-steps").find_all('li')]

print('\ninstructions:\n')
print(instructions)


# get recipe tags
tags = [item.get_text().strip(' ') for item in soup.find(class_='tags-nutrition-container').find_all('a')] if soup.find(class_='tags-nutrition-container') is not None else []




print('\ntags:\n')
print(tags)

# return full info as dictionary
full_recipe_info = {
    "title": title,
    "ingredients": ingredients,
    "instructions": instructions,
    "tags": tags
}

print(full_recipe_info['title'])

















