def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

numero = int(input("Ingrese el numero para calcular el factorial: "))

print(factorial(numero))


def fibonaccino(num):
    lista_fib = []
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return fibonaccino(num - 1) + fibonaccino(num - 2)

# 5 --> 8
# 6 --> 13
# fib --> 1,1,2,3,5,8,13

def mostrar_serie_fibonacci(n):
    serie = []
    for i in range(1, n + 1):
        serie.append(fibonaccino(i))
    return serie


numero = int(input("Ingresa un número: "))
serie = mostrar_serie_fibonacci(numero)
print("Serie de Fibonacci hasta el numero", numero, ":")
print(serie)

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * (potencia(n, m -1))

numero = int(input("Ingresa un número: "))
a_la = int(input("Ingresa un número al cual elevar: "))

print(potencia(numero, a_la))

def decimal_a_binario(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [1]
    else:
        resto = num % 2
        coci = int(num / 2)
        return decimal_a_binario(coci) + [resto]

numero_decimal = int(input("Ingresa un número: "))
print(decimal_a_binario(numero_decimal))


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] != palabra[-1]:
            return False
    return es_palindromo(palabra[1:-1])

palabra = (input("Ingresa una palabra sin espacios ni tildes: "))
print(es_palindromo(palabra))


def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo = n % 10
        resto_numero = n // 10 
        return ultimo + (suma_digitos(resto_numero))

numero_a_sumar = int(input("Ingresa un número: "))
print(suma_digitos(numero_a_sumar))


def contar_bloques(num_bloques):
    if num_bloques == 1:
        return 1
    else:
        return num_bloques + (contar_bloques(num_bloques -1))

numero_bloques = int(input("Ingresa un número: "))
print(contar_bloques(numero_bloques))

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo_digito = numero % 10
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero_a_contar = int(input("Ingresa un número: "))
digito_a_contar = int(input("Ingresa el digito a contar: "))
print(contar_digito(numero_a_contar, digito_a_contar))
