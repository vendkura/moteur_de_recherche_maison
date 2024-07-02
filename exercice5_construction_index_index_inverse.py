import json
from collections import defaultdict
from nltk.tokenize import word_tokenize

# Chargement du corpus
fichier_json = open("index.json", "r")
corpus = json.load(fichier_json)
fichier_json.close ()

def creer_index_inverse_depuis_index(index):
    index_inverse = defaultdict(set)
    for mot, documents in index.items():
        for document in documents:
            index_inverse[document].add(mot)
    return index_inverse


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
    fichiers = set()
    for mot in mots:
        temp_fichier = chercher_mots_simple(mot, index)
        if temp_fichier:
            if mot in resultats:
                resultats[mot] = resultats[mot].union(temp_fichier)
            else:
                resultats[mot] = temp_fichier
        else:
            resultats[mot] = "Aucun resultat trouve pour ce mot"
        # fichiers = fichiers.union(chercher_mots_simple(mot, index))
        # resultats[mot] = fichiers 
    return resultats


# Création des index
index_inverse = creer_index_inverse_depuis_index(corpus)

mot_a_chercher = ["lecoq","femme","homme","chien"]
doc_trouver = chercher_mots_composes(mot_a_chercher, corpus)

print("[INFO] Calcul du Nombre de documents pour les requetes")
print(f"Nombre de documents pour la requete : {len(doc_trouver.keys())}")

print("[INFO] Calcul du Nombre de documents sur l'ensemble du corpus")
# Affichage des informations sur les index de tout le corpus : 
print("Nombre de termes différents :", len(corpus.keys()))
print("Nombre de documents :", len(index_inverse.keys()))
