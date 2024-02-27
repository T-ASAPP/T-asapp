from typing import List, Tuple
from preparacion import Preparacion
from ingrediente import Ingrediente

class Receta:
    def __init__(self, nombre: str, 
                 listaIngredientes: List[Tuple[Ingrediente, float]], pasosPreparacion: List[Preparacion]):
        self.nombre = nombre
        self.listaIngredientes = listaIngredientes
        self.pasosPreparacion = pasosPreparacion
