# Algoritmo de Euclides Extendido 
def aEuclidesExt(a, b):
    
    Q0 = [1, 0]  
    Q1 = [0, 1]  
    
    while b != 0:
        q = a // b  
        r = a % b  
        
        a, b = b, r
        
        Q0, Q1 = Q1, [Q0[0] - q * Q1[0], Q0[1] - q * Q1[1]]
    
    
    return a, Q0[0], Q0[1] 

# Bucle de programación defensiva para asegurar que el usuario ingrese un número válido
while True:
    try:
        # Enteros positivos ingresados por el usuario


        a = int(input("Ingrese un entero positivo a: "))
        b = int(input("Ingrese un entero positivo b: "))
        
        # Verificar si los números son positivos
        if a > 0 and b > 0:
            # Calcular el MCD y los coeficientes de Bézout
            mcd, x, y = aEuclidesExt(a, b)
            print(f"El MCD de {a} y {b} es {mcd}.")
            print(f"Coeficientes de Bézout: x = {x}, y = {y}")
            break
        else:
            print("Entradas inválidas. Debe ingresar números enteros positivos.")
    except ValueError:
        print("Entradas inválidas. Debe ingresar números enteros positivos.")
