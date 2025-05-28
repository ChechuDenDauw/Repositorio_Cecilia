#Funcion recursiva que calcula el factorial de un numero

def factorial(n):
    """Calcula recursivamente el factorial de n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        num = int(input("Ingrese un número entero positivo: "))
        if num < 1:
            print("El número debe ser al menos 1.")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    print(f"\nFactoriales de 1 a {num}:")
    for i in range(1, num + 1):
        print(f"  {i}! = {factorial(i)}")

if __name__ == "__main__":
    main()

#Funcion recursiva que calcula el valor de Fibonacci en la pocision deseada.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    try:
        pos = int(input("Ingrese la posición (entero no negativo) hasta la cual mostrar Fibonacci: "))
        if pos < 0:
            print("El número debe ser 0 o mayor.")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    print(f"\nSerie de Fibonacci hasta la posición {pos}:")
    for i in range(pos + 1):
        print(f"  F({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    main()

#Función recursiva que calculA la potencia de un número base elevado a un exponente.

def potencia(base, exp):
    if exp == 0:
        return 1
    # exp > 0
    return base * potencia(base, exp - 1)

def main():
    try:
        base = float(input("Ingrese la base (número): "))
        exp = int(input("Ingrese el exponente (entero no negativo): "))
        if exp < 0:
            print("El exponente debe ser un entero no negativo.")
            return
    except ValueError:
        print("Entrada inválida. La base debe ser un número y el exponente un entero.")
        return

    resultado = potencia(base, exp)
    print(f"\nResultado:\n  {base}^{exp} = {resultado}")

if __name__ == "__main__":
    main()

#Función recursiva que recibE un número entero positivo en base decimal y devuelve su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

def main():
    try:
        num = int(input("Ingrese un número entero positivo en decimal: "))
        if num < 0:
            print("El número debe ser positivo (>= 0).")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    binario = decimal_a_binario(num)
    print(f"\nLa representación binaria de {num} es: {binario}")

if __name__ == "__main__":
    main()

#Función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto

def es_palindromo(palabra):
    # Caso base: cadenas de longitud 0 o 1 son palíndromos
    if len(palabra) <= 1:
        return True
    # Si los extremos no coinciden, no es palíndromo
    if palabra[0] != palabra[-1]:
        return False
    # Reducir el problema quitando el primer y último carácter
    return es_palindromo(palabra[1:-1])

def main():
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ")
    # Convertir a minúsculas para que la comprobación no sea sensible a mayúsculas
    palabra = palabra.lower()
    if es_palindromo(palabra):
        print(f"'{palabra}' es un palíndromo.")
    else:
        print(f"'{palabra}' no es un palíndromo.")

if __name__ == "__main__":
    main()

#Función recursiva llamada suma_digitos.

def suma_digitos(n):
    # Caso base: si n tiene un solo dígito, su suma es él mismo
    if n < 10:
        return n
    # Paso recursivo: extrae el último dígito y suma al resultado de los dígitos restantes
    return (n % 10) + suma_digitos(n // 10)

def main():
    try:
        num = int(input("Ingrese un número entero positivo: "))
        if num < 0:
            print("El número debe ser un entero positivo.")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    resultado = suma_digitos(num)
    print(f"\nLa suma de los dígitos de {num} es: {resultado}")

if __name__ == "__main__":
    main()

#Función recursiva contar_bloques(n)

def contar_bloques(n):
    if n <= 1:
        return 1
    return n + contar_bloques(n - 1)

def main():
    try:
        n = int(input("Ingrese la cantidad de bloques en el nivel más bajo (entero >= 1): "))
        if n < 1:
            print("El número debe ser al menos 1.")
            return
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    total = contar_bloques(n)
    print(f"\nTotal de bloques necesarios para construir la pirámide de base {n}: {total}")

if __name__ == "__main__":
    main()

#Función recursiva llamada contar_digito(numero, digito

def contar_digito(numero, digito):
    # Caso base: número de un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    # Comparo el último dígito y llamo recursivamente con el resto
    ultimo = numero % 10
    return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        digito = int(input("Ingrese un dígito (0–9): "))
        if numero < 0 or not (0 <= digito <= 9):
            print("Número debe ser >= 0 y dígito entre 0 y 9.")
            return
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar enteros.")
        return

    cuenta = contar_digito(numero, digito)
    print(f"\nEl dígito {digito} aparece {cuenta} vez{'es' if cuenta != 1 else ''} en {numero}.")

if __name__ == "__main__":
    main()
