"""Premier programme"""

def afficherResultat(nom, age):
    print("Bonjour " + nom)
    print("Tu as " + str(age) + " ans et l'an prochain tu auras " + str(age + 1) + " ans")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")
    return age_int


# -----------------------------------------------------------------------------

# demander le nom
nom1 = demander_nom()
nom2 = demander_nom()

# demander l'age
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# afficher les resultats

afficherResultat(nom1, age1)
afficherResultat(nom2, age2)
