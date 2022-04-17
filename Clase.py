class Humano(): 
    def __init__(self,nacionalidad, age, name,pet):
        self.nacionalidad=nacionalidad
        self.age = age 
        self.name = name 
        self.pet = pet
    def Info (self):
        description = ("Nacionalidad:{}\nname de especie:{}\nage:{}") 
        print(description.format(self.nacionalidad,self.name, self.age)) 

    def Asignar (self,pet):
        self.pet=pet
        print ("{} Se le ha asignado la mascota {}".format(self.name,self.pet))


class Animal():
    def __init__(self,tipo,raza,age,name,owner):
        self.tipo=tipo
        self.raza=raza
        self.age=age
        self.name=name
        self.owner=owner
    def Info (self):
        description = ("Tipo:{}\nRaza:{}\nname de especie:{}\nage:{}") 
        print(description.format(self.tipo,self.raza,self.name, self.age))
    def Asignar (self,owner):
        self.owner=owner
        print("El dueño de la mascota {} es {}".format(self.name,self.owner))

        

def callInfo(x):
    x.Info()
