actividades =[
    ("A",1, 4),
    ("B",4, 5),
    ("C",0, 6),
    ("D",5, 7),
    ("E",8, 9),
    ("F",5, 9)
]

actividades.sort(key=lambda x:x[2])

seleccionadas = []
fin_actual = 0

for actividad in actividades:
    nombre, inicio, fin = actividad
    if inicio>= fin_actual:
        seleccionadas.append(nombre)
        fin_actual = fin
    
print("las actividades seleccionadas son ", seleccionadas)
