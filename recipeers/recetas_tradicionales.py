class Receta:
    def __init__(self, nombre: str, ingredientes: List[Ingrediente], pasos: List[Paso], tradicional: bool = False):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos
        self.tradicional = tradicional

