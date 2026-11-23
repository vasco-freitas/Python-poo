class person:
    def __init__(self, name:str , age:int, height:float) -> None:
        self.name = name
        self.age = age
        self.__height = height
    
    def presentation(self) -> None:
        print(f"Hello! My name is {self.name} and i'm {self.age} years old!")
        self.__height_size()
    
    def __height_size(self) -> None:
        print(f"My height is {self.__height}")
    
p1 = person('Vasco',21,1.71)
p1.presentation()
