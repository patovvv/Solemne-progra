from Persona import Persona
#from Main import listadoc
class Docente(Persona):
    def __init__(self, Nombre="", Edad=0,Rol="Docente",Sueldo=0):
        super().__init__(Nombre, Edad,Rol)
        self.__sueldo = Sueldo

    def __str__(self):
        return super().__str__() + "Sueldo: {}".format(self.__sueldo)
    
    def Get_Sueldo(self):
        return self.__sueldo
    
    def Set_Sueldo(self,Sueldo):
        self.__sueldo = Sueldo

