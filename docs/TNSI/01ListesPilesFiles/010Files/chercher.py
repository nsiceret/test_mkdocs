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
def chercher(file,cible):
    trouve = False
    while (not trouve) and (not est_vide(file)):
        e = defiler(file)
        if e == cible:
            trouve = True
    return trouve