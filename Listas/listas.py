# Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista = [i for i in range(1,100) if i % 4 == 0]
print(lista)

# Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

mis_favoritos = ["chocolate", "montañas", "lectura", "música", "gatos"]

print("El penúltimo elemento es:", mis_favoritos[-2])

# Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
# Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior

palabras = []

palabras.append("sol")
palabras.append("mar")
palabras.append("arena")

print("Lista resultante:", palabras)

# Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo
# como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]


animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"

animales[-1] = "oso"

print("Lista actualizada:", animales)


# Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

"""
    el programa encuentra el número más grande dentro de la lista llamada numeros, lo eimina y luego imprime cómo queda la lista sin ese numero
"""

# Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.


numeros = list(range(10, 31, 5))

print("Los dos primeros números son:", numeros[0], "y", numeros[1])


# Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]


autos[1] = "ferrari"
autos[2] = "cinquecento"

print("Lista actualizada:", autos)

# Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print("Lista de dobles:", dobles)


# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
# Lista original
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

compras[1][1] = "tallarines"

compras[0].remove("pan")

print("Lista actualizada de compras:", compras)

# Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla. 

lista_anidada = [
    15,                      
    True,                    
    [25.5, 57.9, 30.6],      
    False                    
]


print("Lista anidada:", lista_anidada)

