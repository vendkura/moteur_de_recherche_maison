Le systeme precedent sera relativement efficace en termes de precision, mais aussi
relativement long. Et encore, vous ne travaillez qu’avec une petite base de texte, mais
en general, de nos jours, on travaille avec des bases qui contiennent des millions de
documents !
Le probleme vient surtout de l’utilisation de la ḿethode des k plus proches voisins,
qui est tres longue quand on fait une recherche exhaustive. Il existe de nombreuses
variantes qui visent a etre plus rapides (mais non-exhaustives). Mais nous n’allons pas
nous attaquer a ce probleme difficile ici, par manque de temps.
Ici, on va plutot essayer d’ameliorer la phase d’indexation, en structurant les index
(descripteurs tf-idf). Pour acc ́el ́erer le systeme, vous allez donc mettre en place, en
plus, une phase de structuration des index.

Pour cela, vous allez implementer une ou plusieurs des m ́ethodes suivantes et comparer leurs efficacit ́es avec la structuration d’origine :

• une methode d’indexation bas ́ee sur les arbres. (KD-Tree)
• une methode de clustering (K-Means).
• une methode de hachage (LSH).
Pour chaque methode choisie, vous devrez l’inclure dans votre schema global puis la
tester et en comparant leurs effets sur les resultats en terme de performance (pr ́ecision),
et de temps de calcul.