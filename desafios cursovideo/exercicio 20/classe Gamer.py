'''from rich import print
from rich.console import Group
from rich.panel import Panel

class Gamer:
    def __init__(self, name:str, nick:str) -> None:
        self.name = name
        self.nick = nick
        self.f_games = []
        
    def add_favorite(self, game:str) -> str:
        self.f_games.append(game)
        self.f_games.sort(key=str.lower)

    def sheet(self) -> str:
        content = Group(
            f'Real name: {self.name}\nFavorite games:',
            *(f'- {n}' for n in self.f_games)
            )
        
        panel = Panel(content, title=f'Player <{self.nick}>', width=56)
        print(panel)
        
g1 = Gamer('Vasco Freitas', 'Demolidor')
g1.add_favorite('Homem aranha')
g1.add_favorite('Titanic')
g1.add_favorite('anic')
g1.sheet()'''


#2ºtentativa

from rich import print
from rich.console import Group
from rich.panel import Panel

class Gamer:
    def __init__(self, name:str, nick:str) -> None:
        self.name = name
        self.nick = nick
        self.__f_games = []
        
    def favorite_games(self, add_game) -> None:
        self.__f_games.append(add_game)
        self.__f_games.sort(key=str.lower)
        
    def sheet(self) -> None:
        content = Group(
            f"Real name: {self.name}\nFavorite games:",
            *(f'- {n}' for n in self.__f_games)
            )
        
        panel = Panel(content, title=f"Player <{self.nick}>", width=55)
        print(panel)
        
g1 = Gamer('Vasco Freitas', 'Demolidor')
g1.favorite_games('Homem aranha')
g1.favorite_games('Titanic')
g1.favorite_games('Arnic')
g1.sheet()