import pandas as pd
import numpy as np
from random import *
from Estudiante import *
from Docente import *

def CargarArchivo():
    global df
    df=pd.read_csv("Solemne03.csv")
    print(" ")

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



def SepararDatos():
    global estudiantefinal
    global docentefinal
    d3.set_index("Profesion",inplace=True)
    d4=d3.loc["Docente"]
    listadoc=d4.to_numpy().tolist()
    #dfdoc0=pd.DataFrame(listadoc)

    dicciodc={0:"Nombre",1:"Edad",2:"Sueldo",3:"Grado",4:"Tipo"}
    #dfdoc1=(dfdoc0.rename(columns=dicciodc))
    listadoc1=[]
    listbigdoc=[]
    for i in range(len(listadoc)):
            obj_doc = Docente()
            obj_doc.SetNombre(listadoc[i][1])
            obj_doc.SetEdad(listadoc[i][2])
            obj_doc.SetSueldo(listadoc[i][3])
            listadoc1.append(obj_doc)

    for i in range(len(listadoc1)):
        listsmalldoc=[]
        listsmalldoc.append(listadoc1[i].GetNombre())
        listsmalldoc.append(listadoc1[i].GetEdad())
        listsmalldoc.append(listadoc1[i].GetSueldo())
        listsmalldoc.append(listadoc1[i].GetGrado())
        listsmalldoc.append(listadoc1[i].GetTipo())
        listbigdoc.append(listsmalldoc)

    df_final_doc= pd.DataFrame(listbigdoc)
    docentefinal=df_final_doc.rename(columns=dicciodc)
    docentefinal.to_excel("Datos de docentes.xlsx",engine="openpyxl")

    print("----------")

    d5=d3.loc["Estudiante"]
    listaest=d5.to_numpy().tolist()
    listaest1=[]
    listbigest=[]
    for i in range(len(listaest)):
            objest= Estudiante()
            objest.SetNombre(listaest[i][1])
            objest.SetEdad(listaest[i][2])
            objest.SetNota1(objest.GetNota1())
            objest.SetNota2(objest.GetNota2())
            objest.SetPromedio(objest.GetPromedio())
            objest.SetAsistencia(objest.GetAsistencia())
            objest.Aprobo()
            listaest1.append(objest)
    for i in range(len(listaest)):
        listsmallest =[]
        listsmallest.append(listaest1[i].GetNombre())
        listsmallest.append(listaest1[i].GetEdad())
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




while True:
    try:
        print(" ")
        print("Sistema de datos\n\n\n")
        print('1.Visualizar archivo csv original\n\n2.Imprimir listas de estudiantes y docentes(limpias)\n\n3.Finalizar programa')
        opcion=int(input('\nOpcion: '))
        if opcion==1:
            CargarArchivo()
            print(df)
        if opcion==2:
            CargarArchivo()
            FiltradoDeDatos()
            SepararDatos()
            print("Docentes:")
            print(" ")
            print(docentefinal)
            print("----------------")
            print("Estudiantes:")
            print(estudiantefinal)
            print(" ")
        if opcion==3:
            print("Saliendo del sistema...")
            print(" ")
    except:
        print("Ingrese solo numero segun las opciones mostradas...")