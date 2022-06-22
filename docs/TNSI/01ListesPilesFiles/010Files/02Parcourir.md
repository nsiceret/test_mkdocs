# Parcourir une file

Pour bien comprendre le concept de file, il faut s'imaginer une file d'attente avec une seule personne responsable, qui se trouve dans un guichet en tête de file. Il lui est impossible de savoir directement qui est la troisième personne qui attend ou même combien de personnes attendent. La personne au gichet peut seulement enlever l'enfant en tête de la file pour connaître son nom.

Pour savoir combien d'enfants attendent, on les fait tous sortir, un par un, dans l'ordre, en les comptant. Cela détruit la file.

Si cela vous paraît étrange, imaginez une file d'attente plus stricte que des enfants : à la douane. Les voyageurs passent un par un, dans l'ordre, devant la personne qui examine les bagages.

## Exemples

!!! example "Exemple : Longueur d'une file"
    Ci-dessous, une fonction `longueur` qui calcule la longueur d'une file donnée en paramètre. Étudiez bien son code pour le comprendre.

    {{IDE('longueur')}}

!!! example "Exemple : Copier une file"
    Ci-dessous, une fonction `copier` qui copie le contenu d'une file dans une autre file et renvoie cette dernière. À noter que la première est détruite.

    {{IDE('copier')}}

Vous pouvez vous inspirer des deux exemples pour résoudre le problème suivant.

## Exercices

!!! exercice
    Programmez une fonction `longueur_nd` qui calcule la longueur d'une file, mais sans la détruire. 

    {{IDE('longueur_nd')}}

!!! exercice
    Programmez une fonction `copier_nd` qui calcule la longueur d'une file, mais sans la détruire. 

    {{IDE('copier_nd')}}
