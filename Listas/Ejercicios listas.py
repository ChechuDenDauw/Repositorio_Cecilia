#Actividad 1:
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Actividad 2:
mis_favoritos = ["chocolate", "pasta", "pizza", "helado", "empanadas"]
print("El penúltimo elemento es:", mis_favoritos[-2])

#Actividad 3:
lista_vacia = []
lista_vacia.append("Python")
lista_vacia.append("UTN")
lista_vacia.append("Programación")
print("Lista resultante:", lista_vacia)

#Actividad 4:
# Lista original
animales = ["perro", "gato", "conejo", "pez"]
# Reemplazar segundo elemento (índice 1) con "loro"
animales[1] = "loro"
# Reemplazar último elemento (índice -1) con "oso"
animales[-1] = "oso"
print("Lista actualizada:", animales)

#Actividad 5:
#se crea la lista
numeros = [8, 15, 3, 22, 7] 
#busca el numer o mas grande (22) y lo remueve
numeros.remove(max(numeros)) 
#ahora imprime la lista actualizada 
print (numeros)

#Actividad 6:
numeros = list(range(10, 31, 5))
print("Primeros dos elementos:", numeros[:2])

#Actividad 7:
# Lista original
autos = ["sedan", "polo", "suran", "gol"]
# Reemplazo de los valores centrales
autos[1] = "civic"
autos[2] = "focus"
print("Lista actualizada:", autos)

#Actividad 8:
# Crear lista vacía
dobles = []
# Agregar los dobles usando append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

#Actividad 9:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"
# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")
# d) Imprimir la lista resultante
print("Lista de compras actualizada:", compras)

#Actividad 10:
# Crear la lista anidada según lo indicado
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Lista anidada:", lista_anidada)




