
#INTENTO EJERCICIO 3

import csv
from Pokemon import pokemon

def datos_entrenadores(coach_1_pokemons,csv):           #Funcion para leer los datos de los entrenadores
    pokemons_entrenador1 = []
    with open("coach_1_pokemons.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            ID = row[0]
            nombre = row[1]
            arma = row[2]
            salud = row[3]
            ataque = row[4]
            defensa = row[5]
            p = pokemon(ID, nombre, arma, salud, ataque, defensa)
            pokemons_entrenador1.append(p)
    
    pokemons_entrenador2 = []
    with open("coach_2_pokemons.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            ID = row[0]
            nombre = row[1]
            arma = row[2]
            salud = row[3]
            ataque = row[4]
            defensa = row[5]
            p = pokemon(ID, nombre, arma, salud, ataque, defensa)
            pokemons_entrenador2.append(p)

    return pokemons_entrenador1 and pokemons_entrenador2

def elegir_pokemon(pokemon):    #Funcion para elegir el pokemon
    print("Pokemon disponibles: ")
    for i, p in enumerate(pokemon):
        print(f"{i+1}. {p.get_nombre()} (salud: {p.get_salud()})")

    while True:
        try:
            opcion = int(input("Elige un pokemon: "))
            if opcion < 1 or opcion > len(pokemon):
                print("Opcion inválida")
            else:
                return pokemon[opcion-1]
        except ValueError:
            print("Opcion inválida.")

def entrenador_jugando(entrenador):
    for p in entrenador:
        if p.vivo():
            return True
    return False

def main():
    entrenador1 = datos_entrenadores('coach_1_pokemons.csv', csv)
    entrenador2 = datos_entrenadores('coach_2_pokemons.csv', csv)

    jugando_entrenador1 = entrenador1[0]
    jugando_entrenador2 = entrenador2[0]

    print(f"El entrenador 1 ha elegido a {jugando_entrenador1.get_nombre()}")
    print(f"El entrenador 2 ha elegido a {jugando_entrenador2.get_nombre()}")



    while True:
        if not entrenador_jugando(entrenador1):
            print("El entrenador 2 ha ganado")
            break
        if not entrenador_jugando(entrenador2):
            print("El entrenador 1 ha ganado")
            break

if __name__ == "__main__":
    main()


