# Ejercicio 1
""" 
acumulador = 0
notas = [3, 9, 8, 9, 4, 7, 6, 8, 5, 7]

print(notas)

for nota in notas:
    acumulador += nota

promedio = acumulador / len(notas)

print(f"El promedio de notas es {promedio}")
"""

# Ejercicio 2
""" 
lista_productos = []

for i in range(5):
    producto = input("Ingrese un producto: ")
    lista_productos.append(producto)

lista_productos = sorted(lista_productos)

print(f"Lista ordenada de productos: {lista_productos}")

producto_eliminado = input("Que producto desea eliminar?: ")
lista_productos.remove(producto_eliminado)

producto_viejo = input("Que producto desea actualizar?: ")

if producto_viejo in lista_productos:
    producto_nuevo = input("Ingrese el producto nuevo: ")

    indice = lista_productos.index(producto_viejo)

    lista_productos[indice] = producto_nuevo

    print(lista_productos)
else:
    print("Este producto no se encuentra en la lista")
"""

# Ejercicio 3
""" 
import random

lista_numeros = []
impares = []
pares = []
contador_impares = 0
contador_pares = 0

while len(lista_numeros) < 15:
    numero_random = random.randint(1,100)

    lista_numeros.append(numero_random)

for numero in lista_numeros:
    if numero % 2 == 0:
        pares.append(numero)
        contador_pares += 1
    else:
        impares.append(numero)
        contador_impares += 1

print(f"Números: {lista_numeros}")
print(f"Impares: {impares}, tiene {contador_impares} números")
print(f"Pares: {pares}, tiene {contador_pares} números")
"""

# Ejercicio 4
""" 
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_no_repetidos = []

for dato in datos:
    if dato not in datos_no_repetidos:
        datos_no_repetidos.append(dato)
    else:
        continue

print(f"Lista de datos repetidos: {datos}")
print(f"Lista de datos NO repetidos: {datos_no_repetidos}")
"""

# Ejercicio 5
""" 
estudiantes = ["Juan", "Martina", "Agustina", "Gerundio", "Lucas", "Pepito", "Pilar", "Tomas"]

print(estudiantes)

modificar = input("Desea agregar un nuevo alumno (a) o eliminar uno existente (e)?: ")

if modificar == "a":
    alumno_nuevo = input("Ingrese el nombre del alumno: ")
    
    estudiantes.append(alumno_nuevo)
    print(estudiantes)

else:
    alumno_eliminado = input("Ingrese el nombre del alumno: ")

    if alumno_eliminado in estudiantes:
        estudiantes.remove(alumno_eliminado)
        print(estudiantes)
    else:
        print("No se encuentra dicho alumno")
"""

# Ejercicio 6
""" 
numeros = [1, 2, 3, 4, 5, 6, 7]

print(f"Lista original {numeros}")

ultimo_numero = numeros.pop()

numeros.insert(0, ultimo_numero)

print(f"Lista modificada: {numeros}")
"""

# Ejercicio 7
""" 
acumulador_maximas = 0
acumulador_minimas = 0
amplitud_maxima = float("-inf")

# [minimas, máximas]
temperaturas = [
    [12, 34], # día 1
    [13, 23], # día 2
    [14, 25], # día 3
    [10, 30], # día 4
    [9, 36], # día 5
    [10, 20], # día 6
    [15, 25] # día 7
]

for temp in temperaturas:
    acumulador_maximas += temp[1]
print(f"Promedio de temperaturas máximas: {acumulador_maximas/len(temperaturas)}°C")

for temp in temperaturas:
    acumulador_minimas += temp[0]
print(f"Promedio de temperaturas mínimas: {acumulador_minimas/len(temperaturas)}°C")

print("/////////////")

for temp in temperaturas:
    amplitud_termica = temp[1] - temp[0]

    if amplitud_termica > amplitud_maxima:
        amplitud_maxima = amplitud_termica
        dia = temperaturas.index(temp) + 1
    else:
        continue

print(f"La mayor amplitud térmica fue el día {dia} con una amplitud de {amplitud_maxima}°C")
"""

# Ejercicio 8
""" 
acumulador = 0

acumulador_materia_uno = 0
acumulador_materia_dos = 0
acumulador_materia_tres = 0

notas = [
    [7, 8, 6],   # Estudiante 1
    [5, 9, 7],   # Estudiante 2
    [10, 6, 8],  # Estudiante 3
    [4, 7, 5],   # Estudiante 4
    [9, 9, 10]   # Estudiante 5
]

for estudiante in notas:
    for nota in estudiante:
        acumulador += nota
    print(f"Promedio del estudiante N°{notas.index(estudiante) + 1}: {acumulador/len(estudiante)}")
    acumulador = 0

print("////////////////")

for estudiante in notas:
    acumulador_materia_uno += estudiante[0]
print(f"Promedio notas de primer materia: {acumulador_materia_uno / len(notas)}")

for estudiante in notas:
    acumulador_materia_dos += estudiante[1]
print(f"Promedio notas de segunda materia: {acumulador_materia_dos / len(notas)}")

for estudiante in notas:
    acumulador_materia_tres += estudiante[2]
print(f"Promedio notas de tercer materia: {acumulador_materia_tres / len(notas)}")
"""

# Ejercicio 9
""" 
tablero = [
    ["-", "-", "-"], 
    ["-", "-", "-"], 
    ["-", "-", "-"]
    ]

for fila in tablero:
    for columna in fila:
        print(columna, end="  ")
    print("\n")

for turno in range(2):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"

    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingresá fila (0-2): "))
    col = int(input("Ingresá columna (0-2): "))

    tablero[fila][col] = jugador

    for fila in tablero:
        for columna in fila:
            print(columna, end="  ")
        print("\n")
"""

# Ejercicio 10

ventas = [
    [10, 12, 9, 11, 13, 15, 14],  # Producto 1
    [5, 7, 6, 8, 9, 10, 11],      # Producto 2
    [20, 18, 22, 19, 21, 23, 20], # Producto 3
    [7, 8, 6, 9, 10, 7, 8]        # Producto 4
]

# primer punto
for producto in ventas:
    acumulador = 0

    for venta in producto:
        acumulador += venta
    
    print(f"Total de ventas del producto N°{ventas.index(producto) + 1}: {acumulador}")

print("///////////////////")

# segundo punto  
total_maximo = -1
numero_dia = 0

for dia in range(7):
    total_dia = 0

    for producto in ventas:
        total_dia += producto[dia]

    if total_dia > total_maximo:
        total_maximo = total_dia
        numero_dia = dia

print(f"EL día con mayores ventas totales es el día {numero_dia + 1}, con un total de {total_maximo} ventas")

print("///////////////////")

# tercer punto
ventas_maximas = -1
numero_producto = 0

for producto in ventas:
    acumulador = 0

    for venta in producto:
        acumulador += venta

    if acumulador > ventas_maximas:
        ventas_maximas = acumulador
        numero_producto = ventas.index(producto) + 1

print(f"El maximo de ventas fue en el producto N°{numero_producto} con {ventas_maximas} ventas totales")

