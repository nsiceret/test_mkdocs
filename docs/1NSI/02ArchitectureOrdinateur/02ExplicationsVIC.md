# Comment utiliser *VIC*

[*VIC* (Visual Computer)](https://faculty.runi.ac.il/vic/software/computer/) est un ordinateur minimal utilisable en ligne pour simuler le *langage machine*. Il comporte très peu de composants et ne comprend qu'un nombre très réduit d'instructions. Cette simplification permet de comprendre le **modèle de von Neumann** et les bases du **langage machine**. Dans *VIC*, toutes les données sont des nombres entiers à trois chiffres (de -999 à 999).

## Architecture

L'interface de *VIC* est composée de trois parties, elles-mêmes partagées en plusieurs composants :

- les **composants d'entrée/sortie** (*I/O Units*), avec :
    * un **composant d'entrée** (*Input*) dans lequel vous pourrez écrire des nombres pour tester vos programmes ;
    * un **composant de sortie** (*Output*) dans lequel le programme peut ÉCRIRE un nombre;
- un **processeur** (*CPU*), composé de :
    * un **registre d'instruction** (*Instruction Register*) dans lequel est indiquée la prochaine instruction à exécuter ;
    * un **registre de données** (*Data Register*) qui contient la donnée à traiter (VIC ne peut traiter qu'une donnée à la fois) ;
    * un **compteur ordinal** (*Program Counter*) qui contient l'adresse en mémoire de l'instruction à exécuter.
- une **mémoire vive** (*Memory*) composée de 100 **cases mémoire** ou **cellules** numérotées de 00 à 99.

## Instructions
Comme les "vrais" ordinateurs, *VIC* ne connaît qu'un petit nombre d'instructions. Elles sont au nombre de dix.

VIC commence son exécution avec l'instructions située dans la case mémoire d'adresse 00. À chaque étape, il exécute l'instruction située dans la case mémoire courante puis passe à la suvante.

Le programme s'arrête lorsqu'il rencontre une case mémoire vide ou, ce qui revient au même, qui contient le nombre 0. Nous avons donc notre première instruction en langage machine :

- 000 : STOP arrêter le programme.

### Le langage machine

Le **langage machine** est le langage compris par la machine au niveau des composants. Il s'exprime à l'aide de nombres entiers. Pour faciliter le travail des humains, on utilse un langage appelé **assembleur** qui consiste à remplacer chaque nombre par une expression plus lisible.

### Entrée-sortie
*VIC* comprend deux instructions d'entrée-sortie :

- 800 : LIRE la case courante de Input et mettre sa valeur dans le registre de données
- 900 : ÉCRIRE la valeur du registre de données dans la case suivante de Output

!!! example "Premier exemple : lire et afficher"
    Un programme qui lit une donnée puis l'écrit dans *Ouput*. Ce programme s'écrirait ainsi en assembleur :
    ```
    LIRE
    ÉCRIRE
    STOP
    ```
    ce qui donne, en langage machine de *VIC* :
 
    ```
    800
    900
    000
    ```
    Essayez ! Si vous écrivez n'importe quel nombre dans la premièce cellule de *Input*, ce programme va l'écrire dans *Ouput*. Pour que cela fonction, il faut écrire `800` dans la case mémoire d'adresse 00 et `900` dans celle d'adresse `01`.

Dans la suite, nous ommettrons la ligne `000 STOP` pour alléger les programmes.


### Avec la mémoire

Deux instructions permettent de travailler avec la mémoire vive :

- 3xx : CHARGER le contenu de la case mémoire dont l'adresse est xx (où xx représente deux chiffres) dans le registre de données depuis
- 4xx : ENREGISTRER le contenu du registre de données dans la case mémoire dont l'adresse est xx.

!!! example "Affichage inverse"
    On veut lire deux nombres, puis les afficher dans l'ordre inverse : d'abord le deuxième nombre entré, puis le premier. Pour cela, il faut garder le premier nombre en mémoire, par exemple dans la case 10.
    En assembleur : 
    ```
    LIRE
    ENREGISTRER dans la case mémoire 10
    LIRE
    ÉCRIRE
    CHARGER le nombre de la case mémore 10
    ÉCRIRE
    ```
    en langage machine de *VIC* :
    ```
    800
    410
    800
    900
    310
    900
    ```

### Arithmétique

*VIC* ne connaît que deux opérations : addition et soustraction. À chaque fois, il travaille avec une case mémoire d'adresse xx et le registre de données.

- 1xx : AJOUTER le nombre stocké dans la case mémoire d'adresse xx au registre de données ;
- 2xx : SOUSTRAIRE le nombre stocké dans la case mémoire d'adresse xx au registre de données.

!!! warning "Attention"
    L'ordre des nombres pour la soustraction est important.

!!! example "Addition"
    Pour additionner deux nombres donnés en entrée, il faudra en enregistrer un en mémoire, par exemple dans la case 09.
    ```
    LIRE (le premier nombre)
    ENREGISTRER dans la case mémoire 09
    LIRE (le deuxième)
    AJOUTER le nombre de la case 09 au registre de données
    ÉCRIRE
    ```
    en langage machine :
    ```
    800
    409
    800
    109
    900
    ```

### Contrôle du flux

Toutes les instructions conditionnelles et les boucles se font en langage machine avec des instructions de **contrôle de flux** qui consistent à passer, non pas à l'instruction suivante, mais à ALLER à une certaine case mémoire.

La plus simple est :

- 5xx : ALLER exécuter l'instruction située dans la case mémoire xx.

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

- 6xx : ALLER_ZÉRO qui envoie à la case mémoire xx si le registre de données contient la valeur 0. Dans les autres cas, *VIC* passe à la case mémoire suivante comme d'habitude.
- 7xx : ALLER_POS qui envoie à la case mémoire xx si le registre de données contient une valeur strictement positive. Dans les autres cas, *VIC* passe à la case mémoire suivante comme d'habitude.

!!! example "Liste de nombres positifs"
    On voudrait afficher une liste de nombres positifs donnés en entrée. Il va donc falloir LIRE, puis ALLER à une cellule indiquant d'écrire et de revenir au début du programme si le nombre lu est positif. Si le nombre n'est pas positif, on passe à la cellule suivante qui arrête le programme.
    En assembleur :
    ```
    LIRE
    ALLER_POS à 03
    STOP
    ÉCRIRE
    ALLER à 0
    ```
    en langage machine :
    ```
    800
    703
    000
    900
    500
    ```
    
   
