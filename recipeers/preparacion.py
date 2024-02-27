from ingrediente import Ingrediente

class Preparacion:
    def __init__(self, verbos_cocinado: set[str], ingredientes: str, instrucciones: str):
       
        self.verbos_cocinado = verbos_cocinado
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones