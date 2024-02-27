class Receta:
    def __init__(self, nombre: str, listaIngredientes: List[Tuple[Ingrediente, float]], pasosPreparacion: List[Preparacion]):
        self.nombre = nombre
        self.listaIngredientes = listaIngredientes
        self.pasosPreparacion = pasosPreparacion

class Ingrediente:
  def __init__(self, nombre: set[str], medida: str):
    self.nombre = nombre
    self.medida = medida   

class Preparacion:
    def __init__(self, verbos_cocinado: set[str], ingredientes: str, instrucciones: str):

        self.verbos_cocinado = verbos_cocinado
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones