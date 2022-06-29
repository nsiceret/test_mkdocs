# Un petit bonjour

Étudions un exemple très simple, celui qu'on voit souvent dans la toute première leçon quand on apprend à programmer en Python :

``` python
"Bonjour !"
```

Quand on tape ce code dans un éditeur Python et qu'on l'exécute, on ne créé pas seulement une chaîne de 9 caractères, on créé un ***objet*** de la ***classe*** `str`. Qu'y a-t-il dans cet objet ?

Pour le savoir, tapez `dir("Bonjour !")` dans la console, puis ++enter++

{{terminal()}}

Tous les objets d'une classe, même s'ils sont différents, sont automatiquement créés avec des fonctions (ou ***méthodes***) et des valeurs (ou ***attributs***) embarquées (on dit ***encapsulées***). La fonction python `dir` renvoie la liste de toutes les méthodes et tous les attributs encapsulés dans un objet.

On accède à une méthode ou un attribut sous la forme `<objet>.<méthode>` avec un point entre l'objet et la méthode.
Par exemple, essayez dans la console : 

- pour appliquer la méthode `lower` à `"OK"`, tapez `"OK".lower()`
- pour avoir l'aide de la méthode `lower` qui est encapsulée dans `"Bonjour !"`, tapez `help("Bonjour !".lower)`. Cela affichera le **docstring** de cette méthode, en anglais ("lowercase" signifie "en minuscule").

L'idée de la ***programmation orientée objet*** est de faire en sorte que, dès sa création, un objet partage des caractéristiques communes avec tous ceux de sa classe et qu'il contienne "tout ce dont il a besoin" pour évoluer.
