from itertools import combinations

numeros = [3, 7, 10, 2,8]
limite = 15

mejor_suma = 0
mejor_conjunto = []


for r in range(len(numeros)+1):
    for combo in combinations(numeros,r):
        suma = sum(combo)
        if suma <= limite and suma > mejor_suma:
            mejor_conjunto = combo
            mejor_suma = suma

print("mejor combinacion: ", mejor_conjunto)
print("suma: ",mejor_suma)
#algoritmo voraces
