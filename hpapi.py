import requests
from pprint import pprint as pp

class Hp(object):
    """HP Class"""

    def __init__(self):
        self.api_url = "https://hp-api.onrender.com/api/"

    def test(self) -> str:
        """ test method """

        response = requests.get(self.api_url + "characters/", params={}, timeout=10, verify=False)

        if response.status_code == 200:
            data = response.json()

        print("----- DATA ------")
        pp(data)
        return data

    def get_characters(self) -> list:
        """getCharacters"""
        response = requests.get(self.api_url + "characters/", params={}, timeout=10, verify=False)

        if response.status_code == 200:
            data = response.json()
        
        # names = []
        # for item in data:
        #     names.append(item["actor"])
        
        # pp(names)

        return data

    def get_character(self, service="character/", characterId=None) -> list:
        """getCharacters"""
        api_call = self.api_url + 'character/' + '484d89aa-5d22-4d4d-9e07-4913cf8d4d20'
        response = requests.get(api_call, params={}, timeout=10, verify=False)

        if response.status_code == 200:
            data = response.json()

        return data[0]
