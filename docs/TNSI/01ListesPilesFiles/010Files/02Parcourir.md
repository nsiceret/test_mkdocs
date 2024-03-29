---
template: pyscript.html
---
# Parcourir une file

Une file ne contient que quatre opérations (ou fonctions) élémentaires. En particulier, il n'y a pas de fonction `longueur` pour calculer le nombre d'éléments d'une file. Mais parfois on peut avoir besoin de plus.

Le modèle à suivre pour étudier une file est de **défiler** un à un les éléments jusqu'à obtenir ce qu'on veut ou que la file soit vide. À noter que lorsqu'on défile un élément, on l'enlève de la file.

Programmons deux nouvelles fonctions : `calculer` la longueur d'une file et `chercher` si un élément est dans une file.

## Longueur

Pour calculer la longueur d'une file, on initialise un `compteur` à zéro. Puis, TANT QUE la file n'est pas vide, on défile l'élément de tête et on ajoute un au compteur.


Ci-dessous, une fonction Python `longueur` qui calcule la longueur d'une file donnée en paramètre. Étudiez bien son code pour le comprendre.

<py-env>
- paths:
  - ../files.py
</py-env>
<py-repl id="repl_longueur" title="Longueur d'un file">
from files import *
def longueur(file):
    compteur = 0
    while not est_vide(file):
        defiler(file)
        compteur += 1
    return compteur
F = creer_file_vide() #une file vide
enfiler(F,3)      # j'enfile le nombre 3 dans F
enfiler(F,5)      # j'enfile le nombre 5 dans F
enfiler(F,2)
enfiler(F,8)
print("longueur :",longueur(F))
</py-repl>
{{boutons('repl_longueur')}}

## Chercher

Pour chercher si une `cible` est dans une file, on initialise une variable `trouve` à `False`. Cela signifie qu'on n'a pas encore trouvé l'élément dans la file. Ensuite on utilise une boucle TANT QUE. TANT QUE on n'a pas trouvé ET que la file n'est pas vide, on défile l'élement de tête et on l'examine SI cet élément est égal à `cible`. Si il l'est, on affecte `True` à la variable `trouve`.

Après la boucle TANT QUE, on renvoie la valeur de `trouve`.

Ci-dessous, une fonction Python `chercher(file,cible)` qui implémente cet algorithme.

<py-repl id="repl_chercher">
from files import *
def chercher(file,cible):
    trouve = False
    while (not trouve) and (not est_vide(file)):
        e = defiler(file)
        if e == cible:
            trouve = True
    return trouve
 # test
F = creer_file_vide() #une file vide
enfiler(F,3)      # j'enfile le nombre 3 dans F
enfiler(F,5)      # j'enfile le nombre 5 dans F
enfiler(F,2)
enfiler(F,8)
print(chercher(F,8))
</py-repl>