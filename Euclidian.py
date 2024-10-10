def euclidean_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ejemplo de uso
a = int(input("Ingrese un entero positivo a: "))
b = int(input("Ingrese un entero positivo b: "))
mcd = euclidean_mcd(a, b)
print(f"El mcd de {a} y {b} es {mcd}.")
