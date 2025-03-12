import math

def numero_a_dia(numero):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    if 1 <= numero <= 7:
        return dias[numero - 1]  # Restamos 1 porque las listas en Python empiezan en 0
    else:
        return "Número fuera de rango"

def piramide(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def comparar_numeros(a, b):
    if a > b:
        return "El primer número es mayor que el segundo."
    elif a < b:
        return "El segundo número es mayor que el primero."
    else:
        return "Los números son iguales."


def area_cuadrado(lado: float) -> float:
    return lado ** 2

def area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2

def area_circulo(radio: float) -> float:
    return math.pi * radio ** 2

def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("El número debe ser mayor a 0")
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def unir_palabras(palabras) -> str:
    return " ".join(palabras)

def modificar_lista(lista: list, comando: str, elemento=None) -> list:
    if comando == "add" and elemento is not None:
        lista.append(elemento)
    elif comando == "remove" and elemento in lista:
        lista.remove(elemento)
    return lista

def contar_letra(texto, letra):
    
    #Contador de veces que aparece una letra en un texto, sin distinguir mayúsculas de minúsculas.
    if len(letra) != 1:
        raise ValueError("El segundo argumento debe ser una única letra.")
    
    return texto.lower().count(letra.lower())
