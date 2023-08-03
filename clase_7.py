class Perro:

    especie = "Mamifero"

    #El constructor
    def __init__(self, nombre, raza):
        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("Este perro acaba de ladrar!")

# self hace referencia a la instancia de la clase

    def caminar(self, pasos):
        print(f"Este perro acaba de caminar {pasos} pasos")

perro1 = Perro("Sammy", "Caniche")

print(f"Su nombre es: {perro1.nombre}")
print(f"Su raza es: {perro1.raza}")
print(f"Es un: {perro1.especie}")

# print(perro1.ladrar())
# print(perro1.caminar(10))

################################################################################################################################


