import requests
from bs4 import BeautifulSoup
import csv

#User-Agent header tells site what kind of client is making a apckaged request, header makes our bot look more legit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://www.allrecipes.com/recipe/204133/old-fashioned-potato-kugel/')
soup = BeautifulSoup(page.text, 'html.parser')

csv_file = open('ingredients.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Ingredients', 'Instructions', 'Macros'])

# match = soup.title.text
ingredients_list_block = soup.find('ul', class_='mm-recipes-structured-ingredients__list')

if (ingredients_list_block):
    items = ingredients_list_block.find_all('li')
    print("Line 17")
    # print("items size: %d\n" (len(items)))
    ingredient_list = []
    for item in items:
        parts = item.find_all('span')
        ingredient = ' '.join(part.get_text(strip=True) for part in parts)
        ingredient_list.append(ingredient)
    print(ingredient_list)
    csv_writer.writerow(["Name", ingredient_list, 'Instructions', 'Macros'])
        
else:
    print("Ingredients list not found")

csv_file.close()


# print(soup.prettify());