# Etape 1: Construire le vocabulaire et un index simple

import glob
import json

def lire_fichier(chemin):
    with open(chemin, 'r', encoding='utf-8') as fichier:
        return fichier.read()

def decouper_mots(chaine):
    # Assuming a simple split by whitespace for word tokenization
    return chaine.split()

# Fonction pour faire les quetes de mots dans les fichiers et retourner : le chemin du fichier et le nombre d'occurences
def chercher_mots(mot, index):
    if mot in index:
        return index[mot]
    else:
        return set()
    

index = {}
for chemin in glob.glob("europarl/europarl/fr/*"):
    chaine = lire_fichier(chemin)
    mots = decouper_mots(chaine)
    print(f"[INFO] Ajout des mots trouvés dans l'index")
    for mot in mots:
        if mot not in index:
            index[mot] = set()
            print(f"Le mot {mot} a été ajouté à l'index")
        index[mot].add(chemin)

# Transformation de l'index en un dictionnaire pour le sauvegarder dans un fichier json
index_for_json = {key:list(value) for key, value in index.items()}
json_string = json.dumps(index_for_json)

# Sauvegarde de l'index transformer dans un fichier json.
with open('index.json', 'w', encoding='utf-8') as fichier:
    json.dump(index_for_json,fichier)



mot_a_chercher = "toto"
print(f"------------[INFO] Statisques ------------")
print(f"Taille du vocabulaire : {len(index)}")
print(f"Echantillon du vocabulaire{list(index.keys ())[:50]}")
print(f"Chemins des documents contenant : {mot_a_chercher}\n {index[mot_a_chercher]}")
print(f"------------[DEMO] Function recherche ------------")
print(f"mot_a_chercher:{ chercher_mots(mot_a_chercher, index)}")