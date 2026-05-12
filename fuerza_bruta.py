from string import ascii_letters, digits
from itertools import product

caracteres = ascii_letters+digits

def buscador(con):
    archivo = open("combinaciones.txt", "w")

    if 3 <= len(con) <=4:
        for i in range(3,5): #range genera rangos
            for comb in product(caracteres, repeat = 1):
                prueba = "".join(comb) #es una cadena vacìa pq no contiene ningun caracter

            archivo.write(prueba+"\n")
            if prueba == con:
                print("tu contraseña es  {}".format(prueba))
                archivo.close()
                break
    else:
        print("ingresa otra contraseña de longitud entre 3 y 4 caracteres")

