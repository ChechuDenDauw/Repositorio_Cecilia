#------------ACTIVIDAD 1---------------
# Diccionario inicial con precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas al diccionario con precio
precios_frutas['Naranja'] = 1200  
precios_frutas['Manzana'] = 1500  
precios_frutas['Pera'] = 2300    


#--------------ACTIVIDAD 2-------------
#Actualizacion de precios banana, manzana, melon
precios_frutas['Banana'] = 1330  
precios_frutas['Manzana'] = 1700  
precios_frutas['Melon'] = 2800    

# Mostrando el diccionario actualizado
print("Diccionario de precios actualizado:")
for fruta, precio in precios_frutas.items():
    print(f"{fruta}: {precio}")

#-------------ACTIVIDAD 3----------------
#Lista que contenga únicamente las frutas
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista de frutas
print("Lista de frutas:")
print(lista_frutas)

#-------------ACTIVIDAD 4----------------
# Crear un diccionario vacío para almacenar los contactos
contactos = {}

# Cargar 5 contactos solicitando nombre y número al usuario
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = numero  # Guarda el nombre como clave y el número como valor

print("\nContactos cargados correctamente.")

# Consultar un número por nombre
consulta = input("\nIngrese el nombre del contacto que desea buscar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("El contacto no existe.")


#--------------ACTIVIDAD 5------------
# Solicitar al usuario una frase
frase = input("Ingrese una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Obtener las palabras únicas usando un set
palabras_unicas = set(palabras)

# Crear un diccionario para contar las repeticiones de cada palabra
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Mostrar los resultados
print("Palabras únicas:", palabras_unicas)
print("Cantidad de veces que aparece cada palabra:")
print(conteo_palabras)



#---------------ACTIVIDAD 6---------------
# Crear un diccionario para almacenar los alumnos y sus notas
alumnos = {}

# Pedir los nombres y notas de 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    while True:
        notas = input(f"Ingrese las 3 notas de {nombre}, separadas por espacio: ")
        notas_lista = notas.split()
        if len(notas_lista) == 3:
            try:
                tupla_notas = tuple(map(float, notas_lista))
                break
            except ValueError:
                print("Por favor, ingrese solo números.")
        else:
            print("Debe ingresar exactamente 3 notas.")
    alumnos[nombre] = tupla_notas

# Calcular y mostrar el promedio de cada alumno
print("\nPromedios de cada alumno:")
for nombre, notas in alumnos.items():
    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")
    else:
        print(f"{nombre}: No se ingresaron notas.")


#-----------ACTIVIDAD 7------------
# Sets de ejemplo de estudiantes que aprobaron cada parcial
aprobados_parcial1 = {101, 102, 103, 104, 105}
aprobados_parcial2 = {104, 105, 106, 107}

# 1. Estudiantes que aprobaron ambos parciales (intersección)
ambos = aprobados_parcial1 & aprobados_parcial2
print("Aprobaron ambos parciales:", ambos)

# 2. Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

# 3. Lista total de estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = aprobados_parcial1 | aprobados_parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


#---------ACTIVIDAD 8------------
# Diccionario para almacenar los productos y su stock
stock_productos = {}

while True:
    print("\n--- Gestión de Stock ---")
    producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ").strip()
    if producto.lower() == 'salir':
        break

    # Consultar si el producto ya existe en el diccionario
    if producto in stock_productos:
        print(f"El stock actual de {producto} es: {stock_productos[producto]}")
        try:
            agregar = int(input("¿Cuántas unidades desea agregar al stock? (Ingrese 0 si no desea agregar): "))
            if agregar > 0:
                stock_productos[producto] += agregar
                print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
        except ValueError:
            print("Por favor ingrese un número válido.")
    else:
        try:
            unidades = int(input(f"{producto} no está registrado. ¿Cuántas unidades desea agregar?: "))
            stock_productos[producto] = unidades
            print(f"{producto} agregado con un stock de {unidades} unidades.")
        except ValueError:
            print("Por favor ingrese un número válido.")

print("\nStock final de productos:")
for prod, stock in stock_productos.items():
    print(f"{prod}: {stock}")


#--------------ACTIVIDAD 9-------------
# Diccionario para almacenar la agenda
agenda = {}

# Cargar eventos en la agenda
while True:
    print("\n--- Cargar evento en agenda ---")
    dia = input("Ingrese el día (ej: lunes): ").strip().lower()
    hora = input("Ingrese la hora (ej: 15:00): ").strip()
    evento = input("Ingrese el evento (o 'fin' para terminar): ").strip()
    if evento.lower() == 'fin':
        break
    # Guardar el evento con clave como tupla (día, hora)
    agenda[(dia, hora)] = evento
    print(f"Evento '{evento}' agregado para {dia} a las {hora}.")

# Consultar un evento específico en la agenda
print("\n--- Consultar actividad en la agenda ---")
dia_consulta = input("Ingrese el día a consultar (ej: lunes): ").strip().lower()
hora_consulta = input("Ingrese la hora a consultar (ej: 15:00): ").strip()

clave = (dia_consulta, hora_consulta)
if clave in agenda:
    print(f"Actividad agendada para {dia_consulta} a las {hora_consulta}: {agenda[clave]}")
else:
    print("No hay ninguna actividad agendada para ese día y hora.")




#-------------ACTIVIDAD 10-------------
# Diccionario original: países como clave, capitales como valor
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Italia": "Roma",
    "España": "Madrid"
}

# Crear un nuevo diccionario donde las capitales sean las claves
capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais  # Invertir clave y valor

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital: país):")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")

