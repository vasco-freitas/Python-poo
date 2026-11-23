# Declaração de classe 
class comando:
    """
    Esta classe cria o estado de um comando, que tem formato, qualidade, nome e idade.
    
    Para criar um novo comando use
    variavel = comando(f= , q= ,n= , i=)
    """
    def __init__(self, f = '', q = '', n = '', i = 0): #Método construtor
        #Atributos de Instancia
        self.formato = f
        self.qualidade = q
        self.nome = n
        self.idade = i 
        
        #Métodos de instancia
    def aniversario(self):
        self.idade += 1
        
    def qualidad(self):
        if self.idade >= 5:
            self.qualidade = 'velho'
             

    def __str__(self):
        return f'O comando do/a {self.nome} tem o formato {self.formato}, é um material {self.qualidade} e tem {self.idade} anos.'

    def __getstate__(self):
        return f'Nome: {self.nome}   Idade: {self.idade}   qualidade: {self.qualidade}  '
#Declaraçao de objeto
g1 = comando(f= "quadrado",q= "novo", n="aquecedor",i=1)
print(g1)
print(g1.__getstate__())

g2 = comando(f="diferente", q= "novo",n = "Playstation",i=1)
g2.aniversario()
print(g2)

g3 = comando(f = "quadrado", q = "novo",n="aquecedor",i=4)
g3.aniversario()
g3.qualidad()
print(g3)

g4 = comando()
print(g4)


#help(comando)