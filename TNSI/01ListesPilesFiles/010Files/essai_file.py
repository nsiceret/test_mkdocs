#--- HDR ---#
def creer_file_vide():
    """
    Renvoie une file vide
    """
    return []

def est_vide(file):
    """
    Renvoie True si `file` est vide, sinon renvoie False
    """
    return len(file) == 0

def enfiler(file,item):
    """
    Emfile `item` à la fin de `file`
    """
    file.append(item)
      
def defiler(file):
    """
    Défile la file et renvoie l'élément enlevé
    """
    assert not est_vide(file),"on ne peut pas défiler une file vide"
    return file.pop(0)

def afficher_file(file):
    """
    Afficher `file` dans la console
    """
    print('->'.join(map(str,file)))
#--- HDR ---#

F = creer_file_vide() #une file vide
enfiler(F,3)      # j'enfile le nombre 3 dans F
enfiler(F,5)      # j'enfile le nombre 5 dans F
defiler(F)        # j'enlève... quoi ?
enfiler(F,2)
enfiler(F,8)
afficher_file(F)
