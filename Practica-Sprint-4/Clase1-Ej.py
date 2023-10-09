#Ejercicio 1
n = 4
if n&2!=0:
    print("Weird")
elif n%2==0 and (n <= 5 and n >=2):
    print("Not weird 1")
elif n%2==0 and (n <= 20 and n >=6):
    print("Not weird 2")
elif n&2==0 and n>20:
    print("Not weird 3")

#Ejercicio 2
a=12
b=3
print("La suma de ",a, "+", b, "es: ", a+b) #SUMA
print("La resta de ",a, "-", b, "es: ", a-b) #RESTA
print("El producto de ",a, "*", b, "es: ", a*b) #PRODUCTO

#EJERCICIO 3
n=4
for i in range(n):
    print(i**2)

#EJERCICIO 4
a=5
b=2
print(a,"/",b,"es:", a/b, " - division de flotante.")
print(a,"/",b,"es:", a//b, " - division de enteros.")




