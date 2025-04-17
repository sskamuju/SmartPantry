import requests
from bs4 import BeautifulSoup

#User-Agent header tells site what kind of client is making a apckaged request, header makes our bot look more legit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://www.allrecipes.com/recipe/204133/old-fashioned-potato-kugel/')
soup = BeautifulSoup(page.text, 'html.parser')

