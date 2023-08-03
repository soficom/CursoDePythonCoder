#un año bisisesto si:
# Es divisible por 4 y no es divisible por 100 ej: 96,1096
# 0, es divisible ppr 400 ej: 2000, 2400

# que el programa nos diga si el año es bisiesto

year = int(input('Ingresar un año:'))

if year % 400 == 0:
    print(f"El año {year} es bisiesto!")
elif year % 4 == 0 and year % 100 != 0:
    print(f"1 El año {year} es bisiesto!")
else:
    print(f"1 El año {year} no es bisiesto!")

#Version 2
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"2 El año {year} es bisiesto!")
else:
    print(f"2 El año {year} no es bisiesto!")

#Version 3
condicion_1 = (year % 400 == 0)
condicion_2 = (year % 4 == 0 and year % 100 != 0)

if condicion_1 or condicion_2:    
    print(f"3 El año {year} es bisiesto!")
else:
    print(f"3 El año {year} no es bisiesto!")

print ("---------------------------------------------------------------------------")


age = int(input("Ingresar edad: "))
name = input("ingresar nombre: ")

condition = (name != "****") and (5 < age < 20) and (4 <= len(name) < 8) and (age * 3 > 35)
print(condition)
#casos de prueba
# nombre = ****, edad = 8 -> False
# nombre = * edad = 4 -> False 
# nombre = * edad = 21 -> False
# nombre = ermenegilda edad = 10 -> False
# nombre = teo edad = 10 -> False
# nombre = micaela edad = 6 -> False
# nombre = micaela edad = 19 -> True


#EJERCICIO 2:

# Para aprobar un crédito, el cliente debe ser mayor de edad.
# Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y un ingreso mayor a 2500 dólares.
# En caso no tenga la antigüedad suficiente,
# su ingreso mensual debe ser como mínimo 4000 dólares.
# Si no cumple ninguna de las condiciones, no se aprueba el crédito

edad = int(input("Ingresar edad: "))
ingresos_mensuales = float(input("Ingresar ingresos mensuales: "))
antiguedad = int(input("Ingresar antigüedad: "))

# condiciones:
# 1. ser mayor de edad
# 2. antiguedad mayor a 3 años ingreso mayor a 2500
# 3. si no se cumple 2. entonces ingreso mayor o igual a 4000

if edad < 18:
    print("Cliente menor de edad. Crédito denegado")
else:
    if antiguedad >= 3 and ingresos_mensuales >= 2500:
        print("Crédito otorgado!")
    elif ingresos_mensuales >= 4000:
        print("Crédito otorgado!")
    else:
        print("Ingresos insuficientes. Crédito denegado!")


# Casos de prueba: (edad, ingresos mensuales, antiguedad)

# a) 17, 2600, 4 -> credito denegado
# b) 18, 2600, 4 -> credito aprobado
# c) 18, 2600, 2 -> credito denegado
# d) 18, 4000, 2 -> credito aprobado
# e) 18, 4001, 2 -> credito aprobado


anio_nacimiento = int(input("ingresar el año de su nacimineto: "))

if anio_nacimiento >= 1920 and anio_nacimiento <= 1940:
    print("Sos generacion Silenciosa")

elif anio_nacimiento >= 1946 and anio_nacimiento <= 1964:
    print("Sos generacion Baby Boomer")

elif anio_nacimiento >= 1965 and anio_nacimiento <= 1979:
    print("Sos generacion X")

elif anio_nacimiento >= 1980 and anio_nacimiento <= 2000:
    print("Sos generacion Y")

elif anio_nacimiento >= 2001 and anio_nacimiento <= 2010:
    print("Sos generacion Z")

else:
    print('Tu generacion no esta dentro de las contempladas')