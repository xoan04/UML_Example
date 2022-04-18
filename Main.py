from pickle import NONE
from Clase import Humano,Animal,callInfo,callAsignar


if __name__ == "__main__":

    print("\nPERSONA""\n")
    Persona1=Humano("Colombiano",20,"Juan","Ninguna")
    callInfo(Persona1)

    print("\nANIMAL\n")
    Animal1=Animal("Oso","Panda Rojo",5,"Turing","Ninguno")
    callInfo(Animal1)
    print("\n\n")
    callAsignar(Persona1,Animal1.name)
    callAsignar(Animal1,Persona1.name)
    print("YA TENGO MASCOTA D:")
    callInfo(Persona1)
    print("Ya tengo Dueño")
    callInfo(Animal1)
