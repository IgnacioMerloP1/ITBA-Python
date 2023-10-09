#EJERCICIO 1
def calcular_promedio(numeros):
    suma=0
    for num in numeros:
        suma += num
    
    return suma / len(numeros)

print(calcular_promedio([5,2,3,5,5]))

#EJERCICIO 2
def contar_vocales(cadena):
    cont=0
    for letra in cadena:
        if letra == 'a' or letra == 'A':
            cont +=1
        elif letra == 'e' or letra == 'E':
            cont +=1
        elif letra == 'i' or letra == 'I':
            cont +=1
        elif letra == 'o' or letra == 'O':
            cont +=1
        elif letra == 'u' or letra == 'U':
            cont +=1    
        else:
            pass
    
    return cont

print(contar_vocales("Hola como EstAs"))






