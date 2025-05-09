# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea

for i in range(0,101):
    print(i)

# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un numero: "))
contador = 0

while  numero > 0:
    numero = numero // 10
    contador += 1

print(f"El numero tiene {contador} digitos")

# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

for i in range(num1 +1, num2):
    print(i)

# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
ingreso = int(input("ingrese numero para sumar: "))
acumulado = 0

while ingreso != 0:
    acumulado += ingreso
    ingreso = int(input("ingrese numero para sumar: "))
    print(acumulado)

# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

incognita = random.randint(0, 9)
intentos = 0
respuesta = int(input("Adivine el num entre 0 y 9: "))

while respuesta != incognita:
    respuesta = int(input("No acerto, ingrese otro num entre 0 y 9: "))
    intentos += 1

print(f"Acertaste! adivinaste el num {incognita} en {intentos} intentos")


# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)

# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("ingrese numero a sumar: "))
rta = 0

for i in range(0, num +1):
    rta = num + 1

print(rta)

# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos.

positivos = 0
negativos = 0
pares = 0
impares = 0

for i in range(100):
    num = int(input("Ingrese un num: "))
    if num >=0:
        positivos += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        negativos += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

# print(f"{positivos} numeros positivos")
# print(f"{negativos} numeros negativos")
# print(f"{pares} numeros pares")
# print(f"{impares} numeros impares")

# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.

contador = 0
res = 0

for i in range(100):
    num = int(input("ingrese un numero: "))
    res = res + num
    contador += 1

media = res/contador

print(f"La media es {media}")

# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Ingrese un número: "))
numero_invertido = 0

while numero != 0:
    digito = numero % 10  # Obtiene el último dígito
    numero_invertido = numero_invertido * 10 + digito  # Construye el número invertido
    numero = numero // 10  # Elimina el último dígito del número original

print(f"El número invertido es: {numero_invertido}")