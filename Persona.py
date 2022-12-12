
class Persona():
    def __init__(self,Nombre="",Edad=0,Rol=""):
        self.__nombre = Nombre
        self.__edad = Edad
        self.__rol = Rol
    def __str__(self):
        return "Nombre: {}, Edad: {}, Rol: {} ".format(self.__nombre,self.__edad,self.__rol)

    def GetNombre(self):
        return self.__nombre
    def GetEdad(self):
        return self.__edad
    def Get_Rol(self):
        return self.__rol



    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetEdad(self,edad):
        self.__edad = edad
    def SetRol(self,rol):
        self.__rol = rol
     