from typing import List, Tuple
from preparacion import Preparacion
from ingrediente import Ingrediente

class Receta:
    def __init__(self, nombre: str, 
                 lista_ingredientes: List[Tuple[Ingrediente, float]] = [], 
                 pasos_preparacion: List[Preparacion] = []):
        self.nombre = nombre
        self.lista_ingredientes = lista_ingredientes
        self.pasos_preparacion = pasos_preparacion
