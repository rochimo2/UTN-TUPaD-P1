import math

def imprimir_hola_mundo():
    print("Hola, Mundo!")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro es {perimetro}")

def segundos_a_horas(segundos):
    horas = segundos/60
    print(f"{segundos} equivalen a {horas} horas.")

def tabla_multiplicar(numero):
    resultado = []
    for i in range(1, 11):
        res = numero * i
        resultado.append(res)
    print(f"Los resultados de la tabla de multiplicar del numero {numero} es {resultado}")


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    print(f"El resultado de las operaciones basicas es: suma: {suma}, resta: {resta}, multiplicacion: {multiplicacion}, division: {division}")


def calcular_imc(peso, altura):
    imc = peso / (altura **2)
    print(f"Su IMC es {imc}")


def celsius_a_farenheit(celsius):
    farenheit = 9/5 * celsius + 32
    print(f"La temperatura en grados farenheit es {farenheit}")


def calcular_promedio(a, b, c):
    promedio = (numero_1 + numero_2 + numero_3) / 3
    print(f"El promedio de los números es {promedio}")


imprimir_hola_mundo()

usuario = input("Ingresá tu nombre: ")
apelido_usuario = input("Ingresá tu apellido: ")
edad_usuario = input("Ingresá tu edad: ")
residencia_usuario = input("Ingresá tu residencia: ")
print()
saludar_usuario(usuario)

informacion_personal(usuario, apelido_usuario, edad_usuario, residencia_usuario)
print()
input_radio = int(input("Ingrese el radio para calcular perimetro y area: "))

calcular_area_circulo(input_radio)
calcular_perimetro_circulo(input_radio)
print()
numero_a_multiplicar = int(input(f"Ingrese un numero para calcular su tabla de multiplicar: "))

tabla_multiplicar(numero_a_multiplicar)
print()
primer_numero_operaciones_basicas = int(input("Ingrese el primer numero para realizar operaciones basicas: "))
segundo_numero_operaciones_basicas = int(input("Ingrese el segundo numero para realizar operaciones basicas: "))

operaciones_basicas(primer_numero_operaciones_basicas, segundo_numero_operaciones_basicas)
print()
peso = int(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

calcular_imc(peso, altura)
print()
celsius = int(input("Ingresá la temperatura en grados celsius para convertirla en farenheit: "))
celsius_a_farenheit(celsius)

numero_1 = int(input("Ingresá un número: "))
numero_2 = int(input("Ingresá otro número: "))
numero_3 = int(input("Ingresá otro número: "))

calcular_promedio(numero_1, numero_2, numero_3)