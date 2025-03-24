# Alumna: Rocío Moyano, comisión 18

# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Por favor, ingresa tu nombre: ")

print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
lugar_residencia = input("Ingresá tu lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

import math

radio = float(input("Ingresá el radio del círculo: "))

area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")


# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Ingresá los segundos que quieras convertir a horas "))

horas = segundos/60

print(f"{segundos} segundos equivalen a {horas}")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingresá un número para calcular su tabla de multiplicar "))

dos = numero * 2
tres = numero * 3
cuatro = numero * 4
cinco = numero * 5
seis = numero * 6
siete = numero * 7
ocho = numero * 8
nueve = numero * 9
diez = numero * 10

print(f"Aqui está la tabla de multiplicar de {numero}:")
print(f"0, {numero}, {dos}, {tres}, {cuatro}, {cinco}, {seis}, {siete}, {ocho}, {nueve}, {diez}")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1 = int(input("Ingresá un número entero, que no sea cero"))
numero_2 = int(input("Ingresá otro número, que tampoco sea cero"))

suma = numero_1 + numero_2
division = numero_1 / numero_2
multiplicacion = numero_1 * numero_2
resta = numero_1 - numero_2

print(f"Suma: {suma}, división: {division}, multiplicación: {multiplicacion}, resta: {resta}")


# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:

peso = int(input("Ingresá tu peso en KG"))
altura = int(input("Ingresá tu altura en MT"))

resultado = peso / (altura **2)

print(f"Tu IMC es de {resultado}")


# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit

celcius = int(input("Ingresá la temperatura en grados celcius para convertirla en farenheit"))

farenheit = 9/5 * celcius + 32
print(f"La temperatura en grados farenheit es {farenheit}")


# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
numero_1 = int(input("Ingresá un número"))
numero_2 = int(input("Ingresá otro número"))
numero_3 = int(input("Ingresá otro número"))
promedio = (numero_1 + numero_2 + numero_3) / 3
print(f"El promedio de los números es {promedio}")