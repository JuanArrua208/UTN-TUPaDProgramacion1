# Juan Arrúa
# TP Manejo de Archivos


# Ejercicio 1
with open("productos.txt", "w") as archivo:
    archivo.write("Manzana,300,40\n")
    archivo.write("Banana,150,80\n")
    archivo.write("Durazno,400,30\n")

""" 
# Ejercicio 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip().split(",")
        print(f"Producto: {linea[0]} | Precio: {linea[1]}$ | Cantidad: {linea[2]}")

# Ejercicio 3
nuevo_producto = input("Ingrese un nuevo producto (Producto,precio,cantidad):")

with open("productos.txt", "a") as archivo:
    archivo.write(nuevo_producto + "\n")
"""

# Ejecricio 4
productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()

        nombre, precio, cantidad = linea.split(",")

        producto = {
            "nombre" : nombre,
            "precio" : int(precio),
            "cantidad" : int(cantidad)
        }

        productos.append(producto)

# Ejercicio 5
buscado = input("Ingrese el producto que desea buscar: ")

bandera = False

for producto in productos:
    if str(producto["nombre"]).lower() == buscado.lower():
        bandera = True
        print(producto)

if bandera == False:
    print("Error")
    
# Ejercicio 6
productos_nuevos = []

while True:
    continuar = input("Desea agregar un nuevo producto (si/no)?: ")
    
    if continuar == "si":
        
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        cantidad = input("Ingrese la cantidad del producto: ")

        producto = f"{nombre},{precio},{cantidad}\n"

        productos_nuevos.append(producto)

    elif continuar == "no":
        break

with open("productos.txt", "w") as archivo:
    archivo.writelines(productos_nuevos)

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
