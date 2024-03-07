class Medida:
    """Clase que representa las medidas utilizadas en recetas.

    Contiene un diccionario que mapea las abreviaturas de las medidas a sus nombres completos
    o descripciones correspondientes.

    Attributes:
        medidas (dict): Un diccionario que mapea las abreviaturas de las medidas a sus nombres
            completos o descripciones correspondientes.

    """

    def __init__(self):
        """Inicializa un nuevo objeto de la clase Medida con un diccionario predefinido de medidas."""
        self.medidas = {
            "kg": "Kilogramo",
            "g": "Gramo",
            "l": "Litro",
            "ml": "Mililitro",
            "unidad": "Conteo de elemento individual",
            "cucharada": "Cuchara sopera",
            "cucharadita": "Cuchara pequeña",
            "pizca": "Para cantidades muy pequeñas",
            "pellizco": "Equivalente a la cantidad que se puede coger con el dedo pulgar e índice",
            "vaso_de_yogur": "Vaso de yogur (125 ml aprox)",
            "al_gusto": "Al gusto (sazonar)"
        }
