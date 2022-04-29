#EJERCICIO 22: dado el archivo denominado Pokemon.csv que contiene datos sobre pokemones,
# se desea generar una función que retorne los nombres de los pokemones de la generación 1 (Generation)
#que tengan igual vaor de ataque y defensa ((Attack y Defense).


#imports de csv y os
import csv
import os

#creacion de ruta y apertura de csv
path_files = "Pokemon.csv"
archivo = open(os.path.join(os.getcwd(), path_files), "r", encoding="utf-8")

pokedex = csv.reader(archivo, delimiter=',')
header, datos = next(pokedex), list(pokedex)

#obtengo el numero de la posicion de Attack, Defense y Name en el header y creo lista de nombres de pkemones
pos_attack = header.index("Sp. Atk")
pos_defense = header.index("Sp. Def")
pos_name = header.index("Name")
pos_generation = header.index("Generation")
nom_pok = []



#-------------------------------------------COD 1-------------------------------------------------------------------------------
# a -> OBTIENE LA LISTA SOLO CON NONE
#el ejercicio termina con 2 estructuras a y nom_pok

#si los valores de ataque y defensa son iguales se añade a la nueva lista

def imprime_añade(x,pos_name,pos_defense,pos_attack, pos_generation, nom_pok):
    if ("1" in x[pos_generation]) and (x[pos_attack] == x[pos_defense]):
        print(x[pos_name])
        nom_pok.append(x[pos_name])


a = list(map(lambda x :imprime_añade(x,pos_name,pos_defense,pos_attack, pos_generation, nom_pok), datos))
# a -> [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
# nom_pok -> tiene la lista con todos los nombres bien



#---------------------------------------COD 2-----------------------------------------------------------------------------------
# a -> OBTIENE LA LISTA CON EL NOMBRE Y NONE, AUNQUE LA FUNCION ME RETORNE EL NOMBRE DEL POKEMON QUE CUMPLA CON LA CONDICION

#si los valores de ataque y defensa son iguales se añade a la nueva lista

#def imprime_añade(x,pos_name,pos_defense,pos_attack, pos_generation):
#    if ("1" in x[pos_generation]) and (x[pos_attack] == x[pos_defense]):
#        print(x[pos_name])
#        return x[pos_name]

#a = list(map(lambda x :imprime_añade(x,pos_name,pos_defense,pos_attack, pos_generation), datos))
# a-> ['Bulbasaur', 'Ivysaur', 'Venusaur', None, None, None, None, None, None, None, None, None, None, 'Caterpie', 'Metapod'......]



#---------------------------------------COD 3-----------------------------------------------------------------------------------
# impresion con for / if
"""for pokemon in datos:
  if ("1" in pokemon[pos_generation]) and (pokemon [8] == pokemon[9]):
    print (f"{pokemon[1]}")"""


#----------------------------------------COD 4------------------------------------------------------------------------------------
#mapeo de datos con -> append if condicion else none

#a = list(map(lambda x: nom_pok.append(x[pos_name]) if (x[pos_attack] == x[pos_defense]) else None, datos))

#a -> [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,......]
#--> creeeo que es todo none xq el lambda nunca recibe el true, y por defecto al map le devuelve un none??
#nom_pok -> tiene agregados todos los elementos


#-------------------------------------------COD 5------------------------------------------------------------------------------------
#filtra la lista buscando si el ataque y defensa son iguales

#a = list(filter(lambda x: (x[pos_attack] == x[pos_defense]), datos))

# a -> devuelve todos los pokemones que cumplen la condicion, pero con todos sus datos(solo necesito nombre)


print(a)
#print(nom_pok)

#cierre del archivo
archivo.close()