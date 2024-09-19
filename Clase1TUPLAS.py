#Crear una tupla que contenga los numeros enteros del 1 al 20

Tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

print(Tupla)

#Imprimir desde el indice 10 al 15 de la tupla

Tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print("Los elementos del indice 10 al 15 son",Tupla[10:16])

#Mostrar la cantidad de veces que se encuentra un elemento especifico dentro de la tupla(utilizar count)

Tupla1=(1,2,3,4,6,6,7,5,6)
print("tenemos una nueva tupla y es:",Tupla1)
numero_repetido=6
print("El numero que se repite en esta tupla es el", numero_repetido, "y se repite", Tupla1.count(6), "veces")


#Convertir una tupla en una lista

Tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
lista= list(Tupla)
print("La tupla convertida en lista es", lista)

#Desempaquetar solo los 3 primeros elementos de la tupla en 3 variables.

Tupla=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

n=Tupla[:3]

print("Los primeros tres elementos de la tupla son",n)