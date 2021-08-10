# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones
def ordenar (numeros):
    numeros.sort(reverse=True)
    ### No me salía con el dichoso 'sort' así que usé el método de 'la burbuja' primero...###
 #   for num in range(1,len(numeros)):
 #       for n in range(len(numeros)-num):
 #           if numeros[n] > numeros[n+1]:
 #             x = numeros[n]
 #               numeros[n] = numeros[n+1]
 #               numeros[n+1] = x
    return numeros

# --------------------------------
# Aquí dentro definir la función ordenar
#def ordenar (numeros):


# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2, 4, 10, 8, 12, 6]

    # Alumno: Crear la función "ordenar"

    # Generar una una nueva funcion que se llame "ordenar",
    # que utilizaremos para odernar la lista de numeros.
    # Debe recibir 1 parámetro que es la lista de números
    # y retornar la nueva lista ordenada (muy simular a la función promedio)

    # Dentro de la función puede ordenar la lista
    # usando la funciones nativas de Python "sort"

    # Luego de crear la función invocarla en este lugar:
    lista_ordenada = ordenar(numeros)
    # lista_ordenada = ordenar(numeros)
    print(lista_ordenada)
    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar:

    print("terminamos")
