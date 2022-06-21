#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:03:54 2022

@author: laurent
"""

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