import re


def renombrarFrutas(array):
    array_salida = []
    for e in (array):
        frutassinnumero=re.sub(r"(1|2|3|4)", '',e)
        array_salida.append(frutassinnumero)
        
    return array_salida  