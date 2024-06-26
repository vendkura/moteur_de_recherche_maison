Exercice 1 : Construire un index

Pour ne pas avoir `a parcourir toute une base de donn ́ees afin de trouver des docu-
ments pertinents pour chaque requˆete (et donc aller “lire” tous les documents `a chaque

requˆete), l’index est utilis ́e pour acc ́eder directement `a un ensemble de documents qui
contiennent les mots de la requˆete.
En Python, un index peut ˆetre repr ́esent ́e par un dictionaire avec les mots index ́es
comme cl ́e, puis un ensemble (ou une liste) de documents qui contient ce mot.
On a donc besoin de d ́ecouper en mots chaque fichier du corpus et d’associer `a
chaque mot tous les fichiers o`u on le trouve.
Etape 1: Construire le vocabulaire et un index simple
Le vocabulaire c’est l’ensmeble des mots rencontr ́es dans le corpus. On n’indexe
pas des mots qu’on a pas vu.

