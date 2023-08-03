def saludar():
    print("saludo desde la funcion")

saludar()


def test():
    variable_test= 10
    print(variable_test)

test()

# usando el return

def saludar_por_nombre():
    nombre = input("Escribe tu nombre: ")
    saludo = "Hola {}!. Bienvenido al curso de python".format(nombre)
    return saludo

saludar_por_nombre()

def lista ():
    return [1,2,3,4,5]
print(lista()[1:3])

# Argumentos por posicion:

def suma(operando1, operando2):
    return operando1 + operando2
suma(7,5)

#resta
def suma(operando1, operando2):
    return operando1 - operando2
suma(15,20)

# Argumentos por nombre
    # Se ejecutan de forma ordenada ya que se le asigna el valor a cada variable

def resta(a,b):
    return a-b
resta(15,12)
resta(b=12, a=15)

def resta (a,b,c):
    return a-b-c
resta(a=100, b=120, c=900)

# LLamada sin argumentos

def resta(a=10,b=13):
    return a-b
resta()

# Argumento por valor y referencia 





def suma(operando1, operando2):
    return operando1 - operando2
suma(15,20)










