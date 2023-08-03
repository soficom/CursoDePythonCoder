indice = 0

numeros = [0,1,2,3,4,5]
for numero in numeros:
    numeros[indice]*=5
    indice += 1

print(numeros)

print("----------------------------------------------------------------")

# Range = nos permite ir iterando por la lista pero en tiempo de ejecución.

for numero in range(10):
    print(numero)

print("----------------------------------------------------------------")

for numero in range(5, 10):
    print(numero)

print("----------------------------------------------------------------")

for numero in range(0,20,2):
    print(numero)

print("----------------------------------------------------------------")

for numero in range(10):
    print(numero)
else:
    print("Terminamos la cuent") 

print("----------------------------------------------------------------")

for numero in range(10):
    pass
    if numero ==2:
        continue
    elif numero == 8:
        break
    else:
        print("El numero es", numero)

mi_lista = [numero for numero in range(6)]

print(mi_lista)



# Calculadora
while True:

    operacion = input("Ingresar operacion (+, -, *, 'exit'): ")

    if operacion.lower() == "exit":
        print("Programa finalizado")
        break
    elif operacion == "+":
        numero1 = int(input("Ingresa el primer numero: "))
        numero2 = int(input("Ingresa el segundo numero: "))
        suma= numero1 + numero2
        print("la suma de ambos numeros es: ", suma)
    
    elif operacion == "-":
        numero1 = int(input("Ingresa el primer numero: "))
        numero2 = int(input("Ingresa el segundo numero: "))
        resta= numero1 - numero2
        print("la resta de ambos numeros es: ", resta)
    
    elif operacion == "*":
        numero1 = int(input("Ingresa el primer numero: "))
        numero2 = int(input("Ingresa el segundo numero: "))
        multiplicacion = numero1 * numero2
        print("La multiplicacion de ambos numeros es: ", multiplicacion)
        break
    else:
        operacion != "+, -, *, 'exit'"
        print("la operacion no es correcta")



while True:
    numero = int(input("Introduce un número impar: "))
    if numero % 2 != 0:
        break 
    else:
        print("El número ingresado no es impar. Por favor, inténtalo nuevamente.")
print("¡Has ingresado un número impar correctamente!")

print("------------------------------------------------------------------------------")

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for numero in lista:
    print("soy un valor de la lista y valgo", numero)
    numero*=5
    print("Me actualice y valgo", numero)
#variable que se crea en el bucle de la lista

print("------------------------------------------------------------------------------")

# ejercicio hecho en clase 
ancho = int(input("Ingresar ancho del rectángulo: "))
altura = int(input("Ingresar altura del rectángulo: "))

for i in range(altura):
    print(ancho * "*")

print("------------------------------------------------------------------------------")

#que pasa en cada ejemplo

c = 0
while c < 10:
    c +=1
    if c == 2:
        pass
    print('c vale', c)

print("------------------------------------------------------------------------------")
   
c = 0
while c < 10:
    c +=1
    if c == 2:
        continue
    print('c vale', c)

print("------------------------------------------------------------------------------")

c = 0
while c < 10:
    c +=1
    if c == 2:
        break
    print('c vale', c)

print("------------------------------------------------------------------------------")

# Hasta el 'Exit'
numeros = []
no_debo_parar = True
while no_debo_parar:
    numero = input("Ingresar un número entero o la palabra 'exit': ")
    if numero.lower() == "exit":
        no_debo_parar = False
    else:
        numeros.append(int(numero))
print(sum(numeros))

print("------------------------------------------------------------------------------")

# Ingresar cantidad deseada y devolver promedio
cantidad = int(input("Ingresar cantidad deseada de números: "))
suma = 0
for i in range(cantidad):
    num = float(input("Ingresa cantidad deseada de numeros: "))
    suma += num
print(suma/cantidad)

# # Escribir un programa que imprima un triángulo rectángulo de asteriscos de una altura dada.
# # - Entrada esperada: alto=5
# # - Salida esperada:
# # *
# # **
# # ***
# # ****
# *****
alto = 5
for i in range(1, alto + 1):
    print("*" *i)



