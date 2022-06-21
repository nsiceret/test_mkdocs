#--- HDR ---#
def creer_pile_vide():
    """
    Renvoie un objet de type list vide pour simuler une pile vide
    """
    return []

def est_vide(pile):
    """
    Renvoie True si et seulement si pile est vide
    """
    return len(pile) == 0

def empiler(pile,item):
    """
    Empile item sur pile
    """
    pile.append(item)
      
def depiler(pile):
    """
    Dépile la pile et renvoie l'élément enlevé
    """
    assert not est_vide(pile),"on ne peut pas dépiler une pile vide"
    return pile.pop()    #fonction Python qui enlève et renvoie le dernier élément d'une 'list'
def afficher_pile(p):
    q  = creer_pile_vide()
    print("---pile---")
    while not est_vide(p):
        e = depiler(p)
        empiler(q,e)
        print(e)
    while not est_vide(q):
        e = depiler(q)
        empiler(p,e)
#--- HDR ---#
P = creer_pile_vide()
empiler(P,12)