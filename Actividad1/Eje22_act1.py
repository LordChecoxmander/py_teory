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

#si los valores de ataque y defensa son iguales se añade a la nueva lista
def imprime_añade(x,pos_name,pos_defense,pos_attack, pos_generation):
    if ("1" in x[pos_generation]) and (x[pos_attack] == x[pos_defense]):
        print(x[pos_name])
        nom_pok.append(x[pos_name])

a = list(map(lambda x :imprime_añade(x,pos_name,pos_defense,pos_attack, pos_generation), datos))

"""for pokemon in datos:
  if ("1" in pokemon[pos_generation]) and (pokemon [8] == pokemon[9]):
    print (f"{pokemon[1]}")"""


#a = list(map(lambda x: nom_pok.append(x[pos_name]) if (x[pos_attack] == x[pos_defense]) else None, datos))

#a = list(filter(lambda x: (x[pos_attack] == x[pos_defense]), datos))
#print(a)
#print(nom_pok)

#cierre del archivo
archivo.close()