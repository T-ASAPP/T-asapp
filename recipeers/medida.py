from enum import Enum

class Medida(Enum):
    kg = "Kilogramos"
    g = "Gramos"
    l = "Litros"
    ml = "Mililitros"
    unidades = "Conteo de elementos individuales"
    cucharadas = "Cucharadas"
    cucharaditas = "Cucharaditas"
    pizcas = "Pizcas para cantidades muy pequeñas"
    pellizcos = "Equivalente a la cantidad que se puede coger con el dedo pulgar e índice"
    vasos_de_yogurt = "Vasos de yogurt (125 ml aprox)"
    al_gusto = "Al gusto (saonar)"

def agregar_medidas(conjunto_medidas, nuevas_medidas):
    """
    Agrega nuevas medidas al conjunto de medidas existente.

    :param conjunto_medidas: Conjunto (set) de medidas existente.
    :param nuevas_medidas: Lista de nuevas medidas a agregar.
    """
    for nueva_medida in nuevas_medidas:
        conjunto_medidas.add(nueva_medida)

# Conjunto de medidas inicial
conjunto_medidas = {
    Medida.kg,  
    Medida.g,   
    Medida.l,   
    Medida.ml,  
    Medida.unidades,  
    Medida.cucharadas,  
    Medida.cucharaditas,  
    Medida.pizcas,  
    Medida.pellizcos,  
    Medida.vasos_de_yogurt,  
    Medida.al_gusto  
}

# Lista de nuevas medidas vacía
nuevas_medidas = []

# Intentar agregar nuevas medidas al conjunto (no habrá cambios)
agregar_medidas(conjunto_medidas, nuevas_medidas)
