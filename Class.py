class Operaciones:

    def __init__(self, num1 , num2): #Es constructor,y Self es como es this
        self.num1 = num1
        self.num2 = num2
    def suma(self):
        return self.num1+self.num2
    def resta(self):
        return self.num1-self.num2

# Ahora instanciamos

Op = Operaciones(5,4) #Aqui instanciamos y enviamos parametros
print (Op.suma())
print (Op.resta())
