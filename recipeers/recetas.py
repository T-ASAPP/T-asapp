from typing import List, Tuple
from preparacion import Preparacion
from ingrediente import Ingrediente
from tipo_receta import TipoReceta

class Receta:
    def __init__(self, nombre: str, 
                 lista_ingredientes: List[Tuple[Ingrediente, float]] = [], 
                 pasos_preparacion: List[Preparacion] = [], 
                 tipo: TipoReceta = None):
        self.nombre = nombre
        self.lista_ingredientes = lista_ingredientes
        self.pasos_preparacion = pasos_preparacion
        self.tipo = tipo
    
    def agregar_ingrediente(self, ingrediente: Ingrediente, cantidad: float):
        self.lista_ingredientes.append((ingrediente, cantidad))
    
    def agregar_paso_preparacion(self, paso: Preparacion):
        self.pasos_preparacion.append(paso)
    
    def asignar_tipo(self, tipo: TipoReceta):
        self.tipo = tipo
