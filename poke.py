import random
import winsound


class Pokemon:
    """Pokemon, type 1, type 2, pv, attack, defense, special attack, special defense, vitesse, liste des capacités"""

    level = 5
    def __init__(self, nom, type_1, type_2, pv, attack, defense, sp_atk, sp_def, vitesse, attaques):
        self.nom = nom
        self.type_1 = type_1
        self.type_2 = type_2
        self.pv = pv
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.vitesse = vitesse
        self.attaques = attaques

class bulbizarre(Pokemon):

        def __init__(self):
            self.nom = "bulbizarre"
            self.type_1 = "plante"
            self.type_2 = "poison"
            self.pv = 45
            self.attack = 49
            self.defense = 49
            self.sp_atk = 65
            self.sp_def = 65
            self.vitesse = 45
            self.attaques = ["charge", "fouet lianes"]

        def attaque(self, numero_attaque):
            self.numero_attaque = numero_attaque
            if numero_attaque == "1":

                self.nom_attaque = self.attaques[0]
                print(self.nom, "utilise", self.nom_attaque, "!")
                self.puissance = 40
                self.coeff = 1
            elif numero_attaque == "2":
                self.nom_attaque = self.attaques[1]
                print(self.nom, "utilise", self.nom_attaque, "!")
                self.puissance = 40
                if pokemon_rival.type_1 == "eau":
                    self.coeff = 2
                    print("c'est très efficace!")
                elif pokemon_rival.type_1 == "feu" or pokemon_rival.type_1 == "plante":
                    self.coeff = 0.5
                    print("ce n'est pas très efficace...")
                else :
                    self.coeff = 1

class carapuce(Pokemon):

        def __init__(self):
            self.nom = "carapuce"
            self.type_1 = "eau"
            self.type_2 = None
            self.pv = 44
            self.attack = 48
            self.defense = 65
            self.sp_atk = 50
            self.sp_def = 64
            self.vitesse = 43
            self.attaques = ["charge", "pistolet à O"]
            self.puissance = 40
            self.coeff = 0


        def attaque(self, numero_attaque):
            self.numero_attaque = numero_attaque
            if numero_attaque == "1":

                self.nom_attaque = self.attaques[0]
                print(self.nom, "utilise", self.nom_attaque, "!")
                self.puissance = 40
                self.coeff = 1
            elif numero_attaque == "2":
                self.nom_attaque = self.attaques[1]
                print(self.nom, "utilise", self.nom_attaque, "!")
                self.puissance = 40
                if pokemon_rival.type_1 == "feu":
                    print("c'est très efficace!")
                    self.coeff = 2
                elif pokemon_rival.type_1 == "plante" or pokemon_rival.type_1 == "eau":
                    self.coeff = 0.5
                    print("ce n'est pas très efficace...")
                else :
                    self.coeff = 1

class salameche(Pokemon):
        def __init__(self):
            self.nom = "salameche"
            self.type_1 = "feu"
            self.type_2 = None
            self.pv = 39
            self.attack = 52
            self.defense = 43
            self.sp_atk = 60
            self.sp_def = 50
            self.vitesse = 65
            self.attaques = ["griffe", "flammèche"]
            self.puissance = 40
            self.coeff = 1

        def attaque(self, numero_attaque):
            self.numero_attaque = numero_attaque
            if numero_attaque == "1":

                self.nom_attaque = self.attaques[0]
                print(self.nom, "utilise", self.nom_attaque, "!")
                self.puissance = 40
                self.coeff = 1
            elif numero_attaque == "2":
                self.nom_attaque = self.attaques[1]
                print(self.nom, "utilise", self.nom_attaque, "!")
                self.puissance = 40
                if pokemon_rival.type_1 == "plante":
                    self.coeff = 2
                    print("c'est très efficace!")
                elif pokemon_rival.type_1 == "eau" or pokemon_rival.type_1 == "feu":
                    self.coeff = 0.5
                    print("ce n'est pas très efficace...")
                else :
                    self.coeff = 1

class pikachu(Pokemon):
    def __init__(self):
        self.nom = "pikachu"
        self.type_1 = "electrik"
        self.type_2 = None
        self.pv = 35
        self.attack = 55
        self.defense = 40
        self.sp_atk = 50
        self.sp_def = 50
        self.vitesse = 95
        self.attaques = ["vive-attaque", "éclair"]
        self.puissance = 40
        self.coeff = 1

    def attaque(self, numero_attaque):
        self.numero_attaque = numero_attaque
        if numero_attaque == "1":

            self.nom_attaque = self.attaques[0]
            print(self.nom, "utilise", self.nom_attaque, "!")
            self.puissance = 40
            self.coeff = 1
        elif numero_attaque == "2":
            self.nom_attaque = self.attaques[1]
            print(self.nom, "utilise", self.nom_attaque, "!")
            self.puissance = 40
            if pokemon_rival.type_1 == "eau" and pokemon_rival.type_1 == "vol":
                self.coeff = 2
                print("c'est très efficace!")
            elif pokemon_rival.type_1 == "electrik" or pokemon_rival.type_1 == "plante":
                self.coeff = 0.5
                print("ce n'est pas très efficace...")
            else :
                self.coeff = 1


class roucool(Pokemon):
    def __init__(self):
        self.nom = "roucool"
        self.type_1 = "vol"
        self.type_2 = None
        self.pv = 40
        self.attack = 45
        self.defense = 40
        self.sp_atk = 35
        self.sp_def = 35
        self.vitesse = 56
        self.attaques = ["charge", "tornade"]
        self.puissance = 40
        self.coeff = 1

    def attaque(self, numero_attaque):
        self.numero_attaque = numero_attaque
        if numero_attaque == "1":

            self.nom_attaque = self.attaques[0]
            print(self.nom, "utilise", self.nom_attaque, "!")
            self.puissance = 40
            self.coeff = 1
        elif numero_attaque == "2":
            self.nom_attaque = self.attaques[1]
            print(self.nom, "utilise", self.nom_attaque, "!")
            self.puissance = 40
            if pokemon_rival.type_1 == "plante":
                self.coeff = 2
                print("c'est très efficace!")
            elif pokemon_rival.type_1 == "electrik":
                self.coeff = 0.5
                print("ce n'est pas très efficace...")
            else :
                self.coeff = 1


my_pokemon= input("Choose your starter : 0: bulbizarre, 1 : salameche, 2: carapuce, 3:pikachu, 4: roucool\n")


# si l'utilisateur n'écrit pas les numéros énoncés lui indiquer une erreur et le refaire choisir
while my_pokemon != "0" and my_pokemon != "1" and my_pokemon !="2"  and my_pokemon != "3" and my_pokemon != "4":
    print("ERROR")
    my_pokemon= input("Choose your starter : 0: bulbizarre, 1 : salameche, 2: carapuce, 3:pikachu, 4: roucool\n")


if int(my_pokemon) == 0:
    my_pokemon = bulbizarre()
elif int(my_pokemon) == 1:
    my_pokemon = salameche()
elif int(my_pokemon) == 2:
    my_pokemon = carapuce()
elif int(my_pokemon) == 3:
    my_pokemon = pikachu()
else :
    my_pokemon = roucool()

print("Vous avez choisi", my_pokemon.nom, "!!!")

choix_pokemon_ordi = random.randint(1, 5)
if choix_pokemon_ordi == 1:
    pokemon_rival = carapuce()
elif choix_pokemon_ordi == 2:
    pokemon_rival = bulbizarre()
elif choix_pokemon_ordi == 3:
    pokemon_rival = salameche()
elif choix_pokemon_ordi == 4:
    pokemon_rival = pikachu()
else :
    choix_pokemon_ordi = roucool()



print("L'ordi a choisi", pokemon_rival.nom, "!!!")

print("\n ********************************* DEBUT DU COMBAT *********************************\n")

winsound.Beep(2500, 1000)



nombre_degats = 0
def degats(pokemon_attaquant, pokemon_defenseur):
    """ degats est une fonction qui définit le nombre de dégats fait pas le pokemon attaquant, avec une probabilité de coup critique et une probabilité que l'attaque échoue
        
        Input : pokemon_attaquant est un objet
                pokemon_defenseur est un objet
            
        Output :   
                nombre_degats est un int     
        
        """
    nombre_degats = 0
    coup_critique = random.randint(1, 10)
    evite_attaque = random.randint(1, 15)
    if evite_attaque == 1:
        nombre_degats = 0
        print( pokemon_defenseur.nom, "évite l'attaque !!!!!!!")

    elif coup_critique==1:
        nombre_degats = (int(((((pokemon_attaquant.level*0.4+2)*pokemon_attaquant.puissance*pokemon_attaquant.attack)/(pokemon_defenseur.defense*50))+2)*pokemon_attaquant.coeff))*2

        print("!!!!! COUP CRITIQUE !!!!!")

    else :
        nombre_degats = int(((((pokemon_attaquant.level*0.4+2)*pokemon_attaquant.puissance*pokemon_attaquant.attack)/(pokemon_defenseur.defense*50))+2)*pokemon_attaquant.coeff)

    return nombre_degats


# le pokemon ayant la vitesse la plus grande attaque en premier
# si l'un des pokemons tombe en dessous de 0 pv, le combat s'arrete
# les attaques de l'ordi sont aléatoires

tour = 0
while my_pokemon.pv > 0 or pokemon_rival.pv > 0:
    tour +=1
    print("\n----------------- Tour numéro", tour, " -----------------\n")
    player = max(my_pokemon.vitesse,pokemon_rival.vitesse)
    if player == my_pokemon:
        print(" 1:",my_pokemon.attaques[0],"       2:", my_pokemon.attaques[1])
        numero_attaque = input("Attaquez!!         ")
        while numero_attaque != "1" and numero_attaque != "2":
            print(" 1:",my_pokemon.attaques[0],"       2:", my_pokemon.attaques[1])
            numero_attaque = input("Attaquez!!         ")
        my_pokemon.attaque(numero_attaque)
        pokemon_rival.pv = pokemon_rival.pv - degats(my_pokemon, pokemon_rival)
        print("Le ", pokemon_rival.nom,"rival a subit", degats(my_pokemon, pokemon_rival),"dégat(s), il lui reste", pokemon_rival.pv, "pv")
        if pokemon_rival.pv > 0 :
            pokemon_rival.attaque(str(random.randint(1, 2)))
            my_pokemon.pv = my_pokemon.pv - degats(pokemon_rival, my_pokemon)
            print("Votre ", my_pokemon.nom,"a subit",  degats(pokemon_rival, my_pokemon),"dégat(s), il lui reste", my_pokemon.pv, "pv")
        else :
            break
    else :
        pokemon_rival.attaque(str(random.randint(1, 2)))
        my_pokemon.pv = my_pokemon.pv - degats(pokemon_rival, my_pokemon)
        print("Votre ", my_pokemon.nom,"a subit",  degats(pokemon_rival, my_pokemon),"dégat(s), il lui reste", my_pokemon.pv, "pv")
        if my_pokemon.pv > 0:
                print(" 1:",my_pokemon.attaques[0],"       2:", my_pokemon.attaques[1])
                numero_attaque = input("Attaquez!!         ")
                while numero_attaque != "1" and numero_attaque != "2":
                    print(" 1:",my_pokemon.attaques[0],"       2:", my_pokemon.attaques[1])
                    numero_attaque = input("Attaquez!!         ")
                my_pokemon.attaque(numero_attaque)
                pokemon_rival.pv = pokemon_rival.pv - degats(my_pokemon, pokemon_rival)
                print("Le ", pokemon_rival.nom,"rival a subit", degats(my_pokemon, pokemon_rival),"dégat(s), il lui reste", pokemon_rival.pv, "pv")
                if pokemon_rival.pv<=0:
                    break
        else :
            break





print("****************************** FIN DU COMBAT ******************************")
winsound.Beep(2600, 1000)


if my_pokemon.pv <= 0:
    print ("Votre pokémon est KO !\nVous avez perdu :( ")






if pokemon_rival.pv <= 0:
    print("Le pokémon rival est KO!\nVous avez gagné :D ")

    
    
    
  
