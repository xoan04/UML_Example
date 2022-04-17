from pickle import NONE
from Clase import Humano,Animal,callInfo


if __name__ == "__main__":

    print("\nPERSONA""\n")
    Persona1=Humano("Colombiano",20,"Juan",NONE)
    callInfo(Persona1)
    print("\nANIMAL\n")
    Animal1=Animal("Oso","Panda Rojo",5,"Turing",NONE)
    callInfo(Animal1)

    print("\nASIGNAR MASCOTA")
    Persona1.Asignar(Animal1.name)

    Animal1.Asignar(Persona1.name)
