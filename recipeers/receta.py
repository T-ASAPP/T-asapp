"""Este módulo contiene la definición de la clase Receta para representar recetas culinarias."""
from typing import List, Tuple
from preparacion import Preparacion
from ingrediente import Ingrediente

class Receta:
    """Clase que representa una receta culinaria.

    Una receta consta de un nombre, una lista de ingredientes junto con sus cantidades,
    y una lista de pasos de preparación.

    Attributes:
        nombre (str): El nombre de la receta.
        lista_ingredientes (List[Tuple[Ingrediente, float]]): Una lista de tuplas que 
            contienen los ingredientes necesarios para la receta junto con las cantidades
            requeridas de cada uno.
        pasos_preparacion (List[Preparacion]): Una lista de objetos de la clase Preparacion
            que describen los pasos necesarios para preparar la receta.

    """

    def __init__(self, nombre: str, 
                 lista_ingredientes: List[Tuple[Ingrediente, float]] = [], 
                 pasos_preparacion: List[Preparacion] = []):
        """Inicializa una nueva receta con su nombre, lista de ingredientes y pasos de preparación.

        Args:
            nombre (str): El nombre de la receta.
            lista_ingredientes (List[Tuple[Ingrediente, float]], optional): Una lista de tuplas que 
                contienen los ingredientes necesarios para la receta junto con las cantidades
                requeridas de cada uno. Por defecto, es una lista vacía.
            pasos_preparacion (List[Preparacion], optional): Una lista de objetos de la clase Preparacion
                que describen los pasos necesarios para preparar la receta. Por defecto, es una lista vacía.
        """
        self.nombre = nombre
        self.lista_ingredientes = lista_ingredientes
      
