class Humano(): 
    def __init__(self,nacionalidad, age, name,pet):
        self.nacionalidad=nacionalidad
        self.age = age 
        self.name = name 
        self.pet = pet
    def Info (self):
        description = ("Nacionalidad:{}\nNombre{}\nEdad:{}\nMascota:{}") 
        print(description.format(self.nacionalidad,self.name, self.age,self.pet)) 

    def Asignar (self,animal):
        self.animal=animal
        self.pet=animal



class Animal():
    def __init__(self,tipo,raza,age,name,owner):
        self.tipo=tipo
        self.raza=raza
        self.age=age
        self.name=name
        self.owner=owner
    def Info (self):
        description = ("Tipo:{}\nRaza:{}\nname de especie:{}\nage:{}\nDueño:{}") 
        print(description.format(self.tipo,self.raza,self.name, self.age,self.owner))
    def Asignar (self,dueño):
        self.dueño=dueño
        self.owner=dueño

        

def callInfo(x):
    x.Info()

def callAsignar(x,d):
    x.Asignar(d)