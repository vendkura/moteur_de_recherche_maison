# KD-Tree
# -----------------------------------------------------
def rechercher_dans_kdtree(requete, vectorizer, kd_tree, k=5):
    # Convertir la requête en vecteur TF-IDF
    tf_idf_requete = vectorizer.transform([requete])
    
    
    tf_idf_requete_dense = tf_idf_requete.toarray()

    # Trouver les k plus proches voisins
    distances, indices = kd_tree.query(tf_idf_requete_dense, k=k)
    
    return indices[0]



# Construction du KD-Tree
# kd_tree = KDTree(tf_idf_matrix, leaf_size=30, metric='euclidean')

# Exemple d'utilisation
request = "fonction"
# indices_plus_proches = rechercher_dans_kdtree(request, vectorizer, kd_tree, k=5)
# print(indices_plus_proches)

#-----------------------------------------------------
# K-MEANS
num_clusters = 20

print(tf_idf_matrix.shape)
# Apply K-Means clustering
# kmeans = KMeans(n_clusters=num_clusters, random_state=42)
# kmeans.fit(tf_idf_matrix)
# cluster_assignments = kmeans.labels_
# print(f"CLUSTER ASSIGNMENTS : {cluster_assignments} \n")
# centroids = kmeans.cluster_centers_
# print(f"CENTROIDS SHAPE: {centroids}")

# If you want to test, uncomment the below code
# for doc_index, cluster_num in enumerate(cluster_assignments):
#     print(f"Document {doc_index} is in Cluster {cluster_num}")
#-----------------------------------------------------
# LSH
num_perm = 128  
minhashes = []
for tf_idf_vector in tf_idf_matrix:
    m = MinHash(num_perm=num_perm)
    for i, v in enumerate(tf_idf_vector):
        if v > 0:
            print(f"Vector : {v}\n")  
            m.update(str(i).encode('utf8') * int(v * 100))  # Weight the hash by the TF-IDF value
    minhashes.append(m)

# LSH index creation et insertion des MinHashes
lsh = MinHashLSH(threshold=0.5, num_perm=num_perm)  # Adjust threshold based on your similarity requirements
for i, minhash in enumerate(minhashes):
    lsh.insert(f"doc_{i}", minhash)

# Requête
# query_doc = minhashes[0]
query = "femme"
query_vector = vectorizer.transform([query])

query_minhash = MinHash(num_perm=num_perm)
print(f"HASH: {query_minhash}")
for i, v in enumerate(query_vector.toarray()[0]):
    if v > 0:
        query_minhash.update(str(i).encode('utf8') * int(v * 100))

print(f"UNIQUE WORDS: {idf_mots}\n")
# print(f"TF-IDF MATRICE : {tf_idf_matrix}\n")
# print(f" LSH DICO: {lsh}\n")
# print(f" MINHASHES: {minhashes}\n")
similar_docs_indices = lsh.query(query_minhash)
print(f"Documents similaires à la requête : {similar_docs_indices}")
for doc_index in similar_docs_indices:
    print(f"Document {doc_index} is similar to the query")
# print(f"Documents similaires à la requête : {similar_docs}")
#-----------------------------------------------------


# print("Indices des documents les plus proches:", indices_plus_proches)




# -----------------------------------------------------
# TF-IDF
import json
import math
from collections import defaultdict, Counter
import numpy as np
from sklearn.neighbors import KDTree
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from datasketch import MinHash, MinHashLSH

# Chargement du corpus
fichier_json = open("index.json", "r")
corpus = json.load(fichier_json)
fichier_json.close ()

vectorizer = TfidfVectorizer()
vectorizer.fit(corpus)

documents = defaultdict(set)
for mot, fichiers in corpus.items():
    for fichier in fichiers:
        documents[fichier].add(mot)


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
 

# Calcul de TF-IDF
tf_idf_docs = {}
for doc, mots_tf in tf_docs.items():
    tf_idf_mots = {}
    for mot, tf in mots_tf.items():
        tf_idf_mots[mot] = tf * idf_mots[mot]
    tf_idf_docs[doc] = tf_idf_mots

corpus_idf = [" ".join(tf_idf_mots.keys()) for tf_idf_mots in tf_idf_docs.values()]

# Liste de tous les mots dans le corpus pour créer des vecteurs de même longueur
mots_uniques = list(idf_mots.keys())
# Création d'une matrice où chaque ligne est le vecteur TF-IDF d'un document
tf_idf_matrix = []
for doc in tf_idf_docs.keys():
    tf_idf_vector = [tf_idf_docs[doc].get(mot, 0) for mot in mots_uniques]
    tf_idf_matrix.append(tf_idf_vector)

tf_idf_matrix = np.array(tf_idf_matrix)

tf_idf_matrix_list = tf_idf_matrix.tolist() if isinstance(tf_idf_matrix, np.ndarray) else tf_idf_matrix
