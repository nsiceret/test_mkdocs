# Définition

Comme les files, les ***piles*** sont des structures de données linéaires : des éléments sont placés les uns à la suite des autres. Comme pour les files, pour examiner un élément d'une pile, il faut l'enlever. La différence est que, dans une pile, l'élément enlevé est celui qui est en haut de la pile, c'est-à-dire le dernier qui a été posé sur la pile. Une pile suit le principe ***FILO*** (***First In, Last Out***) : ***premier arrivé, dernier sorti***.

!!! definition "Pile : définition"
    Une ***pile*** est constituée d'éléments placés les uns "sur" les autres. Elle peut éventuellement être vide. On peut faire quatre opérations sur une file :

    - créer une pile vide ;
    - tester si une pile est vide ;
    - ajouter un élément en haut de la pile : on dit ***empiler*** ;
    - enlever l'élément qui en haut de la file (donc le dernier ajouté) : ***dépiler*** .

!!! example "Un exemple en informatique : l'historique"
    En informatique, on utilise les piles pour enregistrer un historique. Supposons qu'un logiciel enregistre chaque mot qu'on tape dans une pile d'historique. Si on tape "Salut les gens", il va exécuter l'algorithme suivant :
    ```
    créer une pile vide HISTORIQUE
    empiler "Salut" sur HISTORIQUE
    empiler "les" sur HISTORIQUE
    empiler "gens" sur HISTORIQUE
    ```
    on obtient la pile :
    ``` mermaid
    classDiagram
    class HISTORIQUE{
      gens
      les
      Salut
    }
    ```
    Si on appuie sur ++ctrl+z++, cela revient à :
    ```
    dépiler HISTORIQUE
    ```
    et on obtient :
    ``` mermaid
    classDiagram
    class HISTORIQUE{
      les
      Salut
    }
    ```
    Si maintenant on écrit "amis" dans ce logiciel, cela exécute 
    ```
    empiler "amis" sur HISTORIQUE
    ``` 
    et la pile devient :
    ``` mermaid
    classDiagram
    class HISTORIQUE{
      amis
      les
      Salut
    }
    ```


    