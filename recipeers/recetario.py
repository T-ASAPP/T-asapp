from typing import List, Dict

from receta import Receta
from tipo_receta import Tipo_receta

class Recetario:
 def __init__(self):
   self._recetas: Dict[str, Receta] = {}