from typing import Set
from ingrediente import Ingrediente

class Preparacion:
    """Clase que representa los pasos de preparación de una receta.

    Contiene información sobre los verbos de cocinado utilizados, los ingredientes
    involucrados y las instrucciones específicas para llevar a cabo la preparación.

    Attributes:
        verbos_cocinado (Set[str]): Un conjunto de verbos utilizados en el proceso de cocinado.
        ingredientes (str): Una descripción de los ingredientes necesarios para esta preparación.
        instrucciones (str): Las instrucciones detalladas para llevar a cabo la preparación.

    """

    def __init__(self, verbos_cocinado: Set[str], ingredientes: str, instrucciones: str):
        """Inicializa una nueva preparación con los verbos de cocinado, ingredientes e instrucciones dados.

        Args:
            verbos_cocinado (Set[str]): Un conjunto de verbos utilizados en el proceso de cocinado.
            ingredientes (str): Una descripción de los ingredientes necesarios para esta preparación.
            instrucciones (str): Las instrucciones detalladas para llevar a cabo la preparación.
        """
        self.verbos_cocinado = verbos_cocinado
        self.ingredientes = ingredientes
        self.instrucciones = instrucciones
