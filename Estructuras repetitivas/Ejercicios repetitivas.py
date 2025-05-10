#Actividad 1:
for i in range(0, 101):
    print(i)

#Actividad 2:
numero = input("Ingrese un número entero: ")
numero_sin_signo = numero.lstrip("-")
cantidad_digitos = len(numero_sin_signo)
print(f"El número tiene {cantidad_digitos} dígitos.")

#Actividad 3:
inicio = int(input("Ingrese el primer número entero: "))
fin = int(input("Ingrese el segundo número entero: "))
menor = min(inicio, fin)
mayor = max(inicio, fin)
suma = 0
for i in range(menor + 1, mayor):
    suma += i
print(f"La suma de los enteros entre {menor} y {mayor} (excluyéndolos) es: {suma}")

#Actividad 4:
suma = 0
while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}")

#Actividad 5:
import random
secreto = random.randint(0, 9)
intentos = 0
adivinado = False
while not adivinado:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

    if intento == secreto:
        adivinado = True
        print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")
    else:
        print("No es el número. Intenta de nuevo.")

#Actividad 6:
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)

#Actividad 7:
limite = int(input("Ingrese un número entero positivo: "))
if limite < 0:
    print("Debe ingresar un número positivo.")
else:
    suma = 0
    for i in range(limite + 1):
        suma += i

    print(f"La suma de los números desde 0 hasta {limite} es: {suma}")

#Actividad 8:
TOTAL_NUMEROS = 100
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(TOTAL_NUMEROS):
    numero = int(input(f"Ingrese el número {i+1}/{TOTAL_NUMEROS}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("\nResumen:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#Actividad 9:
TOTAL_NUMEROS = 100
suma = 0
for i in range(TOTAL_NUMEROS):
    numero = int(input(f"Ingrese el número {i+1}/{TOTAL_NUMEROS}: "))
    suma += numero
media = suma / TOTAL_NUMEROS
print(f"\nLa media de los {TOTAL_NUMEROS} números ingresados es: {media}")

#Actividad 10:
numero = input("Ingrese un número entero: ")
numero_invertido = numero[::-1]
print(f"El número invertido es: {numero_invertido}")
