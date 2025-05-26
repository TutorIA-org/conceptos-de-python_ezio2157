def pares_cuadrados(lista):
    """
    Recibe una lista de números enteros y devuelve un diccionario donde:
    - Las claves son los números pares de la lista.
    - Los valores son los cuadrados de esos números.
    
    Si la lista está vacía, devuelve un diccionario vacío.
    """
    return {num: num**2 for num in lista if num % 2 == 0}