

import csv

#Entrenador 1 
import csv 
with open('coach_1_pokemons.csv', 'r') as file: 
    datos=file.readlines()      #Leer el archivo csv
    datos.pop(0)                #Eliminar la primera linea del archivo csv
    datos_coach1=[]             #Convertir datos a lista de listas
    for i in datos: 
        pokemon=i.strip().split(',') 
        datos_coach1.append(pokemon) 
    
#Entrenador 2
with open('coach_2_pokemons.csv', 'r') as file:
    datos=file.readlines()
    datos.pop(0)
    datos_coach2=[]
    for i in datos:
        pokemon=i.strip().split(',')
        datos_coach2.append(pokemon)

#Printear datos de los entrenadores
def presentaciones():
    print(f"-----Entrenador 1:-----"
        f"{datos_coach1}\n")
    print(f"-----Entrenador 2:-----"
        f"{datos_coach2}\n")
