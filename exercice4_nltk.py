import json
import re
import os
from nltk.tokenize import word_tokenize

# Chargement du corpus
with open("index.json", "r") as fichier_json:
    corpus = json.load(fichier_json)

def adjust_path_for_windows(file_path):
    return os.path.normpath(file_path)

def chercher_mots_simple(mot, index):
    if mot in index:
        return index[mot]
    else:
        return set()

def chercher_mots_composes(mots, index):

    
    mots = word_tokenize(mots) if isinstance(mots, str) else mots
    resultats = {}
    for mot in mots:
        temp_fichier = chercher_mots_simple(mot, index)
        if temp_fichier:
            resultats[mot] = temp_fichier
        else:
            resultats[mot] = "No results found for this word"
    return resultats

def afficher_contextes(fichier, terme, taille_contexte=30):
    try:
        with open(adjust_path_for_windows(fichier), "r", encoding="utf-8") as f:
            chaine = f.read()
            match = re.search(terme, chaine)
            contexts = []
            while match is not None:
                gauche = max(match.start() - taille_contexte - 1, 0)
                droite = match.end() + 1 + taille_contexte
                contexts.append(chaine[gauche:droite])
                chaine = chaine[match.end():]
                match = re.search(terme, chaine)
            for context in contexts:
                print(f"Le mot '{terme}' a ete trouver dans les fichiers: {fichier}, dont les contextes sont :\n {context}")
    except FileNotFoundError:
        print(f"File {fichier} not found.")

def afficher_contextes_pour_resultats(resultats):
    for terme, fichiers in resultats.items():
        if fichiers != "No results found for this word":
            for fichier in fichiers:
                afficher_contextes(fichier, terme)

mot_a_chercher = ["lecoq", "femme", "homme", "chien"]
resultats = chercher_mots_composes(mot_a_chercher, corpus)
afficher_contextes_pour_resultats(resultats)