import json
import math
from collections import defaultdict, Counter

# Chargement du corpus
fichier_json = open("index.json", "r")
corpus = json.load(fichier_json)
fichier_json.close ()
 
# Creer un dictionnaire qui doit contenir les mots uniques
documents = defaultdict(set)
for mot, fichiers in corpus.items():
    for fichier in fichiers:
        documents[fichier].add(mot)

# Calcul de TF
tf_docs ={}
for doc,mots in documents.items():
    nb_total_mots = len(mots)
    tf_mots = Counter(mots) # On se dit que chaque mot apparait juste une seule fois
    for mot in tf_mots:
        tf_mots[mot] = tf_mots[mot] / nb_total_mots
    tf_docs[doc] = dict(tf_mots)


# Calcul de IDF
idf_mots = {}
nb_docs = len(documents)
for mot in corpus:
    nb_docs_contenant_mot = len(corpus[mot])
    idf_mots[mot] = math.log10(nb_docs / nb_docs_contenant_mot)


# Affichage des résultats
print("[INFO] AFFICHAGE DES RESULTATS TF-IDF")
print("TF par document :")
for doc, tf in list(tf_docs.items())[:10]:
    print(f"{doc}: {tf}\n")
print("-------------------------------------")
print("\nIDF par mot :\n")
for mot, idf in list(idf_mots.items())[:50]:
    print(f"{mot}: {idf}\n")

# Pour afficher tous les TF des documents
for doc, tf in tf_docs.items():
    print(f"{doc}: {tf}")