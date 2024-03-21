import requests


class Hp:
    """HP Class"""

    def __init__(self):
        self.api_url = "https://hp-api.onrender.com/api/"

    def getCharacters(self, service="characters/") -> list:
        """getCharacters"""
        response = requests.get(self.api_url + service, params={}, timeout=10)

        if response.status_code == 200:
            data = response.json()

        names = []
        for item in data:
            names.append(item["name"])

        return names

    def getCharacter(self, service="character/", characterId=None) -> list:
        """getCharacters"""
        api_call = self.api_url + service + characterId
        response = requests.get(api_call, params={}, timeout=10)

        if response.status_code == 200:
            data = response.json()

        return data[0]
