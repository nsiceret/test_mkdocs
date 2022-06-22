#--- HDR ---#
import random
t = [1 for i in range(random.randint(8,20))]
l = len(t)
#--- HDR ---#
assert longueur_nd([])==0
assert longueur_nd(t)==l
assert not est_vide(t),"la file est détruite !"