# Es primo

from criba import criba

# Bucle de programación defensiva para asegurar que el usuario ingrese un número válido
while True:
    try:
        number = int(input("Ingrese un entero positivo n: "))
        if number > 0:
            # Ejecutamos la función `criba` para obtener los números primos y verificar si el número es primo
            result = criba(number=number)

            # Si el número es primo, imprimimos el mensaje correspondiente
            if result['isPrime']:
                print(f"El número {number} es primo.")
            
            # Si no es primo, buscamos el primer divisor del número
            else:
                firstDivisor = 0
                for i in result['sierve']:
                    if number % i == 0:
                        firstDivisor = i
                        break

                # Imprimimos el primer divisor que encontramos
                print(f"El número {number} no es primo, pues lo divide {firstDivisor}.")
            break
        else:
            print("Por favor, ingrese un número positivo.")
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero positivo.")