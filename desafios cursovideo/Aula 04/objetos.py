from classe import comando

'''
# Declaração de classe 
class comando:
    def __init__(self): #Método construtor
        #Atributos de Instancia
        self.formato = "quadrado"
        self.qualidade = 'novo'
        self.nome = "aquecedor"
        self.idade = 1 
        
        #Métodos de instancia
    def aniversario(self):
        self.idade += 1
        
    def qualidad(self):
        if self.idade >= 5:
            self.qualidade = 'velho'
             
            
    def mensagem(self):
        return f'O comando do/a {self.nome} tem o formato {self.formato}, é um material {self.qualidade} e tem {self.idade} anos.'
'''        
        
#Declaraçao de objeto
g1 = comando()
print(g1.mensagem())

g2 = comando()
g2.nome = 'Playstation'
g2.aniversario()
g2.formato = 'diferente'
print(g2.mensagem())

g3 = comando()
g3.idade = 4
g3.aniversario()
g3.qualidad()
print(g3.mensagem())