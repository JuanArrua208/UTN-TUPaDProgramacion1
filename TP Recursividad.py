# Juan Arrúa
# TP Recursividad

# Ejercicio 1
""" 
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("Ingrese un número entero: "))
    
for i in range(1, num + 1):
    print(f"El factorial de {i} es: {factorial(i)}")
"""

# Ejercicio 2
""" 
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

num = int(input("Ingrese un número entero: "))
    
for i in range(1, num + 1):
    print(f"El valor de la posición {i} en la serie de fibonacci es: {fibonacci(i)}")
"""

# Ejercicio 3
""" 
def potencia(base, exponente):
    
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print(potencia(4, 3))
"""

# Ejercicio 4
""" 
def decimal_a_bianrio(num):

    if num < 2:
        return str(num)
    else:
        return decimal_a_bianrio(num // 2) + str(num % 2)
    
print(decimal_a_bianrio(17))
print(type(decimal_a_bianrio(17)))
"""

# Ejercicio 5
""" 
def es_palindromo(palabra):

    if len(palabra) <= 1:
        return True

    if palabra[0] != palabra[-1]:
        return False

    return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra sin espacios ni tildes: ")

if es_palindromo(palabra):
    print(f"La palabra {palabra} es un palíndromo.")
else:
    print(f"La palabra {palabra} no es un palíndromo.")
"""

# Ejercicio 6
""" 
def suma_digitos(n):
    
    if n < 10:
        return n
    else:
        ultimo = n % 10
        resto = n // 10
        return ultimo + suma_digitos(resto)


# Pruebas
print(suma_digitos(1234))  
print(suma_digitos(9))     
print(suma_digitos(305))   
"""

# Ejercicio 7
""" 
def contar_bloques(n):
    
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(1))  
print(contar_bloques(2))  
print(contar_bloques(4))  
"""

#Ejercicio 8

def contar_digito(numero, digito):
    
    if numero < 10:
        return 1 if numero == digito else 0

    ultimo = numero % 10         
    resto = numero // 10       

    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)

print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))