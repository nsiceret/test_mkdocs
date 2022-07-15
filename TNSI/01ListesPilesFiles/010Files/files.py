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
    Enfile `item` à la fin de `file`
    
    Exemple : enfiler(F,7) ajoute le nombre 7 à la fin de la file F
    """
    file.append(item)
      
def defiler(file):
    """
    Défile la file et renvoie l'élément enlevé
    
    exemple : x = defiler(F) permet de récupérer le premier
    élément de la file F dans une variable x.
    """
    assert not est_vide(file),"on ne peut pas défiler une file vide"
    return file.pop(0)    #fonction Python qui enlève et renvoie le premier élément d'une 'list'

def afficher_file(file):
    """
    Afficher `file` dans la console
    """
    if est_vide(file):
        print('La file est vide')
    else:
        print('(fin) '+'->'.join(map(str,list(reversed(file))))+' (début)')