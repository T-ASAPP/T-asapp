class Ingrediente:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def __repr__(self):
        return f"Ingrediente({self.nombre})"
    
class CantidadIngrediente:
    def __init__(self, ingrediente: Ingrediente, cantidad: float, unidad_medida: str):
        self.ingrediente = ingrediente
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida

    def __repr__(self):
        return f"CantidadIngrediente({self.ingrediente}, {self.cantidad}, {self.unidad_medida})"    