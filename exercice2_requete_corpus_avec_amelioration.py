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
    mots = mot.split() if isinstance(mot,str) else mot
    resultats = {}
    print(f"mots divises:{mots}")

    #Initialize a set to collect files containing any of the words
    tous_fichiers = set()
    # Initialize a dictionary to hold sets of files for each word
    fichiers_par_mot = {}
    #
    tous_fichiers = set()
    #
    fichiers = set()
    for mot in mots:
        temp_fichier = chercher_mots_simple(mot, index)

        if temp_fichier:
            #
            fichiers_par_mot[mot] = temp_fichier
            #
            tous_fichiers.update(temp_fichier)
            if mot in resultats:
                resultats[mot] = resultats[mot].union(temp_fichier)
            else:
                resultats[mot] = temp_fichier
        else:
            resultats[mot] = "Aucun resultat trouve pour ce mot"
        # fichiers = fichiers.union(chercher_mots_simple(mot, index))
        # resultats[mot] = fichiers 
    return resultats

mot_a_chercher = ["documents","femme","homme","chien"]

print(chercher_mots_composes(mot_a_chercher, corpus))
