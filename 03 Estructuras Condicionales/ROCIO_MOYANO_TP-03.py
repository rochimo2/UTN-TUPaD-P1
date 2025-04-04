#  Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

print("**" * 10)

# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("**" * 10)

# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("**" * 10)


# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

while edad < 0:
    edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 12:
    print("Usted está en la niñez")
elif edad >= 12 and edad < 18:
    print("Usted está en la adolescencia")
elif edad >= 18 and edad < 30:
    print("Usted está en la juventud, disfrute que no tiene dolor de rodilla")
else:
    print("Usted es un adulto, vaya a pagar las cuentas")

print("**" * 10)

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contraseña = input("Ingrese su contraseña de entre 8 y 14 caracteres: ")

len_contaseña = len(contraseña)
if len_contaseña < 8 or len_contaseña > 14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contraseña correcta")

print("**" * 10)

# escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Se registra un sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Se registra un sesgo negativo o a la izquierda")
else:
    print("No hay sesgos")

print("**" * 10)

# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

palabra = input("ingrese una palabra: ")

if palabra.endswith(("a", "e", "i", "o", "u")):
    print(palabra + "!")

print("**" * 10)

# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
opcion = int(input("""Ingrese un número 1, 2 o 3, dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro: """))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower)
else:
    print(nombre.title())

print("**" * 10)

# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las categorías según la escala de Richter e imprima el resultado por pantalla

magnitud = int(input("Ingrese la magnitud del terremoto: "))


if magnitud < 3:
    print("Terremoto muy leve")
if magnitud >= 3 and magnitud < 4:
    print("Terremoto leve")
if magnitud >= 4 and magnitud < 5:
    print("Terremoto Moderado")
if magnitud < 6:
    print("Terremoto Fuerte")
if magnitud >= 6 and magnitud < 7:
    print("Terremoto muy fuerte")
if magnitud >= 7:
    print("terremoto extremo")

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

from datetime import date

hemisferio = input("Ingrese el hemisferio N/S: ")
dia = int(input("Ingrese que dia del mes es: "))
mes = int(input("ingrese que numero de mes es: "))
año = 2025

try:
    numero_dia = date(año, mes, dia).timetuple().tm_yday
except ValueError:
    print("Ingresó numeros invalidos")
if numero_dia <= 79:
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")
elif numero_dia == 80 or numero_dia <= 171:
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")

elif numero_dia == 172 or numero_dia <= 263:
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")
else:
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")
