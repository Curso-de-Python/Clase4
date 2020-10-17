'''
-----------------------------
 EJERCICIO N°1
 Bucle while
-----------------------------
 Analiza el programa cuidadosamente. Localiza el cuerpo del ciclo y descubre cómo se sale del cuerpo:
-----------------------------
'''
# Almacenaremos el número más grande actual aquí
numero Mayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
  # ¿Es el número más grande que el número más grande?
  if numero > numeroMayor:
    # Sí si, actualiza el mayor númeroNúmero
    numeroMayor = numero
  # Ingresa el siguiente número
  numero = int (input("Introduce un número o escribe -1 para detener:"))

# Imprimir el número más grande
print("El número más grande es:", numeroMayor)
