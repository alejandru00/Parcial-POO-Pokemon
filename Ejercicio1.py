

from enum import Enum

class pokemon:

    id = []
    max_salud = 100
    min_salud = 1
    max_ataque = 10
    min_ataque = 1
    max_defensa = 10
    min_defensa = 1

    def __init__(self, ID, nombre, arma, salud, defensa, ataque):
        
        #Comprobación de tipos
        if not ID == int:           
            raise TypeError("El ID del pokemon debe ser un entero.")
        if not nombre == str:
            raise TypeError("El nombre del pokemon debe ser un string.")
        if not arma in armas:
            raise TypeError("El arma del pokemon debe ser una arma ya creada.")
        if not salud == int or not (self.min_salud <= salud <= self.max_salud):
            raise ValueError("La salud del pokemon debe ser un entero entre 1 y 100.")
        if not ataque == int or not (self.min_ataque <= ataque <= self.max_ataque):
            raise ValueError("El ataque del pokemon debe ser un entero entre 1 y 10.")
        if not defensa == int or not (self.min_defensa <= defensa <= self.max_defensa):
            raise ValueError("La defensa del pokemon debe ser un entero entre 1 y 10.")
        if ID in pokemon.id:
            raise ValueError("El ID del pokemon debe ser unico.")
        
        self.ID = ID
        self.nombre = nombre
        self.arma = arma
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa
        pokemon.id.append(ID)
    
    #Destructor
    def __del__(self):              
        pokemon.id.remove(self.ID)
        print(f"El pokemon: {self.nombre}, eliminado.")

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
    def alive(self):               
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
        if pokemon_a_atacar in pokemon:                 #Existe el pokemon?
            
            if self.pokemon.alive():                    #Esta vivo?
                
                if pokemon_a_atacar.alive() == False:   #El pokemon a atacar esta vivo?
                    
                    if self.arma == "puñetazo":
                        pokemon_a_atacar.salud -= self.ataque * self.daño_arma()
                    elif self.arma == "patada":
                        pokemon_a_atacar.salud -= self.ataque * self.daño_arma()
                    elif self.arma == "codazo":
                        pokemon_a_atacar.salud -= self.ataque * self.daño_arma()
                    elif self.arma == "cabezazo":
                        pokemon_a_atacar.salud -= self.ataque * self.daño_arma()
                    
                    if pokemon_a_atacar.salud <= 0:
                        pokemon_a_atacar.salud = 0
                        print(f"El pokemon {pokemon_a_atacar.nombre} ha muerto.")

            else:
                print("El pokemon a atacar debe estar vivo.")
        else:
            print("El pokemon a atacar debe ser un pokemon ya creado.")

    #Defensa de un pokemon
    def defender(self, pokemon, pokemon_a_defender):
        if pokemon.ataque < pokemon_a_defender.defensa:
            return False
        else:
            return True
          


