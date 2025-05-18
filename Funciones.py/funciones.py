def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

##################################################


def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

##################################################

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

##################################################

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

##################################################

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

##################################################

def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(num)

##################################################

def operaciones_basicas(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Indefinido")

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
suma, resta, multi, div = operaciones_basicas(a, b)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multi}")
print(f"División: {div}")

##################################################

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

##################################################

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Ingrese la temperatura en °C: "))
print(f"{temp}°C equivalen a {celsius_a_fahrenheit(temp):.2f}°F")

##################################################

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))
z = float(input("Ingrese el tercer número: "))
print(f"El promedio es: {calcular_promedio(x, y, z):.2f}")