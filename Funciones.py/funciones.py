def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()


def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
