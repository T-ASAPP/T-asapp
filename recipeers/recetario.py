"""Módulo que contiene la definición de la clase Recetario.

Este módulo proporciona la implementación de la clase Recetario, que representa un recetario que contiene recetas.
"""

from typing import Dict
from receta import Receta
from tipo_receta import TipoReceta

class Recetario:
    """Clase que representa un recetario que contiene recetas.

    Un recetario es una colección de recetas organizadas por un identificador único. 
    Permite realizar operaciones como añadir nuevas recetas, eliminar recetas existentes,
    y buscar recetas por su identificador.

    Attributes:
        _recetas (Dict[str, Receta]): Un diccionario que almacena las recetas del recetario,
            donde las claves son los identificadores únicos de las recetas y los valores son
            objetos de la clase Receta.

    """

    def __init__(self):
        """Inicializa un nuevo recetario sin recetas."""
        self._recetas: Dict[str, Receta] = {}
