from rich import print
from rich.text import Text

class Employee:
    
    company = "Ámandio Carvalho"
    
    def __init__(self, name:str, industry:str, position:str) -> None:
        self.name = name
        self.industry = industry
        self.position = position
        
    def presentation(self) -> str:
        return f"Hello, i'm [bold blue]{self.name}[/bold blue] and i'm a {self.industry} in the sctor {self.position} of the company {Employee.company}."
    
#Employee.company = "Ámandio Carvalh"
    
e1 = Employee('Vasco','Programador','TI')
e1.position = 'Choque'
print(e1.presentation())

e2 = Employee('Vasco','Programador','TI')
print(e2.presentation())