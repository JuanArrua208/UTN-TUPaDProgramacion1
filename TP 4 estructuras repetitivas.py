# Actividad 1
""" 
for num in range(101):
    print(num)
"""

# Actividad 2
""" 
numero_entero = int(input("Ingrese un número entero: "))
digitos = len(str(numero_entero))
print(f"Cantidad de digitos: {digitos}")
"""

# Actividad 3
""" 
a = int(input("Ingrese un valor: "))
b = int(input("Ingrese otro valor: "))
acumulador = 0

for cont in range(a + 1, b):
    acumulador = acumulador + cont

print(f"La suma total de todos los enteros entre esos dos valores es: {acumulador}")
"""

# Actividad 4
""" 
acumulador = 0 

while True:
    numero = int(input("Ingresa un número entero distinto de 0: "))
    if numero != 0:
        acumulador = acumulador + numero
    else:
        break

print(f"La suma de todos los números es {acumulador}")
"""

# Actividad 5
""" 
import random

numero_random = random.randint(0, 9)
contador = 1

numero = int(input("Ingrese un número entre el 0 y 9 incluidos: "))

while numero_random != numero:
    numero = int(input("Ingrese un número entre el 0 y 9 incluidos: "))
    contador += 1

print(f"Ganaste! Te tomó {contador} intentos")
"""

# Actividad 6
""" 
for num in range(100, 0, -2):
    print(num)
"""

# Actividad 7
""" 
acumulador = 0

numero = int(input("Ingrese un número entero positivo: "))

if numero > 0:
    for num in range(0, numero):
        acumulador = acumulador + num
    print(acumulador)
else:
    print("Tendrías que haber puesto un número positivo")
"""

# Actividad 8
""" 
cantidad_iteraciones = 5
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for num in range(cantidad_iteraciones):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares +=1
    
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

print(f"Números pares: {contador_pares}")
print(f"Números impares: {contador_impares}")
print(f"Números positivos: {contador_positivos}")
print(f"Números negativos: {contador_negativos}")
"""

# Actividad 9
""" 
cantidad_iteraciones = 5
acumulador = 0
contador = 0

for num in range(cantidad_iteraciones):
    numero = int(input("Ingrese un número entero: "))
    acumulador = acumulador + numero
    contador += 1

print(f"El promedio de todos los valores es {(acumulador/contador)}")
"""

# Actividad 10
numero = input("Ingrese un número: ")
invertido = ""

for digito in numero:
    invertido = digito + invertido 

print(invertido)
