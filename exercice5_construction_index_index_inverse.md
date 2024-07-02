Ensuite, nous allons implementer les fonctions creer_index() et creer_index inverse().
# EXAMPLE
## Code
```py
index = creer_index ()
index_inverse = creer_index_inverse ()
print("Nombre de termes differents : ", len(index.keys ()))
print("Nombre de documents :", len( index_inverse .keys ()))
```
## Resultat
```
Nombre de termes differents :
Nombre de documents :
```

Les deux indexes: _index_ et _index inverse_ nous permettront d’utiliser le reste des fonctions disponibles. Nous pourrions par exemple faire une requete a notre moteur de
recherche en utilisant la fonction __requeter_documents(requete, index)__

```py
requete = "liberte humaine"
docs trouves = requeter documets (requete , index)
print("Nombre de documents trouvees :", len( docs trouves ))
requete = "sensibilisation minorit«es"
docs trouves = requeter documets (requete , index)
print("Nombre de documents trouvees :", len( docs trouves ))
```

## Resultat
```
Nombre de documents trouves:
Nombre de documents trouves:
```