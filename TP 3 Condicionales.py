# Ejercicio 1
""" 
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
"""

# Ejercicio 2
""" 
edad = int(input("Ingrese su nota: "))

if edad >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
"""

# Ejercicio 3
""" 
numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
"""

# Ejercicio 4
""" 
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Eres un niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un/una adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto joven")
else:
    print("Eres un adulto")
"""

# Ejercicio 5
""" 
contrasenia = input("Ingrese una contraseña entre 8 y 14 caracteres (incluyendo 8 y 14): ")
longitud = len(contrasenia)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
"""

# Ejercicio 6
""" 
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and  mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
"""

# Ejercicio 7
""" 
cadena = input("Ingrese una frase o palabra: ")
ultimo_caracter = cadena[-1]
cadena_modificada = cadena + "!"

if ultimo_caracter in "aeiouAEIOU":
    print(cadena_modificada)
else:
    print(cadena)
"""

# Ejercicio 8:
""" 
print("ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
nombre = input("Nombre:")
numero = int(input("Número: "))

if numero == 1:
    nombre = nombre.upper()
elif numero == 2:
    nombre = nombre.lower()
else:
    nombre = nombre.title()

print(nombre)
"""

# Ejercicio 9:
""" 
magnitud = int(input("Ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")
"""

# Ejercicio 10:

emisferio = input("Ingrese el emisferio donde se encuentra N (norte) o S (sur): ")
mes = input("Ingrese mes del año actual (minúscula): ")
dia = int(input("Ingrese día del mes actual (número): "))
estacion = ""

if mes == "diciembre":
    if dia >= 21:
        if emisferio == "S":
            estacion = "Verano"
        else:
            estacion = "Invierno"
    elif dia <= 20:
        if emisferio == "S":
            estacion = "Primavera"
        else:
            estacion = "Otoño"
elif mes == "enero":
    if emisferio == "S":
            estacion = "Verano"
    else:
        estacion = "Invierno"
elif mes == "febrero":
    if emisferio == "S":
            estacion = "Verano"
    else:
        estacion = "Invierno"
elif mes == "marzo":
    if dia >= 21:
        if emisferio == "S":
            estacion = "Otoño"
        else:
            estacion = "Primavera" 
    elif dia <= 20:
        if emisferio == "S":
            estacion = "Verano"
        else:
            estacion = "Invierno"  
elif mes == "abril":
    if emisferio == "S":
            estacion = "Otoño"
    else:
        estacion = "Primavera" 
elif mes == "mayo":
    if emisferio == "S":
            estacion = "Otoño"
    else:
        estacion = "Primavera" 
elif mes == "junio":
    if dia >= 21:
        if emisferio == "S":
            estacion = "Invierno"
        else:
            estacion = "Verano"
    elif dia <= 20:
        if emisferio == "S":
            estacion = "Otoño"
        else:
            estacion = "Primavera"
elif mes == "julio":
    if emisferio == "S":
            estacion = "Invierno"
    else:
        estacion = "Verano"
elif mes == "agosto":
    if emisferio == "S":
            estacion = "Invierno"
    else:
        estacion = "Verano"
elif mes == "septiembre":
    if dia >= 21:
        if emisferio == "S":
            estacion = "Primavera"
        else:
            estacion = "Otoño"
    elif dia <= 20:
        if emisferio == "S":
            estacion = "Invierno"
        else:
            estacion = "Verano"
elif mes == "octubre":
    if emisferio == "S":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif mes == "noviembre":
    if emisferio == "S":
        estacion = "Primavera"
    else:
        estacion = "Otoño"


print(f"Se encuentra en {estacion}")
