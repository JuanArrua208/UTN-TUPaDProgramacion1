# Juan Arrúa
# TP Estructura de Datos Complejos

""" 
# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# Ejercicio 3

lista_frutas = list(precios_frutas.keys())

print(lista_frutas)
"""

# Ejercicio 4
""" 
contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = int(input("Ingrese un número telefónico: "))
    contactos[nombre] = numero

nombre = input("Ingrese el nombre del contacto que desea buscar: ")

if nombre in contactos:
    print(f"El número telefónico de {nombre} es {contactos[nombre]}")
else:
    print("No se encuentre ese nombre")
"""

# Ejercicio 5
""" 
frase = input("Escribe una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

contador_palabras = {}

for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Palabras únicas:")
print(palabras_unicas)

print("Cantidad de veces que aparece cada palabra:")
print(contador_palabras)
"""

# Ejercicio 6
""" 
alumnos = {}
promedio = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota_uno = float(input("Ingrese la primera nota del alumno: "))
    nota_dos = float(input("Ingrese la segunda nota del alumno: "))
    nota_tres = float(input("Ingrese la tercera nota del alumno: "))

    alumnos[nombre] = (nota_uno, nota_dos, nota_tres)
    promedio[nombre] = (nota_uno + nota_dos + nota_tres) / 3

print(f"\n {alumnos}")
print(f"\n {promedio}" )
"""

# Ejercicio 7
""" 
parcial_uno = {1, 2, 3, 4, 5}
parcial_dos = {4, 5, 6, 7}

print(f"Los alumnos que aprobaron ambos parciales: {parcial_uno & parcial_dos}")
print(f"Los alumnos que aprobaron solo uno de los dos parciales: {parcial_uno ^ parcial_dos}")
print(f"Los alumnos que aprobaron al menos un parcial: {parcial_uno | parcial_dos}")
"""

# Ejercicio 8
""" 
stock_productos = {"Manzanas": 50, "Bananas": 30, "Leche": 20, "Pan": 15, "Huevos": 60}

producto = input("Ingrese un producto: ")

if producto in stock_productos:
    print(f"El stock de {producto} es de {stock_productos[producto]} unidades")
    unidades = int(input("Ingrese las unidades que quiere agregar: "))
    stock_productos[producto] += unidades

else:
    print("No tenemos ese producto, agregado exitosamente")
    stock_productos[producto] = 0

print(stock_productos)
"""

# Ejercicio 9
""" 
agenda = {
    ("Lunes", "09:00"): "Reunión con el equipo",
    ("Lunes", "14:00"): "Llamada con proveedor",
    ("Martes", "10:00"): "Clase de Python",
    ("Miércoles", "16:00"): "Cita médica",
    ("Viernes", "12:00"): "Almuerzo con amigos"
}

dia = input("Ingrese día: ")
hora = input("Ingrese hora (00:00): ")

if (dia, hora) in agenda:
    print(f"Actividad: {agenda[dia, hora]}")
else:
    print("No hay actividad")
"""

# Ejercicio 10

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Paraguay": "Asunción",
    "Uruguay": "Montevideo"
}
invertido = {}

for pais in paises_capitales:
    invertido[paises_capitales[pais]] = pais

print(paises_capitales)
print("\n")
print(invertido)

