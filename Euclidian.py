# Algoritmo de Euclides 

def euclidean_mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.
    
    Args:
        a (int): El primer número.
        b (int): El segundo número.
    
    Returns:
        int: El máximo común divisor (MCD) de a y b.
    """
    while b != 0:
        previosBValue = b
        b = a % b
        a = previosBValue
    return a

# Bucle de programación defensiva para asegurar que el usuario ingrese un número válido
while True:
        try:
            # Enteros positivos ingresados por el usuario
            a = int(input("Ingrese un entero positivo a: "))
            b = int(input("Ingrese un entero positivo b: "))
            if a > 0 and b > 0:
                # Ejecución del algoritmo e impresión de los resultados
                mcd = euclidean_mcd(a, b)
                print(f"El mcd de {a} y {b} es {mcd}.")
                break
            else:
                print("Entradas inválidas. Debe ingresar un números enteros positivos.")     
        except ValueError:
            print("Entradas inválidas. Debe ingresar un números enteros positivos.")
