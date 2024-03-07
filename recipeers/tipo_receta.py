"""Módulo que contiene la definición de la clase TipoReceta.

Este módulo proporciona la implementación de la clase TipoReceta, que representa un tipo de receta.
"""

class tipo_receta:
    """Clase que representa un tipo de receta.

    Attributes:
        nombre (str): El nombre del tipo de receta.
    """

    def __init__(self, nombre: str):
        """Inicializa una instancia de la clase tipo_receta.

        Args:
            nombre (str): El nombre del tipo de receta.
        """
        self.nombre = nombre
