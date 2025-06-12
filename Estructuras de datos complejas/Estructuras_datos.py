# Diccionario inicial con precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas al diccionario con precio
precios_frutas['Naranja'] = 1200  
precios_frutas['Manzana'] = 1500  
precios_frutas['Pera'] = 2300    

# Mostrando el diccionario actualizado
print("Diccionario de precios actualizado:")
for fruta, precio in precios_frutas.items():
    print(f"{fruta}: {precio}")


