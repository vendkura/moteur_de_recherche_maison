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

# chargement de tf-idf
tf_idf_filename="tf_idf_matrix.json"
# Read and deserialize from JSON
with open(tf_idf_filename, 'r') as file:
    tf_idf_list_loaded = json.load(file)

# Convert back to a numpy array or the original format used
tf_idf_matrix = np.array(tf_idf_list_loaded)
# -----------------------------------------------------

vectorizer = TfidfVectorizer()
vectorizer.fit(corpus)

documents = defaultdict(set)
for mot, fichiers in corpus.items():
    for fichier in fichiers:
        documents[fichier].add(mot)



# KD-Tree -> n'est pas implementer avec success
# -----------------------------------------------------
# def rechercher_dans_kdtree(requete, vectorizer, kd_tree, k=5):
#     # Convertir la requête en vecteur TF-IDF
#     tf_idf_requete = vectorizer.transform([requete])
    
    
#     tf_idf_requete_dense = tf_idf_requete.toarray()

#     # Trouver les k plus proches voisins
#     distances, indices = kd_tree.query(tf_idf_requete_dense, k=k)
    
#     return indices[0]



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
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(tf_idf_matrix)
cluster_assignments = kmeans.labels_
print(f"CLUSTER ASSIGNMENTS : {cluster_assignments} \n")
centroids = kmeans.cluster_centers_
print(f"CENTROIDS SHAPE: {centroids}")

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

similar_docs_indices = lsh.query(query_minhash)
print(f"Documents similaires à la requête : {similar_docs_indices}")
for doc_index in similar_docs_indices:
    print(f"Document {doc_index} is similar to the query")
# print(f"Documents similaires à la requête : {similar_docs}")
#-----------------------------------------------------
