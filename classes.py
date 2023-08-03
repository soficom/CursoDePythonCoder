class Perro:
    especie = "Mamifero" #Atributo de clase

    #El constructor
    def __init__(self,nombre, raza):
        #Atributo de instancia
        self.nombre = nombre
        self.raza = raza

    #Metodo sin argumentos
    def ladrar(self):
        print("Este perro acaba de ladrar!")

        #Metodo con argumentos
    def caminar(self, pasos):
        print(f"Este perro acaba de caminar{pasos}")


perro1 = Perro("Sammys", "caniche")

print(f"Su nombre es: {perro1.nombre}")
print(f"Su razas: {perro1.raza}")
print(f"Es un: {perro1.especie}")

# print(perro1.ladrar())
# print(perro1.caminar(10))

