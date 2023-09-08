def suma(a, b):
    """
    Suma dos números y devuelve el resultado.

    Args:
    - a (int/float): Primer número
    - b (int/float): Segundo número

    Returns:
    int/float: Suma de a y b
    """
    return a + b

def sumar_lista(numeros):
    """
    Suma todos los números en una lista y devuelve el resultado.

    Args:
    - numeros (list of int/float): Lista de números

    Returns:
    int/float: Suma total de la lista de números
    """
    total = 0
    for num in numeros:
        total += num
    return total
