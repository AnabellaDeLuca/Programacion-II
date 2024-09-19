#Crear una lista de 5 elementos e imprimirla 
Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]
print(Lista)

#imprimir por pantalla el tercer elemento
Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]
print(Lista[2])

#Imprimir por pantalla del segundo al cuarto elemento
Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]
print(Lista[1:3])

#Mostrar el tipo de dato de la lista
Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]
print(type(Lista))

#Mostrar los primeros 4 elementos de la lista

Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]

print(Lista[:4])

#agregar una provincia a la lista que ya exista y una que no

Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]

Lista.append("La Pampa")

Lista.append("Tierra del Fuego")

print(Lista)
# Agregar una provincia, pero en cuarta posicion

Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]

Lista.insert(3,"Chubut")

print(Lista)

#Extender otra lista a la ya creada
Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]

Lista2 = ["Jujuy","Santiago del Estero","Tierra del Fuego"]

Lista.extend(Lista2)
print(Lista)

#Eliminar un elemento de la lista 
Lista.remove("La Pampa")
print(Lista)

# Extraer el ultimo elemento de la lista, guardarlo en variable e imprimirlo.
Lista = ["Tucuman","Misiones","Cordoba","La Pampa","Salta"]
Largo_lista=(len(Lista))
print(Largo_lista)

Lista[(Largo_lista-1)]
print(Lista[(Largo_lista-1)])

print(Lista)