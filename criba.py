# Criba de Eratóstenes

def is_prime(number):
    """
    Indica si el número ingresado es primo.

    Un número primo es aquel que solo tiene dos divisores: 1 y el propio número. 
    Esta función realiza una verificación simple iterando desde 2 hasta el número 
    dado, retornando `False` si encuentra algún divisor exacto. Los números menores 
    que 2 no son primos por definición.

    Args:
        number (int): El número entero a verificar.

    Returns:
        bool: Retorna `True` si el número es primo, de lo contrario `False`.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """

    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def criba(number):
    """
    Aplica la criba de Eratóstenes para encontrar los números primos menores o iguales a un número dado.

    Args:
        number (int): Un número entero positivo que define el límite superior para la búsqueda de primos.

    Returns:
        dict: Un diccionario que contiene:
            - `isPrime` (bool): Indica si el número dado es primo.
            - `sierve` (list): Una lista con todos los números primos menores o iguales al número dado.

    Example:
        >>> criba(19)
        {'isPrime': True, 'sierve': [2, 3, 5, 7, 11, 13, 17, 19]}
    """
    sierve = []
    isPrime = is_prime(number=number)

    # Agregar números impares a la lista, ya que los pares no pueden ser primos (excepto 2)
    for i in range(3, number + 1):
        if i % 2 != 0:
            sierve.append(i)

    # Filtrar los números primos utilizando la función is_prime
    for i in sierve:
        if is_prime(i):
            deleteNumbers = []
            # Busca los múltiplos de cada primo para eliminarlos del resultado final
            for j in sierve:
                if j % i == 0:
                    deleteNumbers.append(j)
            deleteNumbers.remove(i) # No eliminar el número primo
            sierve = [item for item in sierve if item not in deleteNumbers]

    # Insertar 2, ya que es el único número primo par
    sierve.insert(0, 2)

    return {'isPrime': isPrime, 'sierve': sierve}

if __name__ == "__main__":
    # Número solicitado al usuario para calcular los primos menores o iguales a si mismo
    number = int(input("Ingrese un entero positivo n: "))

    result = criba(number=number)

    #Imprime el resultado
    print(f"Los primos menores o iguales a {number} son {result['sierve']}")