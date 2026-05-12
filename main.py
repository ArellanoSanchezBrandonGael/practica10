from time import time
from fuerza_bruta import buscador

t0 = time()
con = "H0l4"
buscador(con)
t1 = time()
t2 = round(t1-t0, 6)
print("el tiempo de ejecucion fue de {}".format(t2))

