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