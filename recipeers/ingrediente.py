"""Módulo que contiene la definición de la clase Ingrediente.

Este módulo proporciona la implementación de la clase Ingrediente, que representa un ingrediente utilizado en recetas.
"""

from medida import Medida

class Ingrediente:
    """Clase que representa un ingrediente utilizado en una receta.

    Contiene información sobre el nombre del ingrediente y la medida en la que se utiliza.

    Attributes:
        nombre (str): El nombre del ingrediente.
        medida (Medida): El objeto de la clase Medida que representa la unidad de medida
            en la que se utiliza el ingrediente.

    """

    def __init__(self, nombre: str, medida: str):
        """Inicializa un nuevo ingrediente con su nombre y medida.

        Args:
            nombre (str): El nombre del ingrediente.
            medida (Medida): El objeto de la clase Medida que representa la unidad de medida
                en la que se utiliza el ingrediente.
        """
        self.nombre = nombre
        self.medida = medida
