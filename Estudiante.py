from Persona import Persona
from random import randint
class Estudiante(Persona):
    def __init__(self, Nombre="---", Edad=0, Rol="Estudiante",Asistencia=0,Nota1=0,Nota2=0,Promedio=0,Aprueba=""):
        super().__init__(Nombre, Edad, Rol)
        self.__asistencia=Asistencia
        self.__nota1=Nota1
        self.__nota2=Nota2
        self.__promedio=Promedio
        self.__aprueba=Aprueba
    def __str__(self):
        return super().__str__()+"Asisistencia: {}, Nota 1: {}, Nota 2: {}, Promedio: {}, Aprueba: {}".format(self.GetAsistencia(),self.GetNota1(),self.GetNota2(),self.GetPromedio(),self.GetAprobado())
    
    def GetAsistencia(self):
        a=str(randint(50,100))
        asistencia=a+"%"
        self.__asistencia=asistencia
        return self.__asistencia
    
    def GetNota1(self):
        if self.__nota1 == 0:
            a=(randint(10,70))
            self.__nota1=a
            return self.__nota1
        else:
            return self.__nota1
    def GetNota2(self):
        if self.__nota2 ==0:
            a=(randint(10,70))
            self.__nota2=a
            return self.__nota2
        else:
            return self.__nota2
        
    def GetPromedio(self):
        self.__promedio=(self.GetNota1()+self.GetNota2())/2
        return self.__promedio
    
    def SetPromedio(self,Promedio):
        self.__promedio=Promedio
    
    def SetAsistencia(self,Asistencia):
        self.__asistencia=Asistencia

    def SetNota1(self,Nota1):
        self.__nota1=Nota1

    def SetNota2(self,Nota2):
        self.__nota2=Nota2
    
    def Aprobo(self):
        if self.GetPromedio()>=40:
            self.SetAprobado("Aprobado")
        
        elif self.GetPromedio()<40:
            self.SetAprobado("Reprobado")
            
        else:
            pass
        
    def GetAprobado(self):
        self.Aprobo()
        return self.__aprueba
    
    def SetAprobado(self,Aprueba):
        self.__aprueba=Aprueba
    
