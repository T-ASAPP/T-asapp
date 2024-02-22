class Receta:
  def __init__(self, nombre, descripcion, ingredientes, pasos, tiempo_preparacion, imagen=None):
    """ Clase que representa una receta.
      Args:
      nombre: Nombre de la receta.
      descripcion: Descripción breve de la receta.
      ingredientes: Lista de ingredientes con sus cantidades.
      pasos: Lista de instrucciones para preparar la receta.
      tiempo_preparacion: Tiempo total de preparación en minutos.
      imagen: Ruta a una imagen (opcional).
    """
    
    self.nombre = nombre
    self.descripcion = descripcion
    self.ingredientes = ingredientes
    self.pasos = pasos
    self.tiempo_preparacion = tiempo_preparacion
    self.imagen = imagen

  def __str__(self):
    """
    Devuelve una representación textual de la receta.
    """
    return f"""
    **Receta:** {self.nombre}

    **Descripción:** {self.descripcion}

    **Ingredientes:**
    {', '.join(f'- {ingrediente}' for ingrediente in self.ingredientes)}

    **Preparación:**
    {'\n'.join(f'{paso}.' for paso in self.pasos)}

    **Tiempo de preparación:** {self.tiempo_preparacion} minutos
    """

  def imprimir(self):
    """
    Imprime la receta por consola.
    """
    print(self.__str__())

# Ejemplo de uso
receta = Receta(
  nombre="Tortilla de patatas",
  descripcion="Receta tradicional española de tortilla de patatas.",
  ingredientes=[
    "5 patatas medianas",
    "2 cebollas",
    "6 huevos",
    "Aceite de oliva virgen extra",
    "Sal al gusto"
  ],
  pasos=[
    "Pelar y cortar las patatas en rodajas finas.",
    "Cortar la cebolla en juliana.",
    "Calentar aceite en una sartén y freír las patatas hasta que estén doradas.",
    "Escurrir las patatas y reservarlas.",
    "En la misma sartén, freír la cebolla hasta que esté transparente.",
    "Batir los huevos con sal al gusto.",
    "Añadir las patatas y la cebolla a los huevos batidos y mezclar bien.",
    "Calentar un poco de aceite en la sartén y verter la mezcla.",
    "Cocinar la tortilla a fuego lento durante unos minutos por cada lado hasta que esté cuajada.",
    "Servir la tortilla caliente o fría."
  ],
  tiempo_preparacion=30
)

receta.imprimir()
