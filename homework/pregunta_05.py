"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        filas = [linea.strip().split("\t") for linea in f if linea.strip()]
    extremos = {}
    for fila in filas:
        letra = fila[0]
        valor = int(fila[1])
        if letra not in extremos:
            extremos[letra] = [valor, valor]  # [max, min]
        else:
            if valor > extremos[letra][0]:
                extremos[letra][0] = valor
            if valor < extremos[letra][1]:
                extremos[letra][1] = valor
    return sorted((letra, v[0], v[1]) for letra, v in extremos.items())

print(pregunta_05())
