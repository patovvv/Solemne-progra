from Persona import Persona
from random import randint
#from Main import listadoc
lgrado=["Licenciado","Magiser","Doctorado"]
ltipo=["Adjunto","Regular"]
class Docente(Persona):
    def __init__(self, Nombre="", Edad=0,Rol="Docente",Sueldo=0,Grado="",Tipo=""):
        super().__init__(Nombre, Edad,Rol)
        self.__sueldo = Sueldo
        self.__grado=Grado
        self.__tipo=Tipo

    def __str__(self):
        return super().__str__() + "Sueldo: {}, Grado: {}, Tipo: {}".format(self.__sueldo,self.__grado,self.__tipo)
    
    def GetSueldo(self):
        return self.__sueldo
    
    def SetSueldo(self,Sueldo):
        self.__sueldo = Sueldo

    def SetGrado(self,Grado):
        self.__grado=Grado

    def Grado(self):
        a=randint(0,2)
        grdo=lgrado[a]
        self.SetGrado(grdo)

    def GetGrado(self):
        self.Grado()
        return self.__grado

    def Tipo(self):
        a=randint(0,1)
        tipo=ltipo[a]
        self.SetTipo(tipo)

    def GetTipo(self):
        self.Tipo()
        return self.__tipo
    
    def SetTipo(self,Tipo):
        self.__tipo=Tipo
