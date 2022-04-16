class Humano(): 
    def __init__(self,nacionalidad, edad, nombre):
        self.nacionalidad=nacionalidad
        self.edad = edad 
        self.nombre = nombre 
    def Info (self):
        description = ("Nacionalidad:{}\nNombre de especie:{}\nEdad:{}") 
        print(description.format(self.nacionalidad,self.nombre, self.edad)) 




class Animal():
    def __init__(self,tipo,raza,edad,nombre):
        self.tipo=tipo
        self.raza=raza
        self.edad=edad
        self.nombre=nombre
    def Info (self):
        description = ("Tipo:{}\nRaza:{}\nNombre de especie:{}\nEdad:{}") 
        print(description.format(self.tipo,self.raza,self.nombre, self.edad))

        



def callInfo(x):
    x.Info()
