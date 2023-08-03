# En la función de nuestro ejercicio hay un fallo potencial (aritmético), averigua cuándo sucede y retorna el
# valor None en ese caso especial, en cualquier otro caso devuelve el resultado normal de la función.
# >>> def dividir(a, b):
# return a/b

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:  # Captura la excepción si se intenta dividir entre cero
        return None
    except TypeError:
        print("Error en el tipo de argumentos")
    return resultado

print(
    dividir(12,3)
)