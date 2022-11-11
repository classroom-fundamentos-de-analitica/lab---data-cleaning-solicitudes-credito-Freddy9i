"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re
from datetime import datetime


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #eliminar nulos y duplicados
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    #Unnamed: 0 -> indice, se puede borrar
    df.drop('Unnamed: 0', inplace=True, axis=1)

    #sexo -> mayusculas y minusculas
    df.sexo = df.sexo.str.lower()
    
    #tipo de emprendimiento -> mayusculas y minusculas
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    #idea negocio -> mayusculas, minusculas y reemplazo de caracteres
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace("-"," ")
    df.idea_negocio = df.idea_negocio.str.replace("_"," ")

    #barrio -> mayusculas, minusculas y reemplazo de caracteres
    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace("-"," ")
    df.barrio = df.barrio.str.replace("_"," ")

    #comuna ciudadano -> conversion a entero
    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    #fecha de beneficio -> correccion de formatos
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    #monto del credito -> eliminacion puntos, comas, simbolo de dinero y conversion a entero
    df.monto_del_credito = df.monto_del_credito.str.replace("\.00","")
    df.monto_del_credito = df.monto_del_credito.str.replace(",","")
    df.monto_del_credito = df.monto_del_credito.str.replace("\$ ","")
    df.monto_del_credito = df.monto_del_credito.astype(int)

    #línea credito
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.str.replace("_", " ")
    df.línea_credito = df.línea_credito.str.replace("-", " ")

    #eliminar duplicados nuevamente
    df.drop_duplicates(inplace = True)

    return df