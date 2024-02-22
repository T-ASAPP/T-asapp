class Liquidos:
    def __init__(self, mililitros=0, litros=0, cucharaditas=0, cucharadas=0):
        self.mililitros = mililitros + (litros * 1000) + (cucharaditas * 5) + (cucharadas * 15)

    def a_litros(self):
        return self.mililitros / 1000

    def a_cucharaditas(self):
        return self.mililitros / 5

    def a_cucharadas(self):
        return self.mililitros / 15


class Solidos:
    def __init__(self, gramos=0, kilogramos=0, cucharaditas=0, cucharadas=0):
        self.gramos = gramos + (kilogramos * 1000) + (cucharaditas * 5) + (cucharadas * 15)

    def a_kilogramos(self):
        return self.gramos / 1000

    def a_cucharaditas(self):
        return self.gramos / 5

    def a_cucharadas(self):
        return self.gramos / 15


class Especias:
    def __init__(self, pizcas=0, cucharaditas=0, gramos=0):
        # Consideramos que una pizca es aproximadamente 1/8 de cucharadita
        self.gramos = gramos + (cucharaditas * 5) + (pizcas * (5/8))

    def a_cucharaditas(self):
        return self.gramos / 5

    def a_pizcas(self):
        return self.gramos / (5/8)


class OtrasMedidas:
    def __init__(self, tazas=0, unidades=0, punados=0, vasos_yogurt=0):
        self.tazas = tazas
        self.unidades = unidades
        self.punados = punados
        self.vasos_yogurt = vasos_yogurt  # Podríamos definir una conversión estándar si es necesario

# Ejemplo de uso
liquido = Liquidos(litros=1)
print(liquido.a_cucharadas(), "cucharadas")

solido = Solidos(gramos=500)
print(solido.a_kilogramos(), "kilogramos")

especia = Especias(pizcas=3)
print(especia.a_gramos(), "gramos")

otras = OtrasMedidas(tazas=2)
print(otras.tazas, "tazas")

