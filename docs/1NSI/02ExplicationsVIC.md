# Comment utiliser *VIC*

[*VIC* (Visual Computer)](https://faculty.runi.ac.il/vic/software/computer/) est un ordinateur minimal utilisable en ligne pour simuler le *langage machine*. Il comporte très peu de composants et ne comprend qu'un nombre très réduit d'instructions. Cette simplification permet de comprendre le **modèle de von Neumann** et les bases du **langage machine**. Dans *VIC*, toutes les données sont des nombres entiers à trois chiffres (de -999 à 999).

## Architecture

L'interface de *VIC* est composée de trois parties, elles-mêmes partagées en plusieurs composants :

- les **composants d'entrée/sortie** (*I/O Units*), avec :
    * un **composant d'entrée** (*Input*) duquel on peut LIRE ;
    * un **composant de sortie** (*Output*) dans lequel on peut ÉCRIRE ;
- un **processeur** (*CPU*), composé de :
    * un **registre d'instruction** (*Instruction Register*) dans lequel est indiquée la prochaine instruction à exécuter ;
    * un **registre de donnée** (*Data Register*) qui contient la donnée à traiter (VIC ne peut traiter qu'une donnée à la fois) ;
    * un **compteur ordinal** (*Program Counter*) qui contient l'adresse en mémoire de l'instruction à exécuter.
- une **mémoire vive** (*Memory*) composée de 100 **cases mémoire** ou **cellules** numérotées de 00 à 99.

## Instructions
Comme les "vrais" ordinateurs, *VIC* ne connaît qu'un petit nombre d'instructions. Elles sont au nombre de dix.

VIC commence son exécution avec l'instructions située dans la case mémoire d'adresse 00. À chaque étape, il exécute l'instruction située dans la case mémoire courante puis passe à la suvante.

### Le langage machine

Le **langage machine** est le langage compris par la machine au niveau des composants. Il s'exprime à l'aide de nombres entiers. Pour faciliter le travail des humains, on utilse un langage appelé **assembleur** qui consiste à remplacer chaque nombre par une expression plus lisible.

### Entrée-sortie
*VIC* comprend deux instructions d'entrée-sortie :

- 800 : LIRE la case courante de Input et mettre sa valeur dans le registre de donnée
- 900 : ÉCRIRE la valeur du registre de données dans la case suivante de Output

!!! example "Premier exemple : lire et afficher"
    Un programme qui lit une donnée puis l'écrit dans *Ouput*. Ce programme s'écrirait ainsi en assembleur :
    ```
    LIRE
    ÉCRIRE
    ```
    ce qui donne, en langage machine de *VIC* :
 
    ```
    800
    900
    ```
    Essayez ! Si vous écrivez n'importe quel nombre dans la premièce cellule de *Input*, ce programme va l'écrire dans *Ouput*. Pour que cela fonction, il faut écrire `800` dans la case mémoire d'adresse 00 et `900` dans celle d'adresse `01`.


### Avec la mémoire

Deux instructions permettent de travailler avec la mémoire vive :

- 3xx CHARGER le contenu de la case mémoire dont l'adresse est xx (où xx représente deux chiffres) dans le registre de donnée depuis
- 4xx ENREGISTRER le contenu du registre de donnée dans la case mémoire dont l'adresse est xx.

!!! example "Amélioration"
    Améliorons le programme précédent : on lit un nombre, on l'enregistre dans la case mémoire 10 puis on l'affiche.
    En assembleur : 
    ```
    LIRE
    ENREGISTRER dans la case mémoire 10
    ÉCRIRE
    ```
    en langage machine de *VIC* :
    ```
    800
    410
    900
    ```

!!! example "Afficher un nombre précis"
    Il n'est pas possible d'afficher le nombre 42. Pour cela, on peut l'écrire à la main dans une zone mémoire (par exemple celle dont l'adresse est 02) puis programmer ainsi :
    ```
    CHARGER le contenu de la case 02
    ÉCRIRE
    ```
    ce qui donne en langage machine les trois lignes suivantes :
    ```
    310
    900
    42
    ```


### Arithmétique

*VIC* ne connaît que deux opérations : addition et soustraction. À chaque fois, il travaille avec une case mémoire d'adresse xx et le registre de donnée.

- 1xx AJOUTE le nombre stocké dans la case mémoire d'adresse xx au registre de donnée ;
- 2xx SOUSTRAIT le nombre stocké dans la case mémoire d'adresse xx au registre de donnée.

!!! warning "Attention"
    L'ordre des nombres pour la soustraction est important.

!!! example "Addition"
    Pour additionner deux nombres donnés en entrée, il faudra en enregistrer un en mémoire, par exemple dans la case 09.
    ```
    LIRE (le premier nombre)
    ENREGISTRER dans la case mémoire 09
    LIRE (le deuxième)
    AJOUTER le nombre de la case 09 au registre de donnée
    ÉCRIRE
    ```
    en langage machine :
    ```
    800
    410
    800
    110
    900
    ```

### Contrôle du flux
Toutes les instructions conditionnelles et les boucles se font en langage machine avec des instructions de **contrôle de flux** qui consistent à passer, non pas à l'instruction suivante, mais à ALLER à une certaine case mémoire.

La plus simple est :

- 5xx ALLER exécuter l'instruction située dans la case mémoire xx.

!!! example "Boucle infinie"
    Pour exécuter une boucle infinie, on dit à *VIC* d'aller exécuter l'instruction de la case 01. Cette instruction lui dit d'aller à la case 00.
    ```
    ALLER à la case 01
    ALLER à la case 00
    ```
    en langage machine :
    ```
    501
    500
    ```
    Vous verrez le **compteur ordinal** (*Program Counter*) alterner entre 0 et 1. Pour arrêter *VIC*, appuyez sur le bouton en forme de carré.

Pour faire des tests, *VIC* possède deux autres instructions de contrôle de flux :

- 6xx ALLER_ZÉRO qui envoie à la case mémoire xx si le registre de donnée contient la valeur 0. Dans les autres cas, *VIC* passe à la case mémoire suivante comme d'habitude.
- 7xx ALLER_POS qui envoie à la case mémoire xx si le registre de donnée contient une valeur strictement positive. Dans les autres cas, *VIC* passe à la case mémoire suivante comme d'habitude.

