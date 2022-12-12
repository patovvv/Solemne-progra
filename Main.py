import pandas as pd
import numpy as np
from random import *
from Estudiante import *
from Docente import *

def CargarArchivo():
    global df
    df=pd.read_csv("Solemne03.csv")
    print("Archivo cargado correctamente")
    print(" ")
CargarArchivo()
def FiltradoDeDatos():
    global d3
    lista_random=[]
    for i in range(len(df)):#agrega de forma aleatoria docente o estudiante
        b=randint(0,1)
        if b==0:
            lista_random.append("Docente")
        if b==1:
            lista_random.append("Estudiante")        
    df["Profesion"]=lista_random#se agrega columna "Profesion" con los datos de lista

    d1=df[(df["Nombres"]!="TRUE")&(df["Nombres"]!="FALSE")&(df["Edad"]>0)&(df["Edad"]<120)].dropna()
    d2=d1.sort_values(by=["Nombres","Sueldo"])
    d3=d2.drop_duplicates(subset=["Nombres"],keep="last")

FiltradoDeDatos()

def SepararDatos():
    global estudiantefinal
    global docentefinal
    d3.set_index("Profesion",inplace=True)
    d4=d3.loc["Docente"]
    listadoc=d4.to_numpy().tolist()
    #dfdoc0=pd.DataFrame(listadoc)

    dicciodc={0:"Nombre",1:"Edad",2:"Sueldo"}
    #dfdoc1=(dfdoc0.rename(columns=dicciodc))
    listadoc1=[]
    listbigdoc=[]
    for i in range(len(listadoc)):
            obj_doc = Docente()
            obj_doc.Set_Nombre(listadoc[i][1])
            obj_doc.Set_Edad(listadoc[i][2])
            obj_doc.Set_Sueldo(listadoc[i][3])
            listadoc1.append(obj_doc)

    for i in range(len(listadoc1)):
        listsmalldoc=[]
        listsmalldoc.append(listadoc1[i].Get_Nombre())
        listsmalldoc.append(listadoc1[i].Get_Edad())
        listsmalldoc.append(listadoc1[i].Get_Sueldo())
        listbigdoc.append(listsmalldoc)

    df_final_doc= pd.DataFrame(listbigdoc)
    docentefinal=df_final_doc.rename(columns=dicciodc)
    print(docentefinal)
    #docentefinal.to_excel("Datos de docentes.xlsx",engine="openpyxl")

    print("----------")

    d5=d3.loc["Estudiante"]
    listaest=d5.to_numpy().tolist()
    listaest1=[]
    listbigest=[]
    for i in range(len(listaest)):
            objest= Estudiante()
            objest.Set_Nombre(listaest[i][1])
            objest.Set_Edad(listaest[i][2])
            objest.SetNota1(objest.GetNota1())
            objest.SetNota2(objest.GetNota2())
            objest.SetPromedio(objest.GetPromedio())
            objest.SetAsistencia(objest.GetAsistencia())
            objest.Aprobo()
            listaest1.append(objest)
    for i in range(len(listaest)):
        listsmallest =[]
        listsmallest.append(listaest1[i].Get_Nombre())
        listsmallest.append(listaest1[i].Get_Edad())
        listsmallest.append(listaest1[i].GetNota1())
        listsmallest.append(listaest1[i].GetNota2())
        listsmallest.append(listaest1[i].GetPromedio())
        listsmallest.append(listaest1[i].GetAsistencia())
        listsmallest.append(listaest1[i].GetAprobado())
        listbigest.append(listsmallest)

    diccioest={0:"Nombres", 1:"Edad", 2:"Nota 1", 3:"Nota 2",4:"Promedio",5:"Asistencia",6:"Aprobacion"}
    df_final_est=pd.DataFrame(listbigest)
    estudiantefinal=df_final_est.rename(columns=diccioest)
    estudiantefinal.to_excel("Datos de estudiantes.xlsx",engine="openpyxl")
SepararDatos()
print(estudiantefinal)




