from typing import List, Dict

from recetas import Receta
from recetas_tradicionales import TipoReceta

class Recetario:
 def __init__(self):
   self._recetas: Dict[str, Receta] = {}
