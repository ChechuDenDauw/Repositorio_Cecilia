# Actividad 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

# Actividad 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Actividad 4
edad_categoria = int(input("Ingrese su edad para categorizarlo: "))
if edad_categoria < 12:
    print("Niño/a")
elif edad_categoria < 18:
    print("Adolescente")
elif edad_categoria < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Actividad 5
contrasena = input("Ingrese una contraseña (8 a 14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print("Lista de números:", numeros_aleatorios)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("No se puede determinar un sesgo claro con los valores obtenidos")

# Actividad 7
frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

# Actividad 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opción (1: MAYÚSCULAS, 2: minúsculas, 3: Capitalizado): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida.")

# Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

    # Actividad 10
hemisferio = input("¿En qué hemisferio estás? (N para norte / S para sur): ").strip().upper()
mes = int(input("Ingrese el mes (1 a 12): "))
dia = int(input("Ingrese el día del mes: "))


if not (1 <= mes <= 12 and 1 <= dia <= 31):
    print("Fecha inválida.")
else:
    estacion = ""

    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
    else:
        estacion = "Fecha no reconocida"

    print(f"Te encontrás en {estacion}.")
