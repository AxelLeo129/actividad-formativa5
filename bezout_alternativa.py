# Algoritmo de Bézout

# Bucle de programación defensiva para asegurar que el usuario ingrese un número válido
while True:
        try:
            # Enteros positivos ingresados por el usuario
            a = int(input("Ingrese un entero positivo a: "))
            b = int(input("Ingrese un entero positivo b: "))
            if a > 0 and b > 0:
                # Ejecución del algoritmo e impresión de los resultados
                c = a % b
                d = a // b

                matriz1 = [
                    [0, 1],
                    [1, -d]
                ]

                matriz3 = [b, c]

                while c > 0:

                    a = matriz3[0]
                    b = matriz3[1]

                    c = a % b
                    d = a // b

                    matriz0 = [
                        [0, 1],
                        [1, -d]
                    ]

                    matrizTemporal = [
                        [0, 0],
                        [0, 0]  
                    ]

                    for i in range(2):  # Filas de A
                        for j in range(2):  # Columnas de B
                            matrizTemporal[i][j] = matriz0[i][0] * matriz1[0][j] + matriz0[i][1] * matriz1[1][j]
                    
                    matriz1 = matrizTemporal

                    matriz3 = [b, c]

                print(f"Los coeficientes de Bézout de {a} y {b} son {matriz1[0][0]} y {matriz1[0][1]}, respectivamente.")
                break
            else:
                print("Entradas inválidas. Debe ingresar un números enteros positivos.")     
        except ValueError:
            print("Entradas inválidas. Debe ingresar un números enteros positivos.")