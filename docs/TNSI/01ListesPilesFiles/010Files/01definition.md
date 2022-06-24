# Définition


Des enfants, dans une file d'attente, vont se faire vacciner ; des mannequins, dans un défilé de mode, sont photographiées ; des voitures, dans un embouteillage, vont sortir de la rue... toutes ces situations ont un point commun : les données (enfants, mannequins, voitures) sont rangées dans un certain ordre et obéissent à la règle "premier arrivé, premier servi". Cette situation s'appelle une ***file***.

Un **type abstrait de données** est un modèle correspondant à de nombreuses situations concrètes. Dans ce modèle abstrait, on garde uniquement les propriétés essentielles communes à toutes ces situations. L'intérêt est qu'en étudiant un modèle simple et abstrait, on peut résoudre de très nombreux problèmes concrets qui correspondent à ce modèle.

Quelle sont les propriétés minimales du type abstrait de données "file" ?

!!! definition "File : définition"
    Une ***file*** est constituée d'éléments ou éventuellement être vide. On peut faire quatre opérations sur une file :

    - créer une file vide ;
    - tester si une file est vide ;
    - ajouter un élément à la fin de la file : on dit ***enfiler*** ;
    - enlever l'élément qui est au début de la file : ***défiler*** .

Les files suivent le principe ***FIFO*** (de l'anglais ***First In, First Out***) qui signifie ***premier arrivé, premier sorti***. Pour traiter un élément de la file, il faut le défiler : on ne peut traiter que l'élément situé en tête et il faut l'enlever de la file.


!!! example "Premier exemple"
    Ci-dessous le schéma d'une file. Supposons que trois éléments, Noa, Sam et Tim soient enfilés dans cet ordre. Nous obtenons la file suivante :
    ``` mermaid
    graph LR
      Noa --> Sam;
      Sam --> Tim;
    ```
    Si nous *défilons* la file, c'est le premier élément arrivé qui est enlevé :
    ```mermaid
    graph LR
      Sam --> Tim;
    ```
    Si Jo arrive, la file devient :
    ``` mermaid
    graph LR
      Sam --> Tim;
      Tim --> Jo;
    ```
    car Jo doit se placer à la fin de la file.

!!! example "Essayez"
    Ci-dessous, une interface Python fournit les fonctions suivantes :

    - `creer_file_vide()`
    - `est_vide`
    - `enfiler`
    - `defiler` 

    Avec en plus une fonction `afficher_file` qui vous sera utile.

    Vous pouvez avoir plus d'informations sur une fonction appelée `f` en tapant `help(f)` dans la console. Utilisez l'interface pour créer modifier et afficher des files.

    {{IDE('essai_file')}}