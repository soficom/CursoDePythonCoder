class Auto():
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def __str__(self):
        return f"Soy un auto de color {self.color} y tengo {self.puertas} puertas"

mi_auto = Auto("Rojo", 4)

print(mi_auto)