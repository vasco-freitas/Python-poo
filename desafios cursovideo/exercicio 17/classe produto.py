from rich import print
from rich.panel import Panel
from rich.console import Group
from rich.align import Align
from rich.rule import Rule 
from rich.text import Text

class Product:
    
    title = 'Product'
    
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
        
    def label(self) -> str:
        
        preco_normal = Text(f"{self.price:,.2f}€", style="default")
        
        content = Group(
            Align.center(f'{self.name:^20}'),
            Rule(style = 'bold red', characters = '-'),
            Rule(preco_normal,style='bold green', characters='-')
            )
        
        panel = Panel(content, title = Product.title, expand = False)
        print(panel)
        
p1 = Product('Iphone 17', 2)
p1.label()