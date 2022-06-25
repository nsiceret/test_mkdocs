# Définition

Des enfants, dans une file d'attente, vont se faire vacciner ; des mannequins, dans un défilé de mode, sont photographiées ; des voitures, dans un embouteillage, vont sortir de la rue... toutes ces situations ont un point commun : les données (enfants, mannequins, voitures) sont rangées dans un certain ordre et obéissent à la règle "premier arrivé, premier servi". Cette situation s'appelle une ***file***.

!!! definition "File : définition"
    Une ***file*** est constituée d'éléments placés les uns à la suite des autres. Elle peut éventuellement être vide. On peut faire quatre opérations sur une file :

    - créer une file vide ;
    - tester si une file est vide ;
    - ajouter un élément à la fin de la file : on dit ***enfiler*** ;
    - enlever l'élément qui est au début de la file : ***défiler*** .

Les files suivent le principe ***FIFO*** (de l'anglais ***First In, First Out***) qui signifie ***premier arrivé, premier sorti***. Pour traiter un élément de la file, il faut le défiler : on ne peut traiter que l'élément situé en tête et il faut l'enlever de la file.


!!! example "Premier exemple"
    Supposons que trois mannequins, Noa, Sam et Tim soient sur le podium, dans cet ordre. Les flèches indiquent dans quel sens avance le défilé.
    ``` mermaid
    graph RL
      Sam --> Tim;
      Tim --> Noa;
    ```

    La file a pu être constituée ainsi :

    1. Préparation du podium (créer une file vide)
    2. Ajout de Noa à la file
    3. Ajout de Tim à la file (derrière Noa)
    4. Ajout de Sam à la file (derrière Tim) 

    Si nous *défilons* la file, c'est le premier élément arrivé qui est enlevé, on obtient :

    ```mermaid
    graph RL
      Sam --> Tim;
    ```
    Si Jo arrive, la file devient :
    ```mermaid
    graph RL
      Sam --> Tim;
      Jo --> Sam;
    ```
    car Jo doit se placer à la fin de la file.

!!! example "Essayez"
    Ci-dessous, une interface Python fournit les fonctions suivantes :

    - `creer_file_vide`
    - `est_vide`
    - `enfiler`
    - `defiler` 

    Avec en plus une fonction `afficher_file` qui vous sera utile.

    Vous pouvez avoir plus d'informations sur une fonction appelée `f` en tapant `help(f)` dans la console. Utilisez l'interface pour créer, modifier et afficher des files.

    {{IDE('essai_file')}}