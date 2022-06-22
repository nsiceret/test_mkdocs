# Définition

![Des enfants dans une file](file_enfants.jpg)

Lorsque des enfants attendent pour se faire vacciner, ils se rangent à la queue-leu-leu, dans une **file**. Comment ça se passe ?

D'abord, le personnel installe le lieu d'attente : il faut **créer une file vide** (sans enfant). Ensuite l'enfant 1 arrive, puis l'enfant 2, etc. On peut **ajouter un enfant à la fin de la file**, on dit aussi **enfiler**. Quand le personnel est prêt, il appelle le premier enfant arrivé, puis le deuxième… On ne peut enlever qu'un seul enfant à la fois de la file, celui qui est arrivé en premier : **défiler**. Enfin, lorsque la file est vide, on arrête les vaccins.

!!! definition
    Une **file** est constituée d'éléments. On peut faire quatre opérations sur une file :

    - créer une file vide ;
    - tester si une file est vide ;
    - ajouter (**enfiler**) un élément à la fin de la file ;
    - enlever un élément du début de la file (ou **défiler**).

Les files suivent le principe **FIFO** (de l'anglais *First In, First Out*) : premier arrivé, premier sorti.

!!! example "Essayez"
    Ci-dessous, une interface Python fournit les fonctions suivantes :

    - `creer_file_vide()`
    - `est_vide`
    - `enfiler`
    - `defiler` 

    Avec en plus une fonction `afficher_file` qui vous sera utile.

    Vous pouvez avoir plus d'informations sur une fonction appelée `f` en tapant `help(f)` dans la console. Utilisez l'interface pour créer modifier et afficher des files.

    {{IDE('essai_file')}}