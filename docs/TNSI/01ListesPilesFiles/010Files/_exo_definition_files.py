from files import *
from random import randint

cible = []


def tester_F1(F1):
    afficher_test(len(F1)>0, "F1 est vide !",1)
    g = [5,4,3,9]
    afficher_test(len(F1)==len(g), f"F1 n'a pas le bon nombre d'éléments : {len(F1)} au lieu de {len(g)}",2)
    for i in range(len(F1)):
        afficher_test(F1[i]==g[i],f"l'élément n°{i+1} n'est pas correct : {F1[i]} au lieu de {g[i]}",i+3)
    print("---- votre file ----")
    afficher_file(F1)
    print("---- file demandée ----")
    afficher_file(g)
        
        
def afficher_test(test,msg,no):
    if test:
        print(f"test n°{no} réussi ! ")
    else:
        print(f"test n°{no} échoué : {msg}")
        
        
def creer_exo():
    long = randint(3,7)
    while len(cible) > 0:
        cible.pop()
    for i in range(long):
        cible.append(randint(1,20))
    print("Vous devez, avec les fonctions du module `files`, créer la liste suivante :")
    afficher_file(cible)
    print("Votre file doit être affectée à une variable `F2`")
    
def tester_files(F2):
    afficher_test(len(F2)>0, "F2 est vide !",1)
    afficher_test(len(F2)==len(cible), f"F2 n'a pas le bon nombre d'éléments : {len(F2)} au lieu de {len(cible)}",2)
    for i in range(len(F2)):
        afficher_test(F2[i]==cible[i],f"l'élément n°{i+1} n'est pas correct : {F2[i]} au lieu de {cible[i]}",i+3)
    print("---- votre file ----")
    afficher_file(F2)
    print("---- file demandée ----")
    afficher_file(cible)
    
    