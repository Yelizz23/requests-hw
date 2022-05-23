from pprint import pprint
import requests

intelligence_level = []

class Superhero:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        self.intellegence = int()

    def get_data(self):
        URL = f'https://superheroapi.com/api/{self.token}/search/{self.name}'
        response = requests.get(URL)
        heroes_id = dict(response.json())
        self.intellegence = heroes_id['results'][0]['powerstats']['intelligence']
        intelligence_level.append([self.intellegence, self.name])
        return self.intellegence

hero_1 = Superhero('Hulk', '2619421814940190')
hero_2 = Superhero('Captain America', '2619421814940190')
hero_3 = Superhero('Thanos', '2619421814940190')
hero_1.get_data()
hero_2.get_data()
hero_3.get_data()

def find_most_intellegent_hero():
    intelligence_level.sort()
    most_int_hero = intelligence_level[0][1]
    pprint(most_int_hero)
    return most_int_hero

find_most_intellegent_hero()