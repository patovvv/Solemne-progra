import pandas as pd
from random import randint
df=pd.read_csv("Solemne03.csv")
lista=[]
a=len(df)
for i in range(a):#agrega de forma aleatoria docente o estudiante
    b=randint(0,1)
    if b==0:
        lista.append("Docente")
    if b==1:
        lista.append("Estudiante")        
df["Profesion"]=lista#se agrega columna "Profesion" con los datos de lista
d1=df[(df["Nombres"]!="TRUE")&(df["Nombres"]!="FALSE")&(df["Edad"]>0)&(df["Edad"]<120)].dropna()#elimina nan,booleanos y edades fuera de rango
d2=d1.sort_values(by=["Nombres","Sueldo"])#reordena de forma creciente la muestra d1 segun su nombre y sueldo
d3=d2.drop_duplicates(subset=["Nombres"],keep="last")#elimina duplicados de cada nombre dejando el sueldo mas alto
print(d3)
print("")
print(len(d3)," datos")
