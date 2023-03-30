
#EJERCICIO 1 (till line 142) Y EJERCICIO 2 (till end of file)

#ACTIVIDAD 1 

#clase para pokemon
class pokemon():

    id = []
    max_salud = 100
    min_salud = 1
    max_ataque = 10
    min_ataque = 1
    max_defensa = 10
    min_defensa = 1

    def __init__(self, ID, nombre, arma, salud, defensa, ataque):
        armas = ["puñetazo", "patada", "codazo", "cabezazo"]

        #Comprobación de errores
        if arma not in armas:
            print("El arma del pokemon debe ser una arma ya creada (puñetazo, patada, codazo, cabezazo).")
        if not isinstance(salud, int) or not (self.min_salud <= salud <= self.max_salud):
            print("La salud del pokemon debe ser un entero entre 1 y 100.")
        if not isinstance(ataque, int) or not (self.min_ataque <= ataque <= self.max_ataque):
            print("El ataque del pokemon debe ser un entero entre 1 y 10.")
        if not isinstance(defensa, int) or not (self.min_defensa <= defensa <= self.max_defensa):
            print("La defensa del pokemon debe ser un entero entre 1 y 10.")
        if          ID in pokemon.id:
            print("El ID del pokemon debe ser unico.")

        self.ID = ID
        self.nombre = nombre
        self.arma = arma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        pokemon.id.append(ID)
    
    #Destructor
    def __del__(self):
        print(f"El pokemon {self.nombre} ha sido eliminado.")

    #Printear datos
    def __str__(self):              
        return f"El pokemon con ID {self.ID} y nombre {self.nombre} tiene como arma {self.arma.name} y salud {self.salud}."
    
    #def getter y setter
    def get_ID(self):               
        return self.ID
    
    def get_nombre(self):
        return self.nombre
    
    def get_arma(self):
        return self.arma
    
    def get_salud(self):
        return self.salud
    
    def set_salud(self, salud):
        if salud >= 0 and salud <= 100:
            self.salud = salud
        else:
            print("No se puede cambiar la salud.")
    
    def get_ataque(self):
        return self.ataque
    
    def set_ataque(self, ataque):
        if ataque >= 1 and ataque <= 10:
            self.ataque = ataque
        else:
            print("No se puede cambiar el ataque.")
    
    def get_defensa(self):
        return self.defensa
    
    def set_defensa(self, defensa):
        if defensa >= 1 and defensa <= 10:
            self.defensa = defensa
        else:
            print("No se puede cambiar la defensa.")

    #Comprobar si el pokemon esta vivo
    def vivo(self):               
        if self.salud > 0:
            return True
        else:
            return False
        
    #Daño de cada arma
    def daño_arma(self):
        if self.arma == "puñetazo":
            return 4
        elif self.arma == "patada":
            return 3
        elif self.arma == "codazo":    
            return 2
        elif self.arma == "cabezazo":
            return 1 

    #Atacar a otro pokemon
    def atacar(self, pokemon, pokemon_a_atacar):     
                    #Existe el pokemon?
        if pokemon in pokemon.id:                   #Existe el pokemon a atacar?    
            if self.vivo():                         #Esta vivo?
                if pokemon_a_atacar.vivo():         #El pokemon a atacar esta vivo?
                    pokemon_a_atacar.salud -= self.ataque * self.daño_arma()

                    if pokemon_a_atacar.salud <= 0:
                        pokemon_a_atacar.salud = 0
                        print(f"El pokemon {pokemon_a_atacar.nombre} ha muerto.")
                    
                    else:
                        print(f"El pokemon {pokemon_a_atacar.nombre} ha recibido un ataque de {self.ataque * self.daño_arma()} puntos de daño.")

            else:
                print("El pokemon a atacar debe estar vivo.")
        else:
            print("El pokemon no existe.")

    #Defensa de un pokemon
    def defender(self, pokemon, pokemon_a_defender):
        if pokemon.ataque < pokemon_a_defender.defensa:
            print("Has defendido el ataque.")
            return False
        else:
            return True
          

"""                 #La prueba que nos pedia en el ejercicio 1
#probamos para nuestros pokemons
pokemon1_entrenador1 = pokemon(11,"Pikachu","cabezazo",69,8,9)
pokemon2_entrenador1 = pokemon(12,"Pidgey","patada",85,7,7)
pokemon3_entrenador2 = pokemon(13,"Squirtel","codazo",74,7,6)

pokemon1_entrenafor2 = pokemon(14,"Diglett","puñetazo",82,9,7)
pokemon2_entrenador2 = pokemon(15,"Venusaur","patada",78,8,6)
pokemon3_entrenador2 = pokemon(16,"Charmeleon","codazo",88,9,7)
#enfrentamiento
print(pokemon.atacar(pokemon1_entrenador1, pokemon1_entrenafor2))
print(pokemon.defender(pokemon1_entrenador1, pokemon1_entrenafor2))
"""

#ACTIVIDAD 2

import random

#Clase herencia para cada tipo de pokemon

#Clase para pokemon de tipo tierra
class pokemon_tierra(pokemon):
    def __init__(self, ID, nombre, arma, salud, defensa, ataque):
        super().__init__(ID, nombre, arma, salud, defensa, ataque)
        if not isinstance(defensa, int) or not (11 <= defensa <= 20):
            print("El arma del pokemon debe ser de tipo tierra (entre 11 y 20).")
        

#Clase para pokemon de tipo agua
class pokemon_agua(pokemon):
    def __init__(self, ID, nombre, arma, salud, defensa, ataque):
        super().__init__(ID, nombre, arma, salud, defensa, ataque)
        if not isinstance(ataque, int) or not (11 <= defensa <= 20):
            print("El arma del pokemon debe ser de tipo agua (entre 11 y 20).")
        

#Clase para pokemon de tipo aire
class pokemon_aire(pokemon):
    def __init__(self, ID, nombre, arma, salud, defensa, ataque):
        super().__init__(ID, nombre, arma, salud, defensa, ataque)
    
    def defender(self, daño):                      #Cambio en la funcion de defensa
        if random.random(0,1) >= 0.5:
            self.salud -= daño - self.defensa
            print(f"El pokemon {self.nombre} ha recibido un ataque de {self.ataque * self.daño_arma()} puntos de daño.")

        else:
            print(f"El pokemon {self.nombre} ha recibido el ataque.")
          
#Clase para pokemon de tipo electrico
class pokemon_electrico(pokemon):
    def __init__(self, ID, nombre, arma, salud, defensa, ataque):
        super().__init__(ID, nombre, arma, salud, defensa, ataque)
    
    def ataque(self, pokemon_a_atacar):             #Cambio en la funcion de ataque
        if random.random(0,1) >= 0.5:
            daño = self.ataque * self.daño_arma() * 2
            pokemon_a_atacar.salud -= daño - pokemon_a_atacar.defensa
            print(f"El pokemon {pokemon_a_atacar.nombre} ha recibido un ataque de {daño} puntos de daño.")

        else:
            pokemon_a_atacar.salud -= self.ataque * self.daño_arma() - pokemon_a_atacar.defensa
            print(f"El pokemon {pokemon_a_atacar.nombre} ha recibido un ataque de {self.daño} puntos de daño.")
            