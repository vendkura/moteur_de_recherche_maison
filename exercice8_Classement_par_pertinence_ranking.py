import json
import math
from collections import defaultdict, Counter

# Chargement du corpus
with open("index.json", "r") as fichier_json:
    corpus = json.load(fichier_json)

# Créer un dictionnaire pour compter les occurrences des mots dans chaque document
documents = defaultdict(Counter)
for mot, fichiers in corpus.items():
    for fichier in fichiers:
        documents[fichier][mot] += 1

# Calcul de IDF
idf_mots = {}
nb_docs = len(documents)
for mot in corpus:
    nb_docs_contenant_mot = len(corpus[mot])
    idf_mots[mot] = math.log10(nb_docs / nb_docs_contenant_mot)

# Calcul de TF et TF-IDF
tfidf_docs = {}
for doc, mots in documents.items():
    nb_total_mots = sum(mots.values())
    tfidf_mots = {}
    for mot, count in mots.items():
        tf = count / nb_total_mots
        idf = idf_mots[mot]
        tfidf_mots[mot] = tf * idf
    tfidf_docs[doc] = tfidf_mots

# Fonction pour indexer une requête
def indexer_requete(requete):
    if isinstance(requete, str):
        requete = requete.split()
    tf_requete = Counter(requete)
    nb_total_mots_requete = sum(tf_requete.values())
    tfidf_requete = {mot: (tf_requete[mot] / nb_total_mots_requete) * idf_mots.get(mot, 0) for mot in tf_requete}
    return tfidf_requete


def calculer_sim_cosinus(vecA, vecB):
    intersection = set(vecA.keys()) & set(vecB.keys())
    num = sum([vecA[x] * vecB[x] for x in intersection])
    sum1 = sum([val**2 for val in vecA.values()])
    sum2 = sum([val**2 for val in vecB.values()])
    denom = math.sqrt(sum1) * math.sqrt(sum2)
    if not denom:
        return 0.0
    else:
        return float(num) / denom

# Fonction pour calculer la pondération cosinus pour les documents trouvés
def calcule_ponderation_cosinus(requete, documents_trouves):
    tfidf_requete = indexer_requete(requete)
    scores = {}
    for doc in documents_trouves:
        tfidf_doc = tfidf_docs[doc]  # Utilisation de l'index TF-IDF ajusté
        scores[doc] = calculer_sim_cosinus(tfidf_requete, tfidf_doc)
    return scores


# Fonction qui permet de faire une recherche dans le corpus
def chercher_mots_simple(mot, index):
    if mot in index:
        return index[mot]
    else:
        return set()

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
# Exemple d'utilisation
requete = "fonctionnaire"
index_inverse = tfidf_docs  


doc_trouver = chercher_mots_simple(requete,corpus)
docs_trouves_pond = calcule_ponderation_cosinus(requete, doc_trouver)

# Création de la liste de paires [sim, chemin] à partir du dictionnaire
docs_trouves_pond_liste = [[sim, chemin.replace('\\', '/')] for chemin, sim in docs_trouves_pond.items()]

# Tri de la liste en ordre décroissant de similarité
docs_trouves_pond_liste = sorted(docs_trouves_pond_liste, reverse=True)

# Affichage des résultats, en remplaçant les antislashs par des slashs pour la compatibilité
for sim, chemin in docs_trouves_pond_liste:
    print(sim, chemin.split("/")[-1])



