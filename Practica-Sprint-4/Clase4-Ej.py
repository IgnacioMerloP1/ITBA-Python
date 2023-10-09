#EJERCICIO 1
#Escribí un programa que reciba una lista de números enteros como entrada. El
#programa debe eliminar los números duplicados de la lista y luego ordenarla de forma
#ascendente. Finalmente, muestra en pantalla la lista resultante sin elementos
#duplicados y ordenada de menor a mayor.

def ordenar(lista):
    conjunto = set(lista)
    lista = list(conjunto)
    return lista
print(ordenar([4,2,2,6,1,9,9,6]))

#Ejercicio 2
#Creá una lista de tuplas llamada "peliculas" que contenga tres tuplas. 
#Cada tupla debe contener el nombre de una película como primer elemento 
#y el género como segundo elemento. Luego, solicita al usuario que ingrese
#un número del 1 al 3 para seleccionar una película de la lista. Muestra 
#en pantalla el nombre y el género de la película seleccionada
"""
def pelicula():
    peliculas = [("Rapidos y furiosos", "Accion"),("Exorcista", "Terror"),("Sin limites","Suspenso")]
    numero = int(input("Ingrese un numero entre 1 y 3 inclusive: "))
    for i in len(peliculas):
        if i == numero:
            print(peliculas.index(i))

pelicula()
"""
#EJERCICIO 3
persona = {
    "nombre": None,
    "edad": None,
    "ciudad": None,
}
nombre= input("Ingrese el nombre de la persona: ")
edad= input("Ingrese la edad de la persona: ")
ciudad= input("Ingrese la ciudad de la persona: ")

persona["nombre"] = nombre
persona["ciudad"] = ciudad
print(persona["nombre"] + " vive en: " +persona["ciudad"])

#EJERCICIO 4
arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

conjunto1 = set(arr1)
numeros_comunes = conjunto1.intersection(arr2)
print(numeros_comunes)


