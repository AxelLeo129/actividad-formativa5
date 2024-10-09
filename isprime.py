from criba import criba

number = int(input("Ingrese un entero positivo n: "))

result = criba(number=number)

if result['isPrime']:
    print(f"El número {number} es primo.")
else:
    firstDivisor = 0
    for i in result['sierve']:
        if number % i == 0:
            firstDivisor = i
            break

    print(f"El número {number} no es primo, pues lo divide {firstDivisor}.")