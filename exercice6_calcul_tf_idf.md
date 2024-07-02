Term Frequency (TF), est le taux d’apparition d’un mot dans un document. Il
est toujours dans un intervalle de 0 `a 1 (inclus). Cette mesure indique si ce mot est frequent (donc important) par rapport aux autres mots du mˆeme document.

Formule :
```
T F(m,d) = (nombre d’occurrence de ce mot m dans le document d) / (nombre total de toutes les occurrences de tous les mots dans le document d)
```

Exemple de resultat : 
```py
allDocs ={ "docA":{"Le":0.25 ,"petit":0.25 ,"chat":0.25 ,"dort":0.25}
"docB": {"Le":0.3333 , "chat":0.3333 , "dort":0.3333}
"docC": {"Jean":0.5 , "dort":0.5}}
```

Inverse Document Frequency (IDF), est une mesure globale pour un mot.
Cette mesure est dans un intervalle de 0 `a 1 (inclus). Elle repr ́esente l’importance d’un mot pour marquer un document dans la base. Si un mot n’est pr ́esent que dans un
seul document, ce mot est important pour retrouver le document. En revanche, si un
mot est pr ́esent dans tous les documents de la base, il n’est pas significatif et son score IDF sera faible.

Formule :
```
IDF(m) = log10((nombre total de documents dans la base de donnees) / (nombre de documents ou ce mot m est present) )
```

Exemple de resultat:
```py
mot2idf ={ "Le":0.17609 ,
"petit":0.47712 ,
"Jean":0.47712 ,
"chat":0.17609 ,
"dort":0.0}
```

TF montre l’importance d’un mot dans un document tandis que IDF indique si un
mot est important pour remarquer un document dans la base de donnees.
Le produit des scores TF et IDF d’un mot est utilis ́e ensuite pour la dimension de
ce mot pour un document. Les documents sont ainsi repr ́esent ́es comme des vecteurs (avec tous les mots du vocabulaire comme dimensions).