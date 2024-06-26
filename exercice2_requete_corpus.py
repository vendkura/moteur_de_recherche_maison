import json
# Chargement du corpus
fichier_json = open("index.json", "r")
corpus = json.load(fichier_json)
fichier_json.close ()

# Fonction qui permet de faire une recherche dans le corpus
def chercher_mots_simple(mot, index):
    if mot in index:
        return index[mot]
    else:
        return set()

# Fonction qui permet de d'abord checker si la requete est un mot composer, si oui on le decoupe en mot simple puis on fait la requete sur chacun des mots simples trouves et on retourne les fichiers dans lesquels ils se trouvent, sinon on fait la requete directement sur le mot
def chercher_mots_composes(mot, index):
    mots = mot.split()
    fichiers = set()
    for mot in mots:
        fichiers = fichiers.union(chercher_mots_simple(mot, index))
    return fichiers

mot_a_chercher = "homme femme"

print(chercher_mots_composes(mot_a_chercher, corpus))
