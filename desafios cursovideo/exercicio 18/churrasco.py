from rich import print
from rich.panel import Panel
from rich.console import Group

class BBQ:
    
    standard_consumption:float = 0.400
    price_kg:float = 12.49
    
    def __init__(self, name:str, quantity:int) -> None:
        self.name = name
        self.quantity = max(1, quantity)
        
    def analysis(self) -> str:
        content = Group(
            f"Analyzes {self.name} with {self.quantity} people.",
            f"Each participant will eat {BBQ.standard_consumption}kg and each 1kg costs {BBQ.price_kg}€.",
            self.__recommended_meat(),
            self.__total_price(),
            self.__price_per_person()
            )
        
        panel = Panel(content, title=self.name, width = 80)
        print(panel)
    
    def __recommended_meat(self) -> str:
        self.kg_total = self.quantity * BBQ.standard_consumption
        return f"Recommended [green] buy {self.kg_total:.3f}kg [/green] of meat."
    
    def __total_price(self) -> str:
        self.costs_total = self.kg_total * BBQ.price_kg
        f_price = f"{self.costs_total:.2f}".replace(".",",")
        return f"The total costs [blue]will be {f_price}€[/blue]"
    
    def __price_per_person(self) -> str: 
        price_person = self.costs_total / self.quantity
        f_price = f"{price_person:.2f}€".replace(".",",")
        return f"Each person will buy [yellow]{f_price}[/yellow] for participate."
    
b1 = BBQ('Churrasco com amigos', 4)
b1.analysis()