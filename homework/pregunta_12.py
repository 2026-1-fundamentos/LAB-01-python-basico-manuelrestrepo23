"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        filas = [linea.strip().split("\t") for linea in f if linea.strip()]
    sumas = {}
    for fila in filas:
        letra = fila[0]
        total = sum(int(par.split(":")[1]) for par in fila[4].split(","))
        sumas[letra] = sumas.get(letra, 0) + total
    return sumas

print(pregunta_12())