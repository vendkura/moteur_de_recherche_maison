Un moteur de recherche retour toujours le r ́esultat des documents class ́es par l’ordre
decroissante de pertinence par rapport a la requete (taux de similarit ́e entre la requete et un document).
Apres avoir re ̧cu le dictionnaire des similitudes cosinus, il reste a trier la pertinence
de chaque document en fonction de sa similitude cosinus.
```py
docs trouves pond liste =[[sim , chemin] for chemin , sim
in docs trouves pond .items ()]
docs trouves pond liste = sorted( docs trouves pond liste ,
reverse=True)

for sim , chemin in docs trouves pond liste :
print(sim , chemin.split("/")[−1])
```

## RESULTAT :
```
0.022675277068383765 ep-00-10-03-fr.txt
0.020478650616061803 ep-00-04-13-fr.txt
0.012191496227354267 ep-00-02-15-fr.txt
0.010717430319714566 ep-00-09-06-fr.txt
0.010655193648183531 ep-00-05-16-fr.txt
```
