import requests
from bs4 import BeautifulSoup

def get_soup():
    pokemon_name = input("Enter the name of a pokemon: ")
    result = requests.get(f"https://bulbapedia.bulbagarden.net/wiki/{pokemon_name}_(Pok%C3%A9mon)")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    return soup

def get_num():
    soup = get_soup()
    table = soup.find('table', attrs={'class':'roundy'})
    data = table.find('th')
    pokedex_number = data.text.strip()
    return pokedex_number

print(f"Pokedex number: {get_num()}")
