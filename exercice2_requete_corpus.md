Exercice 2 : Requeter le corpus
Maintenant on voudrait requˆeter en associant plusieurs mots.
On charge l’index :
f = open("index.json", "r")
index = json.load(f)
f.close ()

A vous de jouer maintenant, il s’agit de d ́ecouper la requˆete en mots et
de trouver tous les documents contenant un des mots de la requˆete
Ce qui revient `a :
• creer une variable qui contient la requˆete, par exemple “Commission Europ ́eenne”
• decouper la requete en mots
• chercher pour chaque mot les documents ou il apparaıt
• afficher la liste des documents en question


On va pouvoir faire des am ́eliorations:
• afficher si aucun mot de la requˆete n’est connu
• ne pas afficher les doublons: si tous les mots de la requˆete sont pr ́esents dans un
mˆeme document, on ne veut pas afficher plusieurs fois le nom de ce document
• mettre les documents dans l’ordre d ́ecroissant du nombre de mots de la requˆete
qu’il contienne
• limiter l’affichage aux 10 premiers documents