# Juan Arrúa
# TP 6 Funciones

# Ejercicio 1
""" 
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()
"""

# Ejercicio 2
""" 
def  saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su numbre: ")

print(saludar_usuario(nombre))
"""

# Ejercicio 3
""" 
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
"""

# Ejercicio 4
""" 
def calcular_area_circulo(radio):
    return 3.14 * (radio * radio)

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = int(input("Ingrese el radio: "))

print(f"Area: {str(calcular_area_circulo(radio))}")
print(f"Perímetro: {str(calcular_perimetro_circulo(radio))}")
"""

# Ejercicio 5
""" 
def segundos_a_horas(segundos):
    return (segundos / 60) / 60

segundos = int(input("Ingrese la cantidad de segundos que desea convertir a horas: "))

print(f"{segundos} son {segundos_a_horas(segundos)} horas")
"""

# Ejercicio 6
""" 
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))

tabla_multiplicar(numero)
"""

# Ejercicio 7
""" 
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b 
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
"""

# Ejercicio 8
""" 
def calcular_imc(peso, altura):
    return peso / (altura**2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

print(f"Indice de masa corporal: {calcular_imc(peso, altura)}")
"""

# Ejercicio 9
""" 
def celsius_a_fahrenheit(celsius):
    return (celsius * (9/5)) + 32

celsius = float(input("Ingrese grados celsius: "))

print(f"Fahrenheit: {celsius_a_fahrenheit(celsius)}")
"""

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

print(f"Promedio: {calcular_promedio(a, b, c)}")