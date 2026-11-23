class Fav:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.__favorites_things = {}
        
    def fav_things(self, program, content) -> None:
        
        self.__favorites_things[program] = content
        self.dict_organized = dict(sorted(self.__favorites_things.items()))
        
    def sheet(self) -> None:
        print(f'Name: {self.name}\nYour age: {self.age}\n\nFavorite things:')
        
        if not self.dict_organized:
            print(f'No items were recorded!')
        else:
            self.dict_organized = dict(sorted(self.__favorites_things.items()))
            for x,y in self.dict_organized.items():
                print(f'{x}: {y}')
            
f1 = Fav('Vasco', 21)
f1.fav_things('Music', 'None')
f1.fav_things('Film', 'Homem aranha')
f1.sheet()