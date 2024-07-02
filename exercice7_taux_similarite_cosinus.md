Quand les documents sont repr ́esent ́es par les vecteurs, les calculs entre les documents sont devenus possibles.
Pour un moteur de recherche, le calcul lie est le taux de similarit ́e entre une requete
et un document pour pouvoir ensuite classer les documents par pertinence.
Une fa ̧con rapide pour calculer le taux de similarit ́e est le cosinus. Ce taux de
similarit ́e se situe toujours entre 0 et 1 (inclus). 0 signifie que les deux documents n’ont
aucun mot en commun tandis que 1 signifie que les deux documents sont identiques.

```
sim(r, A) = cos(r, A) = (r · A) / (||r|| · ||A||)
```
Rappel: le produit scalaire de deux vecteurs est la somme de tous les produits
dans chaque dimension.
Si le vecteur de la requˆete r et le vecteur du document A sont:
```
r =< r0, r1, ..., rV >
A =< A0, A1, ..., AV >
```
V est la taille de vocabulaire. alors
```
r · A = r0 ∗ A0 + r1 ∗ A1 + ... + rV ∗ AV
```

Nous allons passer a l’implementation de nos fonctions de similarite cosinus :
• indexer requete(requete)
• calculer sim cosinus(docA, docB)
• calcule_ponderation_cosinus(requete, index inverse, documents trouves)
```
docs_trouves_pond = calcule_ponderation_cosinus (requete ,index_inverse , docs_trouves )
```